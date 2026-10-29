# exportlink-site

Landing page do Export Link Pro, publicada em https://exportlink.com.br.

- `site/`: arquivos publicados (página, imagem da tela, 404, robots.txt). Não tem build.
- `wrangler.jsonc`: Worker do Cloudflare só com arquivos estáticos (`npx wrangler deploy`).
- `PASSO-A-PASSO.md`: como ligar o domínio, o e-mail comercial@ e o deploy.

Contato da demonstração: WhatsApp e e-mail ficam no fim de `site/index.html` (constante `WHATSAPP`).
