"""Cada cartaz vira um vídeo 4:5 de 15 s: zoom lento + música da emoção."""
import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
DUR = 15
MUSICA = {   # cartaz -> música
    "raiva": "tensa", "bate": "tensa",
    "tristeza": "triste",
    "nao": "birra", "partilhar": "birra",
    "acalmar": "calma",
}


def run(args):
    r = subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y"] + args, stdin=subprocess.DEVNULL)
    if r.returncode:
        sys.exit("ffmpeg falhou")


for nome, mus in MUSICA.items():
    img = os.path.join(AQUI, f"cartaz-{nome}.jpg")
    som = os.path.join(AQUI, "musica", f"{mus}.mp3")
    out = os.path.join(AQUI, f"cartaz-{nome}.mp4")
    n = DUR * 30
    run(["-loop", "1", "-framerate", "30", "-i", img, "-i", som,
         "-filter_complex",
         # zoom de 1.00 a 1.06 em 15 s, centrado; escala 2x antes para não tremer
         f"[0:v]scale=2160:2700,zoompan=z='1+0.05*on/{n}':x='iw/2-(iw/zoom/2)':y='0'"
         f":d={n}:s=1080x1350:fps=30,format=yuv420p[v];"
         f"[1:a]aresample=44100,aformat=channel_layouts=stereo,apad,atrim=0:{DUR},"
         f"afade=t=in:d=0.3,afade=t=out:st={DUR - 1.5}:d=1.5,volume=0.9[a]",
         "-map", "[v]", "-map", "[a]", "-frames:v", str(n), "-t", str(DUR),
         "-c:v", "libx264", "-crf", "20", "-preset", "fast", "-c:a", "aac", "-b:a", "160k",
         "-movflags", "+faststart", out])
    print("OK", out, flush=True)
