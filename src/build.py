#!/usr/bin/env python3
"""Gera o HTML estático do site da Export Link.

O site publicado não precisa deste script: ele só monta o topo, o rodapé e as
meta tags iguais em todas as páginas. Rode com:  python3 build.py
Lê o conteúdo de cada página em <idioma>/<pagina>.html e grava em ../site-exportlink/.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "site")
BASE = "https://www.exportlink.com.br/"

# slug "" é a página inicial
PAGES = ["", "sobre", "consultoria", "software", "docs", "treinamentos", "contato", "termos", "privacidade"]
# páginas que pertencem a outra no menu (fica destacado o item do pai)
NAV_PARENT = {"docs": "software"}
# CSS extra de algumas páginas
EXTRA_CSS = {"docs": "css/docs.css"}


def has_page(lang, slug):
    return os.path.exists(os.path.join(HERE, lang, (slug or "index") + ".html"))
LANGS = {
    "pt": {"dir": "", "html": "pt-BR", "og": "pt_BR"},
    "es": {"dir": "es/", "html": "es", "og": "es_LA"},
    "en": {"dir": "en/", "html": "en", "og": "en_US"},
}

T = {
    "pt": {
        "skip": "Pular para o conteúdo",
        "home_label": "Export Link Global Solutions, página inicial",
        "nav": {"sobre": "Sobre nós", "consultoria": "Serviços", "software": "Produtos", "treinamentos": "Treinamentos"},
        "foot": {"": "Início", "contato": "Contato"},
        "nav_label": "Principal",
        "lang_label": "Idioma",
        "demo": "Agendar uma conversa",
        "menu": "Abrir menu",
        "tagline": "Suporte à exportação para empresas brasileiras.",
        "h_pages": "Páginas", "h_contact": "Contato", "h_lang": "Idioma",
        "terms": "Termos de Uso", "privacy": "Política de Privacidade",
        "hours": "Segunda a sexta, das 9h às 18h",
        "disclaimer": "A Export Link não é despachante, nem transportadora, nem representante comercial.",
        "wa_float": "Olá! Vim pelo site da Export Link.",
        "wa_label": "Falar no WhatsApp",
        "copied": "Copiado",
        "pages": {
            "": ("Export Link | Suporte à exportação e software para exportar",
                 "A Export Link monta dentro da sua empresa um ecossistema de exportação: método, documentos, preço por Incoterm e um modelo de negócio replicável em vários países."),
            "software": ("Software Export Link | Documentos e preço de exportação",
                         "Proforma, commercial invoice e packing list em PDF e Excel, cadastros com validação fiscal das Américas e formação de preço por Incoterm, inclusive DDP para os EUA."),
            "docs": ("Export Link Docs | Proforma, invoice e packing list para exportação",
                     "Export Link Docs, módulo do software Export Link: digite o pedido uma vez e receba proforma, commercial invoice e packing list em PDF e Excel."),
            "treinamentos": ("Treinamentos em exportação | Export Link",
                             "Treinamentos da Export Link para a sua equipe: o método de exportação da empresa, documentos, preço por Incoterm e o uso do software Export Link."),
            "consultoria": ("Como trabalhamos | Ecossistema de exportação | Export Link",
                            "A Export Link monta o ecossistema de exportação dentro da sua empresa, com um modelo de negócio replicável em vários países. Comece pela pesquisa de mercado orientativa ou pela análise prévia de exportação."),
            "sobre": ("Sobre a Export Link e o fundador Cassiano Pajewski",
                      "A Export Link dá às empresas brasileiras as ferramentas e a orientação para exportar. Conheça a empresa e a trajetória do fundador, Cassiano Pajewski."),
            "contato": ("Contato | Export Link",
                        "Fale com a Export Link pelo formulário, WhatsApp +55 41 99264-0066 ou comercial@exportlink.com.br. Itajaí, Santa Catarina."),
            "termos": ("Termos de Uso | Export Link",
                       "Termos de uso do site e dos serviços da Export Link Global Solutions."),
            "privacidade": ("Política de Privacidade (LGPD) | Export Link",
                            "Como a Export Link coleta, usa e protege dados pessoais, de acordo com a LGPD."),
        },
    },
}

T["es"] = {
    "skip": "Saltar al contenido",
    "home_label": "Export Link Global Solutions, página de inicio",
    "nav": {"sobre": "Nosotros", "consultoria": "Servicios", "software": "Productos", "treinamentos": "Capacitaciones"},
    "foot": {"": "Inicio", "contato": "Contacto"},
    "nav_label": "Principal",
    "lang_label": "Idioma",
    "demo": "Agendar una conversación",
    "menu": "Abrir menú",
    "tagline": "Soporte a la exportación para empresas brasileñas.",
    "h_pages": "Páginas", "h_contact": "Contacto", "h_lang": "Idioma",
    "terms": "Términos de Uso", "privacy": "Política de Privacidad",
    "hours": "Lunes a viernes, de 9 a 18 h (hora de Brasil)",
    "disclaimer": "Export Link no es agente de aduanas, ni transportista, ni representante comercial.",
    "wa_float": "¡Hola! Llegué desde el sitio de Export Link.",
    "wa_label": "Hablar por WhatsApp",
    "copied": "Copiado",
    "pages": {
        "": ("Export Link | Soporte a la exportación y software para exportar",
             "Export Link monta dentro de su empresa un ecosistema de exportación: método, documentos, precio por Incoterm y un modelo de negocio replicable en varios países."),
        "software": ("Software Export Link | Documentos y precio de exportación",
                     "Proforma, commercial invoice y packing list en PDF y Excel, registros con validación fiscal de las Américas y formación de precio por Incoterm, incluso DDP a EE. UU."),
        "treinamentos": ("Capacitaciones en exportación | Export Link",
                         "Capacitaciones de Export Link para su equipo: el método de exportación de la empresa, documentos, precio por Incoterm y el uso del software Export Link."),
        "consultoria": ("Cómo trabajamos | Ecosistema de exportación | Export Link",
                        "Export Link monta el ecosistema de exportación dentro de su empresa, con un modelo de negocio replicable en varios países. Empiece por la investigación de mercado orientativa o por el análisis previo de exportación."),
        "sobre": ("Sobre Export Link y su fundador, Cassiano Pajewski",
                  "Export Link da a las empresas brasileñas las herramientas y la orientación para exportar. Conozca la empresa y la trayectoria de su fundador."),
        "contato": ("Contacto | Export Link",
                    "Comuníquese con Export Link por el formulario, WhatsApp +55 41 99264-0066 o comercial@exportlink.com.br. Itajaí, Santa Catarina, Brasil."),
        "termos": ("Términos de Uso | Export Link",
                   "Términos de uso del sitio y de los servicios de Export Link Global Solutions."),
        "privacidade": ("Política de Privacidad | Export Link",
                        "Cómo Export Link recopila, usa y protege los datos personales, de acuerdo con la LGPD de Brasil."),
    },
}

T["en"] = {
    "skip": "Skip to content",
    "home_label": "Export Link Global Solutions, home page",
    "nav": {"sobre": "About us", "consultoria": "Services", "software": "Products", "treinamentos": "Training"},
    "foot": {"": "Home", "contato": "Contact"},
    "nav_label": "Main",
    "lang_label": "Language",
    "demo": "Book a call",
    "menu": "Open menu",
    "tagline": "Export support for Brazilian companies.",
    "h_pages": "Pages", "h_contact": "Contact", "h_lang": "Language",
    "terms": "Terms of Use", "privacy": "Privacy Policy",
    "hours": "Monday to Friday, 9 am to 6 pm (Brasília time)",
    "disclaimer": "Export Link is not a customs broker, a carrier or a sales agent.",
    "wa_float": "Hi! I found you through the Export Link website.",
    "wa_label": "Chat on WhatsApp",
    "copied": "Copied",
    "pages": {
        "": ("Export Link | Export support and export software",
             "Export Link builds an export ecosystem inside your company: method, documents, pricing by Incoterm and a business model you can replicate in many countries."),
        "software": ("Export Link software | Export documents and pricing",
                     "Pro forma, commercial invoice and packing list in PDF and Excel, tax ID validation across the Americas and export pricing by Incoterm, including DDP to the US."),
        "treinamentos": ("Export training | Export Link",
                         "Export Link training for your team: your company's export method, documents, Incoterm pricing and how to use the Export Link software."),
        "consultoria": ("How we work | Export ecosystem | Export Link",
                        "Export Link builds the export ecosystem inside your company, with a business model you can replicate in many countries. Start with a market research report or an export pre-assessment."),
        "sobre": ("About Export Link and founder Cassiano Pajewski",
                  "Export Link gives Brazilian companies the tools and guidance to export on their own. Meet the company and its founder."),
        "contato": ("Contact | Export Link",
                    "Reach Export Link through the form, WhatsApp +55 41 99264-0066 or comercial@exportlink.com.br. Itajaí, Santa Catarina, Brazil."),
        "termos": ("Terms of Use | Export Link",
                   "Terms of use for the Export Link Global Solutions website and services."),
        "privacidade": ("Privacy Policy | Export Link",
                        "How Export Link collects, uses and protects personal data under Brazil's LGPD."),
    },
}

WA_ICON = '<svg class="icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.4.8 3.2.6a2.8 2.8 0 0 0 1.8-1.3 2.3 2.3 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3Z"/></svg>'


def url_of(lang, slug):
    return LANGS[lang]["dir"] + (slug + "/" if slug else "")


def rel(from_path, to_path):
    """Caminho relativo entre duas páginas (ex.: 'software/' -> 'es/software/')."""
    depth = from_path.count("/")
    r = "../" * depth + to_path
    return r or "./"


def lang_switch(lang, slug, here):
    parts = []
    for code in ("pt", "es", "en"):
        label = code.upper()
        target = slug if has_page(code, slug) else "software"
        if code == lang:
            parts.append(f'<span aria-current="true" lang="{LANGS[code]["html"]}">{label}</span>')
        else:
            parts.append(f'<a href="{rel(here, url_of(code, target))}" lang="{LANGS[code]["html"]}" hreflang="{LANGS[code]["html"]}">{label}</a>')
    return '<span class="sep">|</span>'.join(parts)


def jsonld(lang):
    data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Organization",
                "@id": BASE + "#org",
                "name": "Export Link Global Solutions",
                "url": BASE,
                "logo": BASE + "img/exportdocspro-simbolo.svg",
                "email": "comercial@exportlink.com.br",
                "telephone": "+55 41 99264-0066",
                "address": {"@type": "PostalAddress", "streetAddress": "Rua Gil Stein, 258",
                            "addressLocality": "Itajaí", "addressRegion": "SC", "addressCountry": "BR"},
                "founder": {"@type": "Person", "name": "Cassiano Pajewski"},
            },
            {
                "@type": "SoftwareApplication",
                "name": "Export Link",
                "alternateName": "Export Link Docs",
                "applicationCategory": "BusinessApplication",
                "inLanguage": LANGS[lang]["html"],
                "description": T[lang]["pages"]["software"][1],
                "publisher": {"@id": BASE + "#org"},
            },
        ],
    }
    return json.dumps(data, ensure_ascii=False, indent=2)


def page(lang, slug, body):
    t = T[lang]
    L = LANGS[lang]
    here = url_of(lang, slug)
    P = rel(here, "")
    if P == "./":
        P = ""
    title, desc = t["pages"][slug]
    canonical = BASE + here
    alts = "\n".join(
        f'<link rel="alternate" hreflang="{LANGS[c]["html"]}" href="{BASE + url_of(c, slug)}">' for c in LANGS if has_page(c, slug)
    ) + f'\n<link rel="alternate" hreflang="x-default" href="{BASE + url_of("pt", slug)}">'
    og_alt = "\n".join(f'<meta property="og:locale:alternate" content="{LANGS[c]["og"]}">' for c in LANGS if c != lang and has_page(c, slug))

    def nav_link(s):
        cur = ' aria-current="page"' if s == NAV_PARENT.get(slug, slug) else ""
        return f'<a href="{rel(here, url_of(lang, s))}"{cur}>{t["nav"][s]}</a>'

    nav = "\n      ".join(nav_link(s) for s in t["nav"])
    foot_links = {"": t["foot"][""], **t["nav"], "contato": t["foot"]["contato"]}
    foot_pages = "\n          ".join(f'<li><a href="{rel(here, url_of(lang, s))}">{label}</a></li>' for s, label in foot_links.items())
    demo_href = rel(here, url_of(lang, "contato")) + "?interesse=consultoria"
    home = rel(here, url_of(lang, ""))
    extra_css = f'\n<link rel="stylesheet" href="{P}{EXTRA_CSS[slug]}">' if slug in EXTRA_CSS else ""
    body = body.replace("{P}", P).replace("{L}", rel(here, L["dir"]) if L["dir"] else P)

    return f"""<!doctype html>
