"""Stock 18/11 (3) BRASIL: cartazes «O Corpo É Meu» com DADOS OFICIAIS do INAC (Angola), no formato do cartaz vencedor.
Fontes (verificadas no PDF a 18/11/2026) — Anuário Brasileiro de Segurança Pública 2026 (FBSP), dados de 2025:
 - 48.038 estupros de menores de 14 anos em 2025 (p. 278) -> 131,6/dia
 - 65,6% dos estupros de vulnerável (menores de 14) na residência (p. 281-282) -> «2 em cada 3»
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

SERIE = [  # nome, foto, foco_x, frase, faixa, fonte, música  — crianças negras (quebra de padrão)
 ("brn-mao-confianca", "corpo-brn0", 0.35, "SEU FILHO TEM 5 ADULTOS DE CONFIANÇA PARA CONTAR?",
  "FAÇA O TESTE DE 1 MINUTO", "", "calma"),
 ("brn-dentro-de-casa", "corpo-brn2", 0.75, "2 EM CADA 3 ABUSOS DE CRIANÇAS ACONTECEM DENTRO DE CASA",
  "NÃO É O ESTRANHO. É QUEM ESTÁ PERTO.", "Fonte: Anuário Brasileiro de Segurança Pública 2026", "tensa"),
 ("brn-dizer-nao", "corpo-brn3", 0.4, "SEU FILHO SABE QUE PODE DIZER NÃO ATÉ PARA QUEM CONHECE?",
  "96% DOS ABUSADORES SÃO FAMILIARES OU CONHECIDOS", "Fonte: Anuário Brasileiro de Segurança Pública 2026", "triste"),
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
    if fon: fonte_linha(jpg, fon)
    subprocess.run(["python", os.path.expanduser("~/.claude/skills/formatos-meta/scripts/formatos.py"), jpg, OUT,
                    os.path.join("musica", mus + ".mp3"), "--nome", nome], check=True)
