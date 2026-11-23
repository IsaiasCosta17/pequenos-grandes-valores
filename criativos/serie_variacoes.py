"""Variações dos vencedores (18/11): mesma copy que vende, gancho e foto novos.
Vencedores 7 dias: C-RAIVA (3 vendas, 6,28 USD), C-TRISTEZA (1, 7,29), AO supermercado (2 vendas c/ 1 USD), BR cartaz raiva (6,50).
Angola = banda «50 EXERCÍCIOS PRÁTICOS»; Brasil = «50 BRINCADEIRAS PRÁTICAS»."""
import importlib.util, os, subprocess, sys
spec = importlib.util.spec_from_file_location("fc", "fazer_cartazes.py"); fc = importlib.util.module_from_spec(spec); spec.loader.exec_module(fc)
src = open("fazer_cartazes.py", encoding="utf-8").read()
fn = src[src.index("def cartaz("):src.index("if __name__")]
ns_br = dict(vars(fc)); exec(fn.replace('"EXERCÍCIOS"', '"BRINCADEIRAS"').replace('"PRÁTICOS"', '"PRÁTICAS"'), ns_br)
SERIE = [  # nome, foto, foco_x, gancho, faixa, música, versão
 ("v-raiva-grita",   "v-raiva-grita",   0.40, "O SEU FILHO GRITA QUANDO NÃO LHE FAZEM A VONTADE?", "ENSINE O SEU FILHO A ACALMAR-SE SEM GRITOS", "tensa", "ao"),
 ("v-raiva-atira",   "v-raiva-atira",   0.40, "O SEU FILHO ATIRA AS COISAS QUANDO SE ZANGA?",      "ENSINE O SEU FILHO A LIDAR COM A RAIVA",      "tensa", "ao"),
 ("v-mercado-chao",  "v-mercado-chao",  0.45, "O SEU FILHO ATIRA-SE AO CHÃO QUANDO OUVE «NÃO»?",  "ENSINE O SEU FILHO A LIDAR COM O «NÃO»",      "birra", "ao"),
 ("v-mercado-praca", "v-mercado-praca", 0.45, "BIRRA NA RUA E TODA A GENTE A OLHAR?", "ENSINE O SEU FILHO A ESPERAR SEM BIRRA",     "birra", "ao"),
 ("v-choro",         "v-choro",         0.40, "O SEU FILHO CHORA POR TUDO E POR NADA?",            "ENSINE O SEU FILHO A DIZER O QUE SENTE",      "triste", "ao"),
 ("vbr-raiva-grita", "vbr-raiva-grita", 0.40, "SEU FILHO GRITA QUANDO NÃO CONSEGUE O QUE QUER?",   "ENSINE SEU FILHO A SE ACALMAR SEM GRITOS",    "tensa", "br"),
 ("vbr-mercado-chao","vbr-mercado-chao",0.45, "SEU FILHO SE JOGA NO CHÃO QUANDO OUVE «NÃO»?",      "ENSINE SEU FILHO A LIDAR COM O «NÃO»",        "birra", "br"),
]
OUT = "variacoes-18-11"
os.makedirs(OUT, exist_ok=True)
so = sys.argv[1:]
for nome, foto, fx, gancho, faixa, mus, v in SERIE:
    if so and nome not in so: continue
    f = (ns_br if v == "br" else vars(fc))["cartaz"]
    jpg = f(nome, foto, fx, gancho, faixa)
    subprocess.run(["python", os.path.expanduser("~/.claude/skills/formatos-meta/scripts/formatos.py"), jpg, OUT,
                    os.path.join("musica", mus + ".mp3"), "--nome", nome], check=True)