<html lang="{L['html']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{canonical}">
{alts}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Export Link Global Solutions">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{BASE}img/og-image.jpg">
<meta property="og:locale" content="{L['og']}">
{og_alt}
<link rel="icon" href="{P}favicon.ico" sizes="any">
<link rel="icon" href="{P}favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="{P}css/style.css">{extra_css}
<script type="application/ld+json">
{jsonld(lang)}
</script>
</head>
<body>
<a class="skip" href="#conteudo">{t['skip']}</a>

<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{home}" aria-label="{t['home_label']}">
      <svg class="brand__mark" viewBox="0 0 30 30" aria-hidden="true"><rect x="1" y="1" width="28" height="28" rx="7" fill="#00875A"/><path d="M8 19l5-8 4 5 5-7" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      <span class="brand__text"><span class="brand__name">Export Link</span><span class="brand__sub">Global Solutions</span></span>
    </a>
    <nav id="site-nav" class="nav" aria-label="{t['nav_label']}">
      {nav}
      <a class="btn btn--primary nav-cta-mobile" href="{demo_href}">{t['demo']}</a>
    </nav>
    <div class="lang" aria-label="{t['lang_label']}">
      {lang_switch(lang, slug, here)}
    </div>
    <a class="btn btn--primary header-cta" href="{demo_href}">{t['demo']}</a>
    <button class="menu-toggle" type="button" aria-controls="site-nav" aria-expanded="false" aria-label="{t['menu']}">
      <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
    </button>
  </div>
