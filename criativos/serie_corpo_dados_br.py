"""Stock 18/11 (3) BRASIL: cartazes «O Corpo É Meu» com DADOS OFICIAIS do INAC (Angola), no formato do cartaz vencedor.
Fontes (verificadas no PDF a 18/11/2026) — Anuário Brasileiro de Segurança Pública 2026 (FBSP), dados de 2025:
 - 48.038 estupros de menores de 14 anos em 2025 (p. 278) -> 131,6/dia
 - autor familiar 59,2% + outros conhecidos 36,9% = 96,1%; desconhecidos 3,9% (p. 199 e 282; só onde a relação foi registada)
(Linhas abaixo são da versão Angola, mantidas por histórico:)
 - 4 crianças abusadas sexualmente por dia: Paulo Kalesi, director-geral do INAC (RTP, Jun/2026; Observador 05/10/2026)
 - 85% dos casos dentro da família: INAC, jan-abr 2026, 495 casos (RTP/Lusa, Jun/2026)
 - 1.028 casos de violência sexual contra crianças em 2025: INAC (Observador 05/10/2026)
Fotos sem nenhuma cena de abuso."""
import importlib.util, os, subprocess
from PIL import Image, ImageDraw
spec = importlib.util.spec_from_file_location("fc", "fazer_cartazes.py"); fc = importlib.util.module_from_spec(spec); spec.loader.exec_module(fc)
src = open("fazer_cartazes.py", encoding="utf-8").read()
fn = src[src.index("def cartaz("):src.index("if __name__")]
ns = dict(vars(fc))
exec(fn.replace('"50"', '"10"').replace('"EXERCÍCIOS"', '"CONVERSAS"').replace('"PRÁTICOS"', '"QUE PROTEGEM"'), ns)

SERIE = [  # nome, foto, foco_x, frase, faixa, fonte, música
 ("br-130-por-dia", "corpo-br3", 0.3, "MAIS DE 130 CRIANÇAS SÃO ABUSADAS POR DIA NO BRASIL",
  "ENSINE SEU FILHO A PROTEGER O CORPO", "Fonte: Anuário Brasileiro de Segurança Pública 2026", "triste"),
 ("br-96-conhecidos", "corpo-br1", 0.4, "96% DOS ABUSADORES DE CRIANÇAS SÃO FAMILIARES OU CONHECIDOS",
  "NÃO É O ESTRANHO. É QUEM ESTÁ PERTO.", "Fonte: Anuário Brasileiro de Segurança Pública 2026", "tensa"),
 ("br-48-mil", "corpo-br2", 0.4, "48 MIL CASOS DE ABUSO SEXUAL DE CRIANÇAS EM 2025",
  "ENSINE SEU FILHO A CONTAR PARA VOCÊ", "Fonte: Anuário Brasileiro de Segurança Pública 2026", "calma"),
]

def fonte_linha(jpg, txt):
    im = Image.open(jpg).convert("RGB")
    d = ImageDraw.Draw(im, "RGBA")
    fo = ns["fonte"](34, "Regular") if "estilo" in ns["fonte"].__code__.co_varnames else ns["fonte"](34)
    w = d.textlength(txt, font=fo)
    x0, y0 = 40, 612
    d.rounded_rectangle((x0 - 14, y0 - 8, x0 + w + 14, y0 + 44), 10, fill=(0, 0, 0, 140))
    d.text((x0, y0), txt, font=fo, fill="white")
    im.save(jpg, quality=92)

OUT = "stock-corpo-dados-br-18-11"
os.makedirs(OUT, exist_ok=True)
for nome, foto, fx, frase, faixa, fon, mus in SERIE:
    jpg = ns["cartaz"](nome, foto, fx, frase, faixa)
    fonte_linha(jpg, fon)
    subprocess.run(["python", os.path.expanduser("~/.claude/skills/formatos-meta/scripts/formatos.py"), jpg, OUT,
                    os.path.join("musica", mus + ".mp3"), "--nome", nome], check=True)
