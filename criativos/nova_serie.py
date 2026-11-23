"""Série 17/11: 4 comportamentos novos, versão Angola (50 EXERCÍCIOS) e Brasil (50 BRINCADEIRAS)."""
import importlib.util, os, subprocess
spec = importlib.util.spec_from_file_location("fc", "fazer_cartazes.py"); fc = importlib.util.module_from_spec(spec); spec.loader.exec_module(fc)
src = open("fazer_cartazes.py", encoding="utf-8").read()
fn = src[src.index("def cartaz("):src.index("if __name__")]
ns_br = dict(vars(fc)); exec(fn.replace('"EXERCÍCIOS"', '"BRINCADEIRAS"').replace('"PRÁTICOS"', '"PRÁTICAS"'), ns_br)
SERIE = [  # nome, foto, foco_x, pergunta, faixa, música, versão
 ("ao-ciume", "ao-ciume", 0.05, "O SEU FILHO TEM CIÚMES DO IRMÃO?", "ENSINE O SEU FILHO A PARTILHAR SEM BIRRAS", "triste", "ao"),
 ("ao-supermercado", "ao-supermercado", 0.45, "O SEU FILHO FAZ BIRRA NA RUA E NO MERCADO?", "ENSINE O SEU FILHO A LIDAR COM O «NÃO»", "birra", "ao"),
 ("ao-ignora", "ao-ignora", 0.22, "O SEU FILHO NÃO OBEDECE QUANDO O CHAMA?", "ENSINE O SEU FILHO A OUVIR SEM GRITOS", "birra", "ao"),
 ("ao-dormir", "ao-dormir", 0.2, "O SEU FILHO NÃO SE ACALMA NEM PARA DORMIR?", "EXERCÍCIOS PARA ACALMAR E RESPIRAR", "calma", "ao"),
 ("br-ciume", "br-ciume", 0.05, "SEU FILHO TEM CIÚME DO IRMÃO?", "ENSINE SEU FILHO A DIVIDIR SEM BIRRA", "triste", "br"),
 ("br-supermercado", "br-supermercado", 0.55, "SEU FILHO FAZ BIRRA NO MERCADO?", "ENSINE SEU FILHO A LIDAR COM O «NÃO»", "birra", "br"),
 ("br-ignora", "br-ignora", 0.2, "SEU FILHO NÃO OBEDECE QUANDO VOCÊ CHAMA?", "ENSINE SEU FILHO A OUVIR SEM GRITOS", "birra", "br"),
 ("br-dormir", "br-dormir", 0.2, "SEU FILHO NÃO SE ACALMA NEM PARA DORMIR?", "BRINCADEIRAS PARA ACALMAR E RESPIRAR", "calma", "br"),
]
os.makedirs("serie-17-11", exist_ok=True)
import sys
so=sys.argv[1:]
for nome, foto, fx, perg, faixa, mus, v in SERIE:
    if so and nome not in so: continue
    f = (ns_br if v == "br" else vars(fc))["cartaz"]
    jpg = f(nome, foto, fx, perg, faixa)
    subprocess.run(["python", os.path.expanduser("~/.claude/skills/formatos-meta/scripts/formatos.py"), jpg, "serie-17-11",
                    os.path.join("musica", mus + ".mp3"), "--nome", nome], check=True)
