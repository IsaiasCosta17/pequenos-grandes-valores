"""Vídeo de cartaz com a FOTO ANIMADA (Kling) por baixo do texto do cartaz.
Uso: python video_cartaz.py <nome> <foto> <foco_x> <frase> <faixa> <fonte|""> <musica> <clip.mp4> <pasta_saida>
Gera <nome>-anim-4x5.mp4 e <nome>-anim-9x16.mp4 (15 s, H.264 + AAC).
O texto é recortado por «matte de diferença»: o cartaz é desenhado sobre foto preta e sobre foto branca."""
import importlib.util, os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageDraw

AQUI = os.path.dirname(os.path.abspath(__file__)); os.chdir(AQUI)
spec = importlib.util.spec_from_file_location("fc", "fazer_cartazes.py"); fc = importlib.util.module_from_spec(spec); spec.loader.exec_module(fc)
src = open("fazer_cartazes.py", encoding="utf-8").read()
ns = dict(vars(fc))
exec(src[src.index("def cartaz("):src.index("if __name__")].replace('"50"', '"10"').replace('"EXERCÍCIOS"', '"CONVERSAS"').replace('"PRÁTICOS"', '"QUE PROTEGEM"'), ns)

def fonte_linha(im, txt):
    d = ImageDraw.Draw(im, "RGBA"); fo = ns["fonte"](34, "Regular")
    w = d.textlength(txt, font=fo); x0, y0 = 40, 612
    d.rounded_rectangle((x0 - 14, y0 - 8, x0 + w + 14, y0 + 44), 10, fill=(0, 0, 0, 140))
    d.text((x0, y0), txt, font=fo, fill="white")

def overlay(nome, frase, faixa, fon, tmp):
    camadas = []
    for cor in ("_preto", "_branco"):
        Image.new("RGB", (896, 1120), (0, 0, 0) if cor == "_preto" else (255, 255, 255)).save(f"fotos/{cor}.png")
        jpg = ns["cartaz"](nome + cor, cor, 0.5, frase, faixa)
        im = Image.open(jpg).convert("RGB")
        if fon: fonte_linha(im, fon)
        camadas.append(np.asarray(im).astype(np.float32)); os.remove(jpg); os.remove(f"fotos/{cor}.png")
    b, w = camadas
    a = 1 - (w - b).mean(axis=2, keepdims=True) / 255.0
    a = np.clip(a, 0, 1)
    rgb = np.where(a > 0.01, b / np.maximum(a, 0.01), 0)
    out = np.concatenate([np.clip(rgb, 0, 255), a * 255], axis=2).astype(np.uint8)
    p = os.path.join(tmp, "ov.png"); Image.fromarray(out, "RGBA").save(p); return p

def run(c): subprocess.run(c, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main(nome, foto, fx, frase, faixa, fon, mus, clip, outdir):
    os.makedirs(outdir, exist_ok=True)
    tmp = tempfile.mkdtemp()
    ov = overlay(nome, frase, faixa, fon, tmp)
    pp = os.path.join(tmp, "pp.mp4")  # vai-e-volta: 5 s -> 10 s, sem salto
    run(["ffmpeg", "-y", "-i", clip, "-filter_complex", "[0:v]split[a][b];[b]reverse[r];[a][r]concat=n=2:v=1[v]", "-map", "[v]", "-an",
         "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", pp])
    x = f"(iw-1080)*{fx}"
    v45 = os.path.join(outdir, f"{nome}-anim-4x5.mp4")
    run(["ffmpeg", "-y", "-stream_loop", "2", "-i", pp, "-loop", "1", "-t", "15", "-i", ov, "-i", os.path.join("musica", mus + ".mp3"),
         "-filter_complex",
         f"color=white:s=1080x1350:d=15[bg];[0:v]scale=1080:1050:force_original_aspect_ratio=increase,crop=1080:1050:{x}:(ih-1050)*0.3,setsar=1[f];"
         f"[bg][f]overlay=0:300[b2];[b2][1:v]overlay=0:0,format=yuv420p[v];[2:a]atrim=0:15,afade=t=out:st=13.5:d=1.5[a]",
         "-map", "[v]", "-map", "[a]", "-t", "15", "-r", "30", "-c:v", "libx264", "-crf", "20", "-preset", "medium",
         "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", v45])
    v916 = os.path.join(outdir, f"{nome}-anim-9x16.mp4")
    run(["ffmpeg", "-y", "-i", v45, "-filter_complex",
         "[0:v]split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:2,eq=brightness=-0.08[bg];"
         "[bg][b]overlay=0:275,format=yuv420p[v]",
         "-map", "[v]", "-map", "0:a", "-c:v", "libx264", "-crf", "20", "-preset", "medium", "-c:a", "copy", "-movflags", "+faststart", v916])
    print("OK", v45, v916)

if __name__ == "__main__":
    a = sys.argv[1:]
    main(a[0], a[1], float(a[2]), a[3], a[4], a[5], a[6], a[7], a[8])
