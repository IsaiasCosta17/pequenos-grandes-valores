const express = require('express');
const path = require('node:path');

const app = express();
const port = process.env.PORT || 3000;

app.disable('x-powered-by');
app.get(['/', '/index.html'], (_request, response) => {
  response.sendFile(path.join(__dirname, 'index.html'));
});
app.use('/media', express.static(path.join(__dirname, 'media'), {
  index: false,
  redirect: false,
}));

app.listen(port, '0.0.0.0', () => {
  console.log('Pequenos Grandes Valores a escutar na porta %s', port);
});
