/* pieseu - wspólny JS: zgoda cookies, FAQ, selektor wagi */
(function () {
  "use strict";

  /* ---------- FAQ accordion ---------- */
  document.querySelectorAll(".faq-q").forEach(function (q) {
    q.addEventListener("click", function () {
      var it = q.parentElement;
      var open = it.classList.contains("open");
      var scope = it.closest(".faq") || document;
      scope.querySelectorAll(".faq-item").forEach(function (x) { x.classList.remove("open"); });
      if (!open) it.classList.add("open");
    });
  });

  /* ---------- selektor wagi (dawkowanie) ---------- */
  var wsel = document.getElementById("wsel");
  if (wsel) {
    wsel.addEventListener("click", function (e) {
      var b = e.target.closest("button[data-tier]");
      if (!b) return;
      wsel.querySelectorAll("button").forEach(function (x) { x.classList.remove("on"); });
      b.classList.add("on");
    });
  }

  /* ---------- zgoda na cookies ---------- */
  var KEY = "pieseu_consent_v1";
  var ckb = document.getElementById("ckb");
  var modal = document.getElementById("ckModal");
  if (!ckb) return;

  function read() {
    try { return JSON.parse(localStorage.getItem(KEY)); } catch (e) { return null; }
  }
  function save(consent) {
    consent.ts = new Date().toISOString();
    try { localStorage.setItem(KEY, JSON.stringify(consent)); } catch (e) {}
    apply(consent);
    ckb.classList.remove("show");
    if (modal) modal.classList.remove("show");
  }
  function apply(c) {
    // Punkt podpięcia tagów: ładuj GA/Meta tylko po zgodzie.
    window.pieseuConsent = c;
    document.dispatchEvent(new CustomEvent("pieseu:consent", { detail: c }));
    if (c.analytics) { /* TODO: init analytyka (np. Google Analytics) */ }
    if (c.marketing) { /* TODO: init marketing (np. Meta Pixel, Google Ads) */ }
  }

  var stored = read();
  if (stored) {
    apply(stored);
  } else {
    setTimeout(function () { ckb.classList.add("show"); }, 600);
  }

  function bind(id, fn) { var el = document.getElementById(id); if (el) el.addEventListener("click", fn); }

  bind("ckbAccept", function () { save({ necessary: true, analytics: true, marketing: true }); });
  bind("ckbReject", function () { save({ necessary: true, analytics: false, marketing: false }); });
  bind("ckAcceptAll", function () { save({ necessary: true, analytics: true, marketing: true }); });
  bind("ckbSettings", function () { if (modal) modal.classList.add("show"); });
  bind("ckSave", function () {
    var a = document.getElementById("ckAnalytics");
    var m = document.getElementById("ckMarketing");
    save({ necessary: true, analytics: !!(a && a.checked), marketing: !!(m && m.checked) });
  });
  if (modal) {
    modal.addEventListener("click", function (e) { if (e.target === modal) modal.classList.remove("show"); });
  }

  // pre-fill przełączników stanem zapisanym
  if (stored) {
    var a = document.getElementById("ckAnalytics");
    var m = document.getElementById("ckMarketing");
    if (a) a.checked = !!stored.analytics;
    if (m) m.checked = !!stored.marketing;
  }

  // Globalny hak: ponowne otwarcie ustawień z dowolnego linku [data-cookie-settings]
  document.querySelectorAll("[data-cookie-settings]").forEach(function (el) {
    el.addEventListener("click", function (e) { e.preventDefault(); if (modal) modal.classList.add("show"); });
  });
})();
