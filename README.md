# exportlink-site

Site da Export Link (PT/ES/EN), publicado em https://www.exportlink.com.br.

- `site/`: arquivos publicados no Cloudflare (o `wrangler.jsonc` aponta para esta pasta).
  - Home, Software, Como trabalhamos, Sobre, Contato, Termos e Privacidade em `/`, `/es/` e `/en/`.
  - `/docs/`: página do produto Export Link Docs (antiga landing do Export Link Pro), gerada pelo build a partir de `src/pt/docs.html`, com estilos próprios em `css/docs.css`. Por enquanto só em português.
  - `css/style.css` e `js/*.js` são editados direto aqui. `js/config.js` tem o WhatsApp e as redes sociais.
- `src/`: partes de cada página (`pt/`, `es/`, `en/`) e `build.py`. Depois de mudar um texto, rode
  `python3 src/build.py`: ele monta cabeçalho, rodapé e metatags em `site/` e gera `sitemap.xml` e `robots.txt`.
- O formulário de contato abre o WhatsApp com a mensagem pronta (o Cloudflare não recebe formulários).
- `PASSO-A-PASSO.md`: como ligar o domínio, o e-mail comercial@ e o deploy. Cada push no `main` publica o site.
