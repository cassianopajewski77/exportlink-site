/* Export Link: Diagnóstico de prontidão exportadora.
   24 perguntas em 8 áreas. Sim = 2, Em parte = 1, Não = 0.
   Tudo roda no navegador; nada é enviado a servidor. O resultado vai para o WhatsApp só se a pessoa quiser. */
(function () {
  "use strict";

  var AREAS = [
    { id: "direcao", nome: "Direção", perguntas: [
      "A exportação faz parte do planejamento estratégico, com metas e orçamento próprios?",
      "A direção acompanha os resultados da exportação em reuniões periódicas?",
      "Existe uma pessoa ou um grupo com autoridade para reunir as áreas quando a exportação precisa?"
    ], dica: "Colocar a exportação no plano da empresa, com meta, orçamento e um grupo de todas as áreas que se reúne com frequência." },
    { id: "comercial", nome: "Comercial", perguntas: [
      "Sabemos quais países e clientes priorizar, com base em dados de mercado?",
      "Temos catálogo, ficha técnica e apresentação da empresa em espanhol ou inglês?",
      "Conseguimos responder uma cotação internacional em até 48 horas?"
    ], dica: "Escolher mercados com dados reais e preparar o material de venda no idioma do cliente, para responder rápido." },
    { id: "financeiro", nome: "Financeiro", perguntas: [
      "Temos o preço de exportação calculado por Incoterm, com os benefícios fiscais da exportação?",
      "Conhecemos as formas de pagamento internacional e o risco de cada uma?",
      "Sabemos fechar câmbio e receber do exterior com segurança?"
    ], dica: "Formar o preço por Incoterm sem os impostos que não incidem na exportação e definir formas de pagamento seguras." },
    { id: "producao", nome: "Produção", perguntas: [
      "A produção conhece os prazos prometidos ao cliente e planeja os pedidos de exportação?",
      "Temos capacidade para atender um pedido de exportação sem atrasar o mercado interno?",
      "Conseguimos garantir o mesmo padrão de qualidade em todos os lotes?"
    ], dica: "Incluir os pedidos de exportação no planejamento da fábrica, com prazo e padrão de qualidade combinados com o comercial." },
    { id: "engenharia", nome: "Engenharia", perguntas: [
      "Conhecemos as normas e certificações exigidas nos países que queremos atender?",
      "Conseguimos adaptar produto, embalagem e rotulagem quando o mercado pede?",
      "Acompanhamos o que os concorrentes internacionais oferecem?"
    ], dica: "Levantar as normas de cada mercado e ter um caminho rápido para adaptar produto, embalagem e rótulo." },
    { id: "suprimentos", nome: "Suprimentos", perguntas: [
      "Temos fornecedores confiáveis para garantir os materiais de um pedido maior ou urgente?",
      "Conhecemos o custo real dos insumos para formar um preço competitivo lá fora?",
      "Conhecemos o drawback e outros regimes que reduzem o custo dos insumos?"
    ], dica: "Garantir fornecedores para pedidos maiores e usar regimes como o drawback para baixar o custo." },
    { id: "logistica", nome: "Logística", perguntas: [
      "Sabemos emitir proforma, commercial invoice e packing list sem erro?",
      "Temos embalagem e paletização adequadas para o transporte internacional?",
      "Temos parceiros (agente de carga, despachante) para cotar frete e embarcar?"
    ], dica: "Padronizar os documentos de exportação e ter parceiros de frete e despacho já definidos." },
    { id: "pessoas", nome: "Pessoas (RH)", perguntas: [
      "Temos pessoas que falam espanhol ou inglês para atender clientes?",
      "A equipe já recebeu treinamento sobre exportação e o papel de cada área?",
      "Quando um pedido de exportação dá problema, as áreas resolvem juntas em vez de procurar culpados?"
    ], dica: "Treinar todas as áreas no processo de exportação, para que cada uma saiba o seu papel e trabalhe junto." }
  ];

  var OPCOES = [["Sim", 2], ["Em parte", 1], ["Não", 0]];
  var NIVEIS = [
    { min: 70, nome: "Pronta para crescer", texto: "A sua empresa já tem uma boa base. O próximo passo é transformar a exportação em um canal de venda permanente, com processo, método e metas claras." },
    { min: 40, nome: "Em preparação", texto: "Há pontos fortes, mas algumas áreas ainda não estão preparadas. É nelas que costumam aparecer atrasos, erros de preço e clientes perdidos." },
    { min: 0, nome: "Começando", texto: "A empresa ainda não tem a estrutura para exportar com segurança. Isso é comum e tem solução: preparar as áreas antes de buscar clientes evita prejuízo e desgaste." }
  ];

  var root = document.getElementById("dg-app");
  if (!root) return;
  var resp = {};
  var passo = 0;

  function el(tag, cls, txt) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (txt != null) e.textContent = txt;
    return e;
  }

  function notaArea(a) {
    var s = 0;
    a.perguntas.forEach(function (_, i) { s += resp[a.id + i] || 0; });
    return Math.round((s / (a.perguntas.length * 2)) * 100);
  }

  function completa(a) {
    return a.perguntas.every(function (_, i) { return resp.hasOwnProperty(a.id + i); });
  }

  function renderPasso() {
    var a = AREAS[passo];
    root.innerHTML = "";

    var prog = el("div", "dg-progress");
    prog.setAttribute("role", "progressbar");
    prog.setAttribute("aria-valuemin", "0");
    prog.setAttribute("aria-valuemax", String(AREAS.length));
    prog.setAttribute("aria-valuenow", String(passo + 1));
    prog.setAttribute("aria-label", "Etapa " + (passo + 1) + " de " + AREAS.length);
    var bar = el("span");
    bar.style.width = ((passo + 1) / AREAS.length) * 100 + "%";
    prog.appendChild(bar);

    var head = el("div", "dg-step-head");
    head.appendChild(el("p", "dg-count", "Área " + (passo + 1) + " de " + AREAS.length));
    var h = el("h2", null, a.nome);
    h.tabIndex = -1;
    head.appendChild(h);

    root.appendChild(prog);
    root.appendChild(head);

    a.perguntas.forEach(function (q, i) {
      var key = a.id + i;
      var fs = el("fieldset", "dg-q");
      fs.appendChild(el("legend", null, q));
      var opts = el("div", "dg-opts");
      OPCOES.forEach(function (o) {
        var lab = el("label", "dg-opt");
        var inp = document.createElement("input");
        inp.type = "radio";
        inp.name = key;
        inp.value = o[1];
        if (resp[key] === o[1]) inp.checked = true;
        inp.addEventListener("change", function () {
          resp[key] = o[1];
          next.disabled = !completa(a);
        });
        lab.appendChild(inp);
        lab.appendChild(el("span", null, o[0]));
        opts.appendChild(lab);
      });
      fs.appendChild(opts);
      root.appendChild(fs);
    });

    var nav = el("div", "dg-nav");
    var back = el("button", "btn btn--ghost", "Voltar");
    back.type = "button";
    back.hidden = passo === 0;
    back.addEventListener("click", function () { passo--; renderPasso(); foco(); });
    var next = el("button", "btn btn--primary", passo === AREAS.length - 1 ? "Ver meu resultado" : "Próxima área");
    next.type = "button";
    next.disabled = !completa(a);
    next.addEventListener("click", function () {
      if (passo < AREAS.length - 1) { passo++; renderPasso(); } else { renderResultado(); }
      foco();
    });
    nav.appendChild(back);
    nav.appendChild(next);
    root.appendChild(nav);
  }

  function foco() {
    var top = document.getElementById("diagnostico");
    if (top) top.scrollIntoView({ behavior: "smooth", block: "start" });
    var h = root.querySelector("h2");
    if (h) h.focus({ preventScroll: true });
  }

  function renderResultado() {
    var notas = AREAS.map(function (a) { return { a: a, n: notaArea(a) }; });
    var total = Math.round(notas.reduce(function (s, x) { return s + x.n; }, 0) / notas.length);
    var nivel = NIVEIS.filter(function (n) { return total >= n.min; })[0];
    var fracas = notas.slice().sort(function (x, y) { return x.n - y.n; }).filter(function (x) { return x.n < 100; }).slice(0, 3);

    root.innerHTML = "";
    var res = el("div", "dg-result");

    var top = el("div", "dg-score");
    var ring = el("div", "dg-ring");
    ring.style.setProperty("--p", total);
    ring.appendChild(el("strong", null, total + "%"));
    ring.setAttribute("role", "img");
    ring.setAttribute("aria-label", "Nota geral: " + total + " por cento");
    var txt = el("div", "dg-score__text");
    txt.appendChild(el("p", "dg-count", "Seu resultado"));
    var h = el("h2", null, nivel.nome);
    h.tabIndex = -1;
    txt.appendChild(h);
    txt.appendChild(el("p", null, nivel.texto));
    top.appendChild(ring);
    top.appendChild(txt);
    res.appendChild(top);

    res.appendChild(el("h3", null, "Prontidão por área"));
    var list = el("ul", "dg-bars");
    notas.forEach(function (x) {
      var li = el("li");
      var cls = x.n >= 70 ? "is-ok" : x.n >= 40 ? "is-mid" : "is-low";
      li.className = cls;
      li.appendChild(el("span", "dg-bars__name", x.a.nome));
      var b = el("span", "dg-bars__track");
      var f = el("span");
      f.style.width = Math.max(x.n, 2) + "%";
      b.appendChild(f);
      li.appendChild(b);
      li.appendChild(el("span", "dg-bars__val", x.n + "%"));
      list.appendChild(li);
    });
    res.appendChild(list);

    if (fracas.length) {
      res.appendChild(el("h3", null, "Por onde começar"));
      var ol = el("ol", "dg-tips");
      fracas.forEach(function (x) {
        var li = el("li");
        li.appendChild(el("strong", null, x.a.nome + " (" + x.n + "%)"));
        li.appendChild(el("span", null, x.a.dica));
        ol.appendChild(li);
      });
      res.appendChild(ol);
    }

    var cta = el("div", "dg-cta");
    cta.appendChild(el("h3", null, "Receba a análise completa"));
    cta.appendChild(el("p", null, "Mande o seu resultado para a Export Link pelo WhatsApp. Conversamos sobre os pontos fracos da sua empresa e o que fazer primeiro, sem compromisso."));
    var form = el("form", "dg-form");
    form.innerHTML =
      '<label><span>Seu nome</span><input name="nome" autocomplete="name" required></label>' +
      '<label><span>Empresa</span><input name="empresa" autocomplete="organization" required></label>';
    var send = el("button", "btn btn--wa", "Enviar resultado pelo WhatsApp");
    send.type = "submit";
    form.appendChild(send);
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var cfg = window.EXPORTLINK_CONFIG || {};
      var phone = cfg.whatsapp || "5541992640066";
      var msg = "Olá! Fiz o Diagnóstico de Prontidão Exportadora no site da Export Link.\n" +
        "Nome: " + form.nome.value.trim() + "\nEmpresa: " + form.empresa.value.trim() + "\n\n" +
        "Nota geral: " + total + "% (" + nivel.nome + ")\n" +
        notas.map(function (x) { return "• " + x.a.nome + ": " + x.n + "%"; }).join("\n") +
        "\n\nQuero receber a análise completa.";
      window.open("https://wa.me/" + phone + "?text=" + encodeURIComponent(msg), "_blank", "noopener");
    });
    cta.appendChild(form);
    res.appendChild(cta);

    var redo = el("button", "btn btn--ghost dg-redo", "Refazer o diagnóstico");
    redo.type = "button";
    redo.addEventListener("click", function () { resp = {}; passo = 0; renderPasso(); foco(); });
    res.appendChild(redo);

    root.appendChild(res);
  }

  var start = document.getElementById("dg-start");
  if (start) {
    start.addEventListener("click", function () {
      root.hidden = false;
      document.getElementById("dg-intro").hidden = true;
      renderPasso();
      foco();
    });
  } else {
    renderPasso();
  }
})();