</header>

<main id="conteudo">
{body.strip()}
</main>

<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="brand" href="{home}"><svg class="brand__mark" viewBox="0 0 30 30" aria-hidden="true"><rect x="1" y="1" width="28" height="28" rx="7" fill="#00875A"/><path d="M8 19l5-8 4 5 5-7" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="brand__text"><span class="brand__name">Export Link</span><span class="brand__sub">Global Solutions</span></span></a>
        <p class="footer-tagline">{t['tagline']}</p>
        <div class="social">
          <a data-social="linkedin" href="#" hidden target="_blank" rel="noopener" aria-label="LinkedIn"><svg class="icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5ZM3 9h4v12H3zM9 9h3.8v1.7h.1c.5-1 1.8-2 3.8-2 4 0 4.8 2.6 4.8 6V21h-4v-5.6c0-1.3 0-3-1.9-3s-2.1 1.4-2.1 2.9V21H9z"/></svg></a>
          <a data-social="instagram" href="#" hidden target="_blank" rel="noopener" aria-label="Instagram"><svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg></a>
        </div>
      </div>
      <div>
        <h2>{t['h_pages']}</h2>
        <ul>
          {foot_pages}
        </ul>
      </div>
      <div>
        <h2>{t['h_contact']}</h2>
        <ul>
          <li>WhatsApp: +55 41 99264-0066</li>
          <li>comercial@exportlink.com.br</li>
          <li>Rua Gil Stein, 258 · Itajaí · SC</li>
          <li>{t['hours']}</li>
        </ul>
      </div>
      <div>
        <h2>{t['h_lang']}</h2>
        <div class="lang">{lang_switch(lang, slug, here)}</div>
        <ul class="footer-legal-links">
          <li><a href="{rel(here, url_of(lang, 'termos'))}">{t['terms']}</a></li>
          <li><a href="{rel(here, url_of(lang, 'privacidade'))}">{t['privacy']}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-legal">
      <span>© 2026 Export Link Global Solutions</span>
      <span>{t['disclaimer']}</span>
    </div>
  </div>
