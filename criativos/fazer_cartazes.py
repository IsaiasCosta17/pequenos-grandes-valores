"""Variações do cartaz que vende (cartaz.jpg): mesmo layout, outra emoção.
1080x1350: pergunta a vermelho, faixa amarela, «50 EXERCÍCIOS PRÁTICOS» numa banda escura, foto real."""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1080, 1350
VERM = (206, 17, 17)
AMAR = (255, 221, 0)
AQUI = os.path.dirname(os.path.abspath(__file__))

CARTAZES = {
    # nome: (foto, foco_x 0..1, pergunta, faixa)
    "raiva":     ("raiva", 0.30, "O SEU FILHO FICA COM RAIVA POR TUDO?", "ENSINE O SEU FILHO A ACALMAR-SE SEM GRITOS"),
    "tristeza":  ("tristeza", 0.45, "O SEU FILHO CHORA E NÃO SABE DIZER O QUE SENTE?", "ENSINE O SEU FILHO A RECONHECER AS EMOÇÕES"),
    "nao":       ("nao", 0.45, "O SEU FILHO FAZ BIRRA QUANDO OUVE UM «NÃO»?", "ENSINE O SEU FILHO A LIDAR COM A FRUSTRAÇÃO"),
    "partilhar": ("partilhar", 0.50, "O SEU FILHO NÃO QUER PARTILHAR OS BRINQUEDOS?", "ENSINE O SEU FILHO A PARTILHAR E A ESPERAR A VEZ"),
    "bate":      ("bate", 0.45, "O SEU FILHO BATE NOS COLEGAS?", "ENSINE O SEU FILHO A TRATAR BEM OS OUTROS"),
    "acalmar":   ("acalmar", 0.55, "QUER UM FILHO MAIS CALMO E RESPEITADOR?", "15 MINUTOS POR DIA, COM O QUE JÁ TEM EM CASA"),
}


def fonte(t, estilo="Bold Condensed"):
    f = ImageFont.truetype("bahnschrift.ttf", t)
    f.set_variation_by_name(estilo)
    return f


def quebra(d, txt, fo, larg):
    linhas, l = [], ""
    for p in txt.split():
        t = (l + " " + p).strip()
        if d.textlength(t, font=fo) <= larg:
            l = t
        else:
            linhas.append(l)
            l = p
    return linhas + [l]


def caber(d, txt, larg, maxl, t0):
    """maior tamanho em que o texto cabe em `maxl` linhas"""
    t = t0
    while t > 30:
        fo = fonte(t)
        ls = quebra(d, txt, fo, larg)
        if len(ls) <= maxl:
            return fo, ls
        t -= 4
    return fonte(t), quebra(d, txt, fonte(t), larg)


def cartaz(nome, foto, fx, pergunta, faixa):
    im = Image.new("RGB", (W, H), "white")
    # foto: ocupa de y=300 até ao fim
    f = Image.open(os.path.join(AQUI, "fotos", foto + ".png")).convert("RGB")
    ah = H - 300
    esc = max(W / f.width, ah / f.height)
    f = f.resize((round(f.width * esc), round(f.height * esc)), Image.LANCZOS)
    x = int((f.width - W) * fx)
    im.paste(f.crop((x, 0, x + W, ah)), (0, 300))
    d = ImageDraw.Draw(im)
    # pergunta a vermelho (fundo branco)
    fo, ls = caber(d, pergunta, W - 80, 2, 104)
    alt = fo.size * 0.98
    y0 = 24 + (2 - len(ls)) * alt / 2
    for i, l in enumerate(ls):
        d.text((W / 2, y0 + i * alt), l, font=fo, fill=VERM, anchor="ma", stroke_width=2, stroke_fill=VERM)
    # banda escura translúcida com o «50 EXERCÍCIOS PRÁTICOS»
    banda = Image.new("RGBA", (W, 280), (60, 60, 60, 170))
    im.paste(banda, (0, 320), banda)
    d = ImageDraw.Draw(im)
    f50 = fonte(270)
    fex = fonte(118)
    w50 = d.textlength("50", font=f50)
    wex = max(d.textlength("EXERCÍCIOS", font=fex), d.textlength("PRÁTICOS", font=fex))
    x0 = (W - (w50 + 30 + wex)) / 2
    sombra = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ds = ImageDraw.Draw(sombra)
    for dd, cor in ((ds, (0, 0, 0, 160)), (d, "white")):
        off = 6 if dd is ds else 0
        dd.text((x0 + off, 318 + off), "50", font=f50, fill=cor)
        dd.text((x0 + w50 + 30 + off, 345 + off), "EXERCÍCIOS", font=fex, fill=cor)
        dd.text((x0 + w50 + 30 + off, 460 + off), "PRÁTICOS", font=fex, fill=cor)
        if dd is ds:
            sombra = sombra.filter(ImageFilter.GaussianBlur(6))
            im.paste(sombra, (0, 0), sombra)
            d = ImageDraw.Draw(im)
    # faixa amarela por cima da junção
    ff, lf = caber(d, faixa, W - 120, 1, 56)
    wf = d.textlength(lf[0], font=ff)
    d.rounded_rectangle(((W - wf) / 2 - 26, 236, (W + wf) / 2 + 26, 236 + ff.size + 26), 14, fill=AMAR)
    d.text((W / 2, 236 + 10), lf[0], font=ff, fill="black", anchor="ma", stroke_width=1, stroke_fill="black")
    out = os.path.join(AQUI, f"cartaz-{nome}.jpg")
    im.save(out, quality=93)
    return out


if __name__ == "__main__":
    feitos = []
    for nome, args in CARTAZES.items():
        if os.path.exists(os.path.join(AQUI, "fotos", args[0] + ".png")):
            feitos.append(cartaz(nome, *args))
    t = [Image.open(p).resize((324, 405)) for p in feitos]
    s = Image.new("RGB", (324 * len(t), 405))
    for i, x in enumerate(t):
        s.paste(x, (i * 324, 0))
    s.save(os.path.join(AQUI, "_cartazes.jpg"), quality=85)
    print(len(feitos), "cartazes")
