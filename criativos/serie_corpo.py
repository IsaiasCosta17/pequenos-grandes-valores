"""Stock 18/11: cartazes para o novo produto «O Corpo É Meu» (prevenção), no formato do cartaz vencedor.
Banda «10 CONVERSAS QUE PROTEGEM» em vez de «50 EXERCÍCIOS PRÁTICOS». Fotos sem nenhuma cena de abuso."""
import importlib.util, os, subprocess
spec = importlib.util.spec_from_file_location("fc", "fazer_cartazes.py"); fc = importlib.util.module_from_spec(spec); spec.loader.exec_module(fc)
src = open("fazer_cartazes.py", encoding="utf-8").read()
fn = src[src.index("def cartaz("):src.index("if __name__")]
ns = dict(vars(fc))
exec(fn.replace('"50"', '"10"').replace('"EXERCÍCIOS"', '"CONVERSAS"').replace('"PRÁTICOS"', '"QUE PROTEGEM"'), ns)
SERIE = [  # nome, foto, foco_x, pergunta, faixa, música
 ("corpo-quem-contar", "corpo-sozinho", 0.15, "O SEU FILHO SABE A QUEM CONTAR SE ALGUÉM LHE FIZER MAL?", "ENSINE O SEU FILHO A PROTEGER O CORPO", "triste"),
 ("corpo-segredos", "corpo-janela", 0.35, "O SEU FILHO GUARDA SEGREDOS DE SI?", "ENSINE A DIFERENÇA ENTRE SURPRESA E SEGREDO MAU", "tensa"),
 ("corpo-ja-ensinou", "corpo-conversa", 0.4, "JÁ ENSINOU À SUA FILHA QUE O CORPO DELA É DELA?", "CONVERSAS SIMPLES QUE PROTEGEM", "calma"),
 ("corpo-calado", "corpo-sala", 0.0, "O SEU FILHO MUDOU E ANDA CALADO SEM RAZÃO?", "APRENDA OS SINAIS E COMO O PROTEGER", "triste"),
]
OUT = "stock-corpo-18-11"
os.makedirs(OUT, exist_ok=True)
for nome, foto, fx, perg, faixa, mus in SERIE:
    jpg = ns["cartaz"](nome, foto, fx, perg, faixa)
    subprocess.run(["python", os.path.expanduser("~/.claude/skills/formatos-meta/scripts/formatos.py"), jpg, OUT,
                    os.path.join("musica", mus + ".mp3"), "--nome", nome], check=True)