</footer>

<a class="wa-float" data-wa="{t['wa_float']}" href="https://wa.me/5541992640066" target="_blank" rel="noopener" aria-label="{t['wa_label']}">
  {WA_ICON.replace('class="icon" ', '')}
</a>

<script src="{P}js/config.js"></script>
<script src="{P}js/main.js" defer></script>
</body>
</html>
"""


def main():
    built = []
    for lang in T:
        for slug in PAGES:
            src = os.path.join(HERE, lang, (slug or "index") + ".html")
            if not os.path.exists(src):
                continue
            body = open(src, encoding="utf-8").read().replace("{WA_ICON}", WA_ICON)
            out_dir = os.path.join(OUT, url_of(lang, slug))
            os.makedirs(out_dir, exist_ok=True)
            with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
                f.write(page(lang, slug, body))
            built.append(url_of(lang, slug) or "/")
    write_sitemap()
    print("Páginas geradas:", ", ".join(built))


def write_sitemap():
    rows = []
    for lang in T:
        for slug in PAGES:
            if not has_page(lang, slug):
                continue
            alts = "".join(
                f'\n    <xhtml:link rel="alternate" hreflang="{LANGS[c]["html"]}" href="{BASE + url_of(c, slug)}"/>' for c in T if has_page(c, slug)
            ) + f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE + url_of("pt", slug)}"/>'
            prio = "1.0" if slug == "" else ("0.3" if slug in ("termos", "privacidade") else "0.8")
            rows.append(f"  <url>\n    <loc>{BASE + url_of(lang, slug)}</loc>{alts}\n    <priority>{prio}</priority>\n  </url>")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n")


if __name__ == "__main__":
    main()
