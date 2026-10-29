# Colocar a landing page no ar em exportlink.com.br

A página é um site estático: `site/index.html`, a imagem da tela, uma página 404 e o `robots.txt`.
Ela roda num Worker do Cloudflare só com arquivos (`wrangler.jsonc`), do mesmo jeito que o export-link.

## 1. Levar o domínio para o Cloudflare (uma vez)
1. No Cloudflare: **Account Home → Add a domain**, digite `exportlink.com.br` e escolha o plano **Free**.
2. O Cloudflare mostra **dois nameservers** (algo como `xxx.ns.cloudflare.com`).
3. No **Registro.br**: entre no domínio → **DNS → Alterar servidores DNS** e troque pelos dois do Cloudflare.
4. Aguarde o e-mail do Cloudflare dizendo que o domínio está **Active** (costuma levar de minutos a algumas horas).

## 2. Criar o repositório do site
1. No GitHub, crie um repositório **vazio e privado** chamado `exportlink-site` (sem README).
2. O Claude envia os arquivos desta pasta para lá.

## 3. Criar o Worker do site
1. No Cloudflare: **Workers & Pages → Create → Import a repository** → escolha `exportlink-site`.
2. Deixe o comando de deploy como `npx wrangler deploy` e o diretório raiz como `/`.
3. Clique em **Deploy**. O site sobe num endereço `exportlink-site.<sua-conta>.workers.dev`.

## 4. Ligar o domínio
1. No Worker `exportlink-site`: **Settings → Domains & Routes → Add → Custom domain**.
2. Adicione `exportlink.com.br` e depois `www.exportlink.com.br`.
3. O Cloudflare cria o DNS e o certificado HTTPS sozinho.

## 5. (Opcional) O sistema em app.exportlink.com.br
No Worker `export-link` (o gerador online): **Settings → Domains & Routes → Add → Custom domain** →
`app.exportlink.com.br`. O endereço `.workers.dev` antigo continua funcionando.

## Antes de publicar
- WhatsApp comercial já configurado em `site/index.html` (5541992640066).
  O botão "Agendar minha demonstração" abre o WhatsApp com nome, empresa, e-mail e telefone já escritos.
- Preço: a página mostra "Sob consulta".

## E-mail comercial@exportlink.com.br
O endereço aparece na página. Para ele receber mensagens sem contratar e-mail, use o **Email Routing** do
Cloudflare (grátis): no domínio, **Email → Email Routing → Get started**, crie `comercial@exportlink.com.br`
e aponte para o seu Gmail. O Cloudflare cria os registros de DNS sozinho.
