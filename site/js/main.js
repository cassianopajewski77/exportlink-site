/* Export Link Global Solutions: script único do site. */
(function () {
  "use strict";
  var cfg = window.EXPORTLINK_CONFIG || {};

  // Menu do celular
  var toggle = document.querySelector(".menu-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    var mq = window.matchMedia("(max-width: 760px)");
    var sync = function () { nav.hidden = mq.matches; toggle.setAttribute("aria-expanded", "false"); };
    sync();
    if (mq.addEventListener) mq.addEventListener("change", sync);
    toggle.addEventListener("click", function () {
      var open = nav.hidden;
      nav.hidden = !open;
      toggle.setAttribute("aria-expanded", String(open));
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && mq.matches && !nav.hidden) { nav.hidden = true; toggle.setAttribute("aria-expanded", "false"); toggle.focus(); }
    });
  }

  // Redes sociais: o ícone só aparece quando o link estiver preenchido em js/config.js
  document.querySelectorAll("[data-social]").forEach(function (a) {
    var url = cfg[a.getAttribute("data-social")];
    if (url) { a.href = url; a.hidden = false; }
  });

  // Links de WhatsApp com mensagem pronta: data-wa="texto"
  var phone = cfg.whatsapp || "5541992640066";
  document.querySelectorAll("[data-wa]").forEach(function (a) {
    var msg = a.getAttribute("data-wa");
    a.href = "https://wa.me/" + phone + (msg ? "?text=" + encodeURIComponent(msg) : "");
  });

  // Botões de copiar e-mail / telefone
  document.querySelectorAll("[data-copy]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var text = btn.getAttribute("data-copy");
      var label = btn.textContent;
      var done = function () { btn.textContent = btn.getAttribute("data-copied") || "Copiado"; setTimeout(function () { btn.textContent = label; }, 1800); };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, function () { selectNear(btn); });
      } else { selectNear(btn); }
    });
  });
  function selectNear(btn) {
    var target = btn.previousElementSibling;
    if (!target) return;
    var r = document.createRange(); r.selectNodeContents(target);
    var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
  }

  // Formulário de contato: o site no Cloudflare não recebe formulários, então abre o WhatsApp com a mensagem pronta
  var form = document.querySelector("form[data-whatsapp]");
  if (form) {
    var pre = new URLSearchParams(location.search).get("interesse");
    var radio = pre && document.getElementById("i-" + pre);
    if (radio) radio.checked = true;
    var status = form.querySelector(".form-status");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var d = new FormData(form);
      if (d.get("bot-field")) return;
      var v = function (k) { return (d.get(k) || "").toString().trim(); };
      var msg = "Olá! Vim pelo site da Export Link (" + v("idioma") + ").\n\n" +
        "Nome: " + v("nome") + "\nEmpresa: " + v("empresa") + "\nE-mail: " + v("email") +
        (v("whatsapp") ? "\nWhatsApp: " + v("whatsapp") : "") + "\nInteresse: " + v("interesse") +
        "\n\n" + v("mensagem");
      var num = (window.EXPORTLINK_CONFIG && window.EXPORTLINK_CONFIG.whatsapp) || "5541992640066";
      var url = "https://wa.me/" + num + "?text=" + encodeURIComponent(msg);
      if (!window.open(url, "_blank", "noopener")) location.href = url;
      status.hidden = false;
      status.className = "form-status form-status--ok";
      status.textContent = form.getAttribute("data-ok");
      status.setAttribute("tabindex", "-1");
      status.focus();
    });
  }

  // Carrossel do topo: troca a cada 8 s, pausa com mouse ou foco, para de vez quando a pessoa usa os controles
  var car = document.querySelector(".carousel");
  if (car) {
    var slides = car.querySelectorAll(".slide");
    var dots = car.querySelectorAll("[data-go]");
    var pauseBtn = car.querySelector("[data-pause]");
    var current = 0, timer = null, stopped = false, hold = false;
    var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var show = function (i) {
      current = (i + slides.length) % slides.length;
      slides.forEach(function (s, k) {
        var on = k === current;
        s.classList.toggle("is-active", on);
        if (on) { s.removeAttribute("inert"); s.removeAttribute("aria-hidden"); }
        else { s.setAttribute("inert", ""); s.setAttribute("aria-hidden", "true"); }
      });
      dots.forEach(function (d, k) { if (k === current) d.setAttribute("aria-current", "true"); else d.removeAttribute("aria-current"); });
    };
    var tick = function () { if (!stopped && !hold) show(current + 1); };
    var start = function () { if (!reduce && !timer) timer = setInterval(tick, 8000); };
    var stop = function () {
      stopped = true; clearInterval(timer); timer = null;
      if (pauseBtn) { pauseBtn.classList.add("is-paused"); pauseBtn.setAttribute("aria-label", pauseBtn.getAttribute("data-label-play")); }
    };
    car.querySelector("[data-prev]").addEventListener("click", function () { stop(); show(current - 1); });
    car.querySelector("[data-next]").addEventListener("click", function () { stop(); show(current + 1); });
    dots.forEach(function (d) { d.addEventListener("click", function () { stop(); show(+d.getAttribute("data-go") - 1); }); });
    if (pauseBtn) pauseBtn.addEventListener("click", function () {
      if (stopped) {
        stopped = false; pauseBtn.classList.remove("is-paused");
        pauseBtn.setAttribute("aria-label", pauseBtn.getAttribute("data-label-pause")); start();
      } else stop();
    });
    car.addEventListener("mouseenter", function () { hold = true; });
    car.addEventListener("mouseleave", function () { hold = false; });
    car.addEventListener("focusin", function () { hold = true; });
    car.addEventListener("focusout", function () { hold = false; });
    var x0 = null;
    car.addEventListener("touchstart", function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    car.addEventListener("touchend", function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0; x0 = null;
      if (Math.abs(dx) > 50) { stop(); show(current + (dx < 0 ? 1 : -1)); }
    });
    start();
  }

  // Ano no rodapé
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
