# Colocar o site no ar em exportlink.com.br (do zero)

São 5 partes. A parte 1 pode ser feita agora. As partes 2 e 3 levam o domínio para o Cloudflare.
A parte 4 só funciona depois que o domínio estiver **Active**.

---

## Parte 1. Publicar o site no Cloudflare (5 min)

1. Entre em **dash.cloudflare.com** (a mesma conta do export-link).
2. No menu da esquerda, clique em **Compute** e depois em **Workers & Pages**.
3. Clique no botão azul **Create** (canto superior direito).
4. Na aba **Workers**, clique em **Import a repository**.
5. Escolha a conta do GitHub **cassianopajewski77** e o repositório **exportlink-site**.
   - Se ele não aparecer, clique em **Configure GitHub App** / **Add GitHub account** e libere o acesso ao repositório `exportlink-site`.
6. Na tela de configuração, **não mude nada**:
   - Project name: `exportlink-site`
   - Build command: vazio
   - Deploy command: `npx wrangler deploy`
   - Root directory: `/`
7. Clique em **Create and deploy** (ou **Deploy**).
8. Espere cerca de 1 minuto. Quando aparecer **Success**, clique em **Visit**:
   o site abre em `exportlink-site.cassiano-pajewski.workers.dev`.

---

## Parte 2. Adicionar o domínio no Cloudflare (3 min)

1. No menu da esquerda, clique em **Account home** (ou **Domains**).
2. Clique em **Add a domain** (ou **Onboard a domain**).
3. Digite `exportlink.com.br`.
4. Deixe marcado **Quick scan for DNS records** e clique em **Continue**.
5. Escolha o plano **Free** (role a página até o fim) e clique em **Continue**.
6. Aparece a lista de registros DNS. Não precisa mexer em nada: clique em **Continue to activation**.
7. A tela seguinte mostra **dois nameservers** do Cloudflare, por exemplo:
   - `ana.ns.cloudflare.com`
   - `bob.ns.cloudflare.com`

   **Copie os dois** (os seus nomes serão outros). Deixe essa página aberta.

---

## Parte 3. Trocar os DNS no Registro.br (5 min)

1. Entre em **registro.br** e faça login.
2. Na lista de domínios, clique em **exportlink.com.br**.
3. Procure a seção **DNS** e clique em **Alterar servidores DNS**.
4. Apague o que estiver nos campos e preencha:
   - **Servidor 1:** o primeiro nameserver do Cloudflare
   - **Servidor 2:** o segundo nameserver do Cloudflare
   - Deixe os campos de **IP** em branco.
5. Se houver **DNSSEC** ativo, desative.
6. Clique em **Salvar alterações**.
7. Volte à página do Cloudflare (parte 2, item 7) e clique em **Check nameservers now**.

O Registro.br costuma publicar a troca em **1 a 2 horas** (pode levar até 24 h).
Quando o domínio ficar **Active**, o Cloudflare manda um e-mail.

---

## Parte 4. Ligar o site ao domínio (depois do Active, 2 min)

1. Vá em **Workers & Pages** e clique em **exportlink-site**.
2. Abra a aba **Settings** e procure **Domains & Routes**.
3. Clique em **Add** e escolha **Custom domain**.
4. Digite `exportlink.com.br` e clique em **Add domain**.
5. Repita com `www.exportlink.com.br`.
6. Em alguns minutos o Cloudflare cria o DNS e o certificado HTTPS.
   Teste abrindo **https://exportlink.com.br** e **https://www.exportlink.com.br**.

---

## Parte 5. Fazer o comercial@exportlink.com.br receber e-mails (5 min)

1. No Cloudflare, clique no domínio **exportlink.com.br**.
2. No menu do domínio, clique em **Email** e depois em **Email Routing**.
3. Clique em **Get started** / **Enable Email Routing**.
4. Em **Custom address**, digite `comercial`. Em **Destination**, coloque o seu Gmail.
5. Confirme o e-mail de verificação que chega no Gmail.
6. Clique em **Add records and enable** quando o Cloudflare pedir.

Tudo que for enviado para comercial@exportlink.com.br vai cair no seu Gmail.

---

## (Opcional) O sistema em app.exportlink.com.br

Depois do Active: **Workers & Pages → export-link → Settings → Domains & Routes → Add → Custom domain** →
`app.exportlink.com.br`. O endereço `.workers.dev` atual continua funcionando.
