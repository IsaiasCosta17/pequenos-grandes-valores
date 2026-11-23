"""Gera index.html (Brasil) a partir do desenho da página de Angola.
A página de Angola só é lida, nunca alterada."""
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
ORIGEM = os.path.join(AQUI, "..", "pagina_manual", "index.html")
CHECKOUT = "https://pay.kiwify.com.br/30vy1k8"

s = open(ORIGEM, encoding="utf-8").read()
a, b = s.index("<body>"), s.index("<footer>")

CTA = f'''<p class="price">Manual completo em PDF<b>R$ 37</b></p>
        <a class="cta" href="{CHECKOUT}">
          QUERO O MANUAL
          <small>61 páginas · acesso na hora</small>
        </a>
        <p class="under">Pix ou cartão em até 12x · garantia de 7 dias</p>'''

# os depoimentos e a estante vêm iguais da página de Angola
dep = s[s.index('    <div class="vozes">'):s.index('    <div class="fecho">')]
dep = dep.replace("Depoimentos reais, publicados com autorização.",
                  "Depoimentos reais de mães angolanas, publicados com autorização.")
est = s[s.index('    <div class="estante">'):s.index('    <details>')]
est = (est.replace("Os exercícios resultam melhor quando há leitura em casa.",
                   "As brincadeiras funcionam melhor quando há leitura em casa.")
          .replace("Estes são os livros que costumo sugerir aos pais — procure-os na livraria\n        ou na biblioteca da escola.",
                   "Estes são os livros que costumo indicar — procure na livraria\n        ou na biblioteca da escola.")
          .replace('alt="O Principezinho"', 'alt="O Pequeno Príncipe"')
          .replace("<b>O Principezinho</b>", "<b>O Pequeno Príncipe</b>"))

corpo = f'''<body>

<div class="brand">
  <img src="media/sara-40.webp" alt="Sara Ginga" width="40" height="40">
  <div><b>Sara Ginga</b><span>Manual para pais e educadores</span></div>
</div>

<section class="stage">
  <div class="w">
    <p class="kicker">Pais de crianças de 2 a 6 anos</p>
    <h1>Seu filho não é malcriado.<br><em>Ele está repetindo o que aprendeu.</em></h1>
    <p class="deck">Assista ao vídeo até o fim. A Sara Ginga explica por que isso
      acontece — e o que você pode começar a fazer hoje, em 15 minutos por dia.</p>

    <div class="player" id="player">
      <video id="v" playsinline preload="metadata" poster="media/poster-bondade.jpg">
        <source src="media/vsl-bondade-br.mp4" type="video/mp4">
      </video>
      <button class="cover" id="cover" aria-label="Assistir ao vídeo">
        <span class="play"></span>
        <span class="covertxt">Toque para assistir · 3 min · com som</span>
      </button>
    </div>
    <p class="sound" id="sound">Ligue o som do celular</p>

    <div class="gate">
      <p class="wait" id="wait">O botão aparece quando o vídeo mostrar <b>o que fazer</b>.</p>
      <div class="reveal" id="reveal">
        {CTA}
      </div>
    </div>
  </div>
</section>

<section class="mini" id="mini" hidden>
  <div class="w">
    <h2>O que você recebe</h2>
    <div class="rows">
      <div class="row"><i></i><span><b>50 brincadeiras</b> em 5 capítulos, de 15 a 20 minutos cada</span></div>
      <div class="row"><i></i><span><b>61 páginas</b> coloridas, com espaço para a criança escrever e desenhar</span></div>
      <div class="row"><i></i><span><b>Plano de 30 dias</b> — você sempre sabe por onde seguir</span></div>
      <div class="row"><i></i><span>Materiais que <b>você já tem em casa</b> — nada para comprar</span></div>
    </div>

{dep}    <div class="fecho">
      {CTA}
    </div>

    <div class="autora">
      <div class="top">
        <img data-src="media/sara.webp" alt="Sara Ginga" width="76" height="76">
        <div>
          <b>Sara Ginga</b>
          <span>Educadora · autora do manual</span>
        </div>
      </div>
      <p>Trabalho todos os dias com crianças em idade pré-escolar e com as mães
        que me escrevem. Este manual reúne as brincadeiras que funcionam, escritas
        de um jeito que qualquer pai ou mãe consegue fazer em casa.</p>
      <a class="fb" href="https://www.facebook.com/profile.php?id=61596591507060"
         target="_blank" rel="noopener">Ver minha página no Facebook</a>
    </div>

{est}    <details>
      <summary>Meu filho tem 3 anos. Já serve?</summary>
      <p>Sim. É para crianças de 2 a 6 anos. Com os menores, comece pelos capítulos 1 e 2.</p>
    </details>
    <details>
      <summary>É impresso ou digital?</summary>
      <p>Digital, em PDF. Logo depois do pagamento você vai direto para a página de
        download. Dá para ler no celular ou imprimir em casa — está em tamanho A4.</p>
    </details>
    <details>
      <summary>Como pago?</summary>
      <p>Pix, aprovado na hora, ou cartão de crédito em até 12x. O pagamento é feito
        pela Kiwify, plataforma segura de produtos digitais.</p>
    </details>
    <details>
      <summary>E se não servir para mim?</summary>
      <p>Você tem 7 dias de garantia. Se não gostar, pede o reembolso pela própria
        Kiwify e recebe o dinheiro de volta.</p>
    </details>
  </div>
</section>

'''
s = s[:a] + corpo + s[b:]

TROCAS = [
    ('<html lang="pt">', '<html lang="pt-BR">'),
    ("<title>Ele não é mau — faltam-lhe as ferramentas | Sara Ginga</title>",
     "<title>Seu filho não é malcriado | Meu Manual da Bondade · Sara Ginga</title>"),
    ('content="Veja o vídeo: porque é que o seu filho bate, e o que fazer a partir de amanhã."',
     'content="Assista ao vídeo: por que seu filho bate, grita e não divide — e o que fazer a partir de hoje."'),
    ('content="Ele não é mau — faltam-lhe as ferramentas"',
     'content="Seu filho não é malcriado. Ele está repetindo o que aprendeu."'),
    ("content_name:'Manual 50 Exercicios',\n  content_ids:['manual-50'],content_type:'product',value:5500,currency:'AOA'",
     "content_name:'Manual da Bondade BR',\n  content_ids:['manual-bondade-br'],content_type:'product',value:37,currency:'BRL'"),
    ("KEY='vsl50-visto'", "KEY='bondade-br-visto'"),
    ("Ferramenta educativa; não substitui", "Material educativo; não substitui"),
    ("{content_name:'VSL 50 Exercicios'}", "{content_name:'VSL Bondade BR'}"),
]
for x, y in TROCAS:
    assert x in s, x[:60]
    s = s.replace(x, y)

for proibido in ("Kz", "Multicaixa", "pagar.html", "kwanza", "referência"):
    assert proibido not in s, proibido
open(os.path.join(AQUI, "index.html"), "w", encoding="utf-8").write(s)
print("OK index.html", len(s), "bytes;", s.count(CHECKOUT), "botões para a Kiwify")
