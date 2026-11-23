# Importação da página original e publicação na Hostinger

A raiz contém o HTML original da página de vendas e a versão anterior à Black Friday, além do gerador histórico e dos ficheiros originais de configuração. Os dois HTML incluem os seus próprios estilos e scripts. A página atual usa a Cakto e a anterior usa a Kiwify. Ambas incluem o Meta Pixel.

Os nove vídeos de campanha e os nove scripts de criação foram arquivados em `criativos/`, mantendo os nomes e os scripts juntos. Os anexos avulsos chegaram sem os caminhos de origem, pelo que esta pasta foi escolhida para os guardar. As imagens dos criativos apresentadas na conversa não estavam disponíveis como ficheiros originais com nomes e caminhos verificáveis.

## Vídeos importados

Os seis MP4 recebidos estão em `media/` com os nomes originais. A página atual usa `vsl-bondade-br-bf2.mp4` e a histórica usa `vsl-bondade-br.mp4`. As três variantes `vsl-bondade-br*.mp4` têm o mesmo SHA-256. Os três cortes e a variante `-bf` não são referenciados pelos HTML.

## Recursos recuperados

As 22 imagens referenciadas pelos dois HTML foram recuperadas do site público da Vercel pelos caminhos originais e validadas como JPEG ou WebP. O inventário local cobre os 12 recursos da página atual e os 18 da versão anterior.

O ZIP integral excedeu o limite de transferência da sessão. O conteúdo das pastas `corpo/`, `_kiwify/` e `.vercel/` não pôde ser conferido. Nenhum dos dois HTML referencia diretamente esses diretórios. Preserve os caminhos originais ao receber o restante material e confira o inventário antes de identificar uma versão completa.

## Publicar a página atual

1. Confirme os 12 recursos referenciados pelo `index.html` sob `media/` antes de montar o pacote.
2. Prepare um pacote com o `index.html` e a árvore `media/` necessária. A página é estática e pode ser servida diretamente. O `vercel.json` fica como referência histórica. O gerador `fazer_pagina.py` sobrescreve o HTML e não faz parte da instalação.
3. Confirme no hPanel o domínio, o diretório público associado (normalmente `public_html`) e o SSL. Antes de atualizar, faça uma cópia dos ficheiros do site de destino.
4. Envie o pacote pelo Gerenciador de Arquivos ou por SFTP, mantendo `index.html` e `media/` no mesmo nível. Mantenha os scripts, os criativos, a versão histórica e os metadados de projeto fora do diretório público.
5. Abra o domínio por HTTPS em desktop e telemóvel. Confira as imagens, o poster, a reprodução e a navegação no vídeo, a resposta `206 Partial Content` a um pedido Range do MP4, e os botões de compra. Use o modo de teste do Meta para verificar eventos, sem concluir compras nem simular eventos de compra.
6. Para atualizar, valide primeiro o pacote completo em ambiente de teste e registe o commit correspondente. Para restaurar, reponha a cópia do HTML e das mídias da mesma versão e repita as verificações por HTTPS.

Nesta importação foram conferidos os caminhos de mídia nos dois HTML, a sintaxe dos blocos JavaScript e dos scripts Python e a leitura das faixas de vídeo dos nove MP4 de campanha. A validação de reprodução do vídeo principal, responsividade com todos os recursos, checkout, rastreamento e domínio público permanece pendente.

Os seis MP4 deste lote passaram na leitura de metadados com ffprobe. O servidor local entregou os dois vídeos referenciados com HTTP 200, tipo `video/mp4` e conteúdo idêntico ao original.
