# Validação e publicação do upgrade

## Ponto de restauração

A tag `v1.0-pagina-original` aponta para `e34d656`, a versão da `main` com o HTML original, seus recursos e o servidor Node.js. A implementação está em `feat/upgrade-premium-pgv`.

## Resultados

- Chromium em 320, 360, 375, 390, 414, 430, 768, 820, 1024, 1280, 1366, 1440 e 1920 px. Sem rolagem horizontal nas larguras testadas, imagens HTML carregadas e grelhas com as colunas previstas.
- Capturas da página completa e das nove seções e do rodapé, em 1440 e 390 px. A comparação por seção incluiu composição, hierarquia, proporções, cores e diferenças documentadas em `REFERENCIAS-VISUAIS.md`.
- O primeiro acordeão abriu e fechou com Enter. As cinco perguntas e respostas são as originais. Os componentes usam `details` e `summary` nativos.
- O vídeo original iniciou a reprodução e aceitou navegação no tempo. Duração medida de 182,37 s. Poster aprovado e `preload="none"`.
- Os links de checkout e Facebook correspondem ao HTML original. O checkout respondeu com HTTP 200 e apresentou R$ 29,90, Pix e cartão. Nenhuma compra foi realizada.
- O navegador confirmou uma chamada local para cada evento esperado, incluindo PageView, ViewContent, VideoPlay, VideoHalf, ClicouComprar e InitiateCheckout. Os pedidos externos do Meta foram bloqueados durante a auditoria local. A receção no Events Manager ainda precisa de validação.
- Sem exceções JavaScript nem respostas HTTP de erro para recursos locais durante o teste. Imagens abaixo da dobra usam carregamento diferido e dimensões explícitas. Não foi executada uma auditoria Lighthouse nem medido desempenho numa conexão móvel real.
- O preço riscado, a garantia, o acesso vitalício e a faixa etária seguem a oferta original. A data Black Friday foi omitida por falta de confirmação da vigência. A entrega efetiva por e-mail e o reembolso não foram exercitados numa compra real.

## Hostinger

Para hospedagem estática, o pacote contém `index.html` na raiz e os recursos usados em `media/`. Extraia o pacote apenas no diretório público confirmado. Para o modo Node.js via Git, use a branch `feat/upgrade-premium-pgv` num ambiente de pré-visualização, com entrada `server.js` e arranque `npm start`. A aplicação não requer build. A branch de publicação anterior continua disponível para restauração.

Faça uma cópia do conteúdo publicado antes de trocar a versão. Depois de confirmar domínio e diretório de produção, valide a página por HTTPS, reproduza o vídeo e confirme o checkout e o rastreamento no ambiente autorizado. Para restaurar, volte à versão `v1.0-pagina-original` ou à cópia do site anterior. Esta entrega não implanta em produção.
