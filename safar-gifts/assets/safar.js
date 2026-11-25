(function(){
  var CAT = window.CAT, T = window.T, LANG = window.LANG;
  var KEY = 'safar-cart-v1', mem = [];
  function load(){ try { var v = JSON.parse(localStorage.getItem(KEY) || '[]'); return Array.isArray(v) ? v : []; } catch(e){ return mem; } }
  function save(c){ mem = c; try { localStorage.setItem(KEY, JSON.stringify(c)); } catch(e){} count(); }
  function prod(id){ for (var i = 0; i < CAT.products.length; i++) if (CAT.products[i].id === id) return CAT.products[i]; return null; }
  function money(n){ return CAT.currency + ' ' + (Math.round(n * 100) / 100).toLocaleString('en-US', {minimumFractionDigits: n % 1 ? 2 : 0, maximumFractionDigits: 2}); }
  function unitPrice(it){ var p = prod(it.id); return (p ? p.price : 0) + (it.sticker ? CAT.stickerPerUnit : 0); }
  function count(){ var n = load().reduce(function(s, i){ return s + i.units; }, 0); document.querySelectorAll('[data-count]').forEach(function(el){ el.textContent = n; el.style.display = n ? 'flex' : 'none'; }); }
  function toast(msg){ var t = document.querySelector('.toast'); if (!t) return; t.textContent = msg; t.style.display = 'block'; clearTimeout(toast.h); toast.h = setTimeout(function(){ t.style.display = 'none'; }, 2200); }
  function add(item){ var c = load(); c.push(item); save(c); toast(T.added); }
  function waLink(text){ return 'https://wa.me/?text=' + encodeURIComponent(text); }
  function showWA(box, text){ box.textContent = text; box.style.display = 'block'; var a = box.nextElementSibling; if (a && a.tagName === 'A') { a.href = waLink(text); a.style.display = 'inline-flex'; } }
  window.SAFAR = {money: money};

  // ---- product page ----
  var pd = document.querySelector('[data-product]');
  if (pd) {
    var p = prod(pd.getAttribute('data-product'));
    var packs = pd.querySelector('[name=packs]'), custom = pd.querySelector('[name=custom]');
    function units(){ var m = (pd.querySelector('[name=mode]:checked') || {}).value; if (m === 'custom') return Math.max(CAT.customRange[0], Math.min(CAT.customRange[1], parseInt(custom.value || 0, 10) || 0)); return parseInt(m, 10) * Math.max(1, parseInt(packs.value || 1, 10)); }
    function sticker(){ return pd.querySelector('[name=sticker]').checked; }
    function calc(){
      var m = (pd.querySelector('[name=mode]:checked') || {}).value;
      pd.querySelector('[data-packs-row]').style.display = m === 'custom' ? 'none' : 'flex';
      pd.querySelector('[data-custom-row]').style.display = m === 'custom' ? 'flex' : 'none';
      pd.querySelector('[data-sticker-row]').style.display = sticker() ? 'flex' : 'none';
      var u = units(), each = p.price + (sticker() ? CAT.stickerPerUnit : 0);
      pd.querySelector('[data-units]').textContent = u;
      pd.querySelector('[data-total]').textContent = money(u * each);
      var kg = u * p.weightG / 1000, l = u * p.size[0] * p.size[1] * p.size[2] / 1000;
      pd.querySelector('[data-weight]').textContent = kg.toFixed(1) + ' kg';
      pd.querySelector('[data-volume]').textContent = l.toFixed(1) + ' L';
    }
    pd.addEventListener('input', calc); pd.addEventListener('change', calc);
    pd.querySelectorAll('[data-step]').forEach(function(b){ b.addEventListener('click', function(){ packs.value = Math.max(1, (parseInt(packs.value, 10) || 1) + parseInt(b.getAttribute('data-step'), 10)); calc(); }); });
    pd.querySelectorAll('.thumbs button').forEach(function(b){ b.addEventListener('click', function(){ pd.querySelector('.gallery .main img').src = b.querySelector('img').src; pd.querySelectorAll('.thumbs button').forEach(function(x){ x.classList.remove('on'); }); b.classList.add('on'); }); });
    function item(){ return {id: p.id, units: units(), sticker: sticker(), stickerText: sticker() ? pd.querySelector('[name=stickerText]').value : '', note: ''}; }
    pd.querySelector('[data-add]').addEventListener('click', function(){ add(item()); });
    pd.querySelector('[data-wa]').addEventListener('click', function(){ var it = item(); showWA(pd.querySelector('.wa-preview'), T.waHello + '\n\n' + lineText(it) + '\n' + T.total + ': ' + money(it.units * unitPrice(it))); });
    calc();
  }
  function lineText(it){ var p = prod(it.id); return '- ' + p.name[LANG] + ' (' + CAT.currency + ' ' + p.price + ') x ' + it.units + (it.sticker ? ' + ' + T.sticker + (it.stickerText ? ': "' + it.stickerText + '"' : '') : '') + (it.note ? ' [' + it.note + ']' : ''); }

  // ---- shop filters ----
  var sf = document.querySelector('[data-filters]');
  if (sf) {
    function apply(){
      var prices = [].map.call(sf.querySelectorAll('[name=price]:checked'), function(x){ return x.value; });
      var items = [].map.call(sf.querySelectorAll('[name=item]:checked'), function(x){ return x.value; });
      var shown = 0;
      document.querySelectorAll('[data-card]').forEach(function(c){
        var ok = (!prices.length || prices.indexOf(c.getAttribute('data-price')) > -1) && items.every(function(i){ return c.getAttribute('data-items').split(' ').indexOf(i) > -1; });
        c.style.display = ok ? '' : 'none'; if (ok) shown++;
      });
      document.querySelector('[data-shown]').textContent = shown;
      var q = (sf.querySelector('[name=qty]:checked') || {}).value || '10';
      document.querySelectorAll('[data-packprice]').forEach(function(el){ el.textContent = money(parseFloat(el.getAttribute('data-packprice')) * parseInt(q, 10)); });
      document.querySelectorAll('[data-qtylabel]').forEach(function(el){ el.textContent = q; });
    }
    sf.addEventListener('change', apply); apply();
  }

  // ---- build your pack ----
  var bp = document.querySelector('[data-build]');
  if (bp) {
    function rec(){
      var budget = parseFloat(bp.querySelector('[name=budget]').value), sel = [].map.call(bp.querySelectorAll('[name=bitem]:checked'), function(x){ return x.value; });
      var fits = CAT.products.filter(function(p){ return sel.every(function(s){ return p.items.indexOf(s) > -1; }); }).sort(function(a, b){ return a.price - b.price; });
      var best = fits.filter(function(p){ return p.price <= budget; }).pop() || null;
      var cheapest = fits[0] || null;
      return {best: best, cheapest: cheapest};
    }
    function out(){
      var r = rec(), n = Math.max(1, parseInt(bp.querySelector('[name=recipients]').value || 0, 10) || 1), st = bp.querySelector('[name=bsticker]').checked;
      var box = bp.querySelector('[data-result]');
      if (!r.best) { box.innerHTML = '<p class="note">' + T.overBudget.replace('{p}', r.cheapest ? money(r.cheapest.price) : '') + '</p>'; bp.querySelector('[data-badd]').disabled = true; return; }
      var each = r.best.price + (st ? CAT.stickerPerUnit : 0);
      box.innerHTML = '<div class="row" style="gap:16px;align-items:center;flex-wrap:nowrap"><img src="' + window.ASSETS + r.best.img + '" alt="" style="width:120px;height:90px;object-fit:cover;border-radius:12px"><div><span class="eyebrow">' + T.recommended + '</span><h3 style="font-size:20px">' + r.best.name[LANG] + '</h3><p class="muted">' + r.best.contents[LANG].join(' · ') + '</p></div></div>' +
        '<div class="total"><div><small>' + n + ' x ' + money(each) + '</small>' + T.total + '</div><b>' + money(n * each) + '</b></div>';
      bp.querySelector('[data-badd]').disabled = false;
      bp._item = {id: r.best.id, units: n, sticker: st, stickerText: st ? bp.querySelector('[name=bstickerText]').value : '', note: T.colour + ': ' + bp.querySelector('[name=colour]:checked').parentNode.textContent.trim() + ', ' + bp.querySelector('[name=location]').selectedOptions[0].textContent};
    }
    bp.addEventListener('input', out); bp.addEventListener('change', out);
    bp.querySelector('[data-badd]').addEventListener('click', function(){ if (bp._item) add(bp._item); });
    out();
  }

  // ---- cart ----
  var cp = document.querySelector('[data-cart]');
  if (cp) {
    function render(){
      var c = load(), list = cp.querySelector('[data-lines]'), sub = 0;
      if (!c.length) { list.innerHTML = '<div class="empty"><p>' + T.empty + '</p><p style="margin-top:12px"><a class="btn btn-em" href="' + window.SHOP + '">' + T.shop + '</a></p></div>'; }
      else list.innerHTML = c.map(function(it, i){ var p = prod(it.id), lt = it.units * unitPrice(it); sub += lt;
        return '<div class="line"><img src="' + window.ASSETS + p.img + '" alt=""><div><b>' + p.name[LANG] + '</b><div class="muted" style="font-size:13px">' + money(unitPrice(it)) + ' x ' + it.units + (it.sticker ? ' · ' + T.sticker : '') + (it.note ? ' · ' + it.note : '') + '</div>' +
        '<div class="row" style="margin-top:6px;gap:8px"><div class="stepper"><button type="button" data-q="' + i + '" data-d="-10" aria-label="-10">−</button><input aria-label="' + T.units + '" value="' + it.units + '" readonly><button type="button" data-q="' + i + '" data-d="10" aria-label="+10">+</button></div><button type="button" class="rm" data-rm="' + i + '">' + T.remove + '</button></div></div><b>' + money(lt) + '</b></div>'; }).join('');
      cp.querySelector('[data-sub]').textContent = money(sub);
      cp.querySelector('[data-grand]').textContent = money(sub);
      cp.querySelector('[data-checkout]').disabled = !c.length;
      return sub;
    }
    cp.addEventListener('click', function(e){
      var t = e.target.closest('button'); if (!t) return; var c = load();
      if (t.hasAttribute('data-rm')) { c.splice(+t.getAttribute('data-rm'), 1); save(c); render(); }
      if (t.hasAttribute('data-q')) { var it = c[+t.getAttribute('data-q')]; it.units = Math.max(10, it.units + parseInt(t.getAttribute('data-d'), 10)); save(c); render(); }
    });
    cp.querySelector('[data-checkout]').addEventListener('click', function(){
      var f = cp.querySelector('form'); if (!f.reportValidity()) return;
      var c = load(), sub = c.reduce(function(s, it){ return s + it.units * unitPrice(it); }, 0);
      var txt = T.waHello + '\n\n' + c.map(lineText).join('\n') + '\n\n' + T.total + ': ' + money(sub) + '\n' + T.delivery + ': ' + f.delivery.selectedOptions[0].textContent + (f.place.value ? ' (' + f.place.value + ')' : '') + '\n' + T.date + ': ' + (f.date.value || '-') + '\n' + T.name + ': ' + f.name.value + '\n' + T.phone + ': ' + f.phone.value;
      showWA(cp.querySelector('.wa-preview'), txt);
    });
    render();
  }

  // ---- bulk enquiry ----
  var bk = document.querySelector('[data-bulk]');
  if (bk) bk.querySelector('[data-bwa]').addEventListener('click', function(){
    var f = bk; if (!f.reportValidity()) return;
    var txt = T.bulkHello + '\n\n' + T.org + ': ' + f.org.value + '\n' + T.name + ': ' + f.name.value + '\n' + T.phone + ': ' + f.phone.value + '\n' + T.units + ': ' + f.units.value + '\n' + T.tier + ': ' + f.tier.selectedOptions[0].textContent + '\n' + T.branding + ': ' + (f.branding.checked ? T.yes : T.no) + '\n' + T.date + ': ' + (f.date.value || '-') + '\n' + (f.msg.value || '');
    showWA(bk.querySelector('.wa-preview'), txt);
  });
  count();
})();
