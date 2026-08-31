#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the VA backlink task page. Never hand-edit the html — edit articles.py.

    python3 build.py > ../docs/backlinks/index.html

The page is written for someone following instructions in a second language, at speed,
without being asked to judge anything. Every decision is already made here; her job is
copy, paste, link, publish.
"""
import html, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from articles import ARTICLES, PUBLISH_ORDER, BASE

BY = {a[0]: a for a in ARTICLES}

# ── assertions. A batch that is four posts on one platform, or two posts pointing at the
# same page, is a footprint. Assert it here rather than hope.
order = [BY[k] for k in PUBLISH_ORDER]
assert len(order) == len(ARTICLES) == 8, "expected 8 articles"
assert len({a[3] for a in order}) == 8, "a target page is used twice"
for i in range(len(order) - 3):
    window = [a[1] for a in order[i:i + 4]]
    assert len(set(window)) > 1, "four consecutive posts on one platform at %d" % i
for k, plat, lang, target, anchor, title, paras in order:
    body = "\n\n".join(paras)
    assert "ANCHOR" in body, "%s has no link slot" % k
    assert body.count("ANCHOR") == 1, "%s has more than one link" % k
    for bad in ("**", "##", "](", "* ", "#"):
        assert bad not in body.replace("# ", ""), "%s contains markdown %r" % (k, bad)
    w = len(body.split())
    assert 350 <= w <= 640, "%s is %d words, want 350-640" % (k, w)

E = html.escape

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{font:17px/1.65 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;
 color:#1c2024;background:#f4f5f7;padding:0 0 80px}
.wrap{max-width:940px;margin:0 auto;padding:0 20px}
header{background:#0A4F44;color:#fff;padding:34px 0 30px;margin-bottom:28px}
header h1{font-size:27px;line-height:1.25;margin-bottom:8px}
header p{opacity:.92;font-size:16px;max-width:70ch}
.big{background:#fff;border:2px solid #0A4F44;border-radius:10px;padding:22px;margin:0 0 26px}
.big h2{font-size:20px;margin-bottom:10px;color:#0A4F44}
.big ol{margin:12px 0 0 22px}.big ol li{margin-bottom:9px}
.big ul{margin:10px 0 0 22px}.big ul li{margin-bottom:7px}
.warn{background:#FFF4E5;border:2px solid #E9A020;border-radius:10px;padding:20px;margin:0 0 26px}
.warn h2{font-size:19px;margin-bottom:8px;color:#8A5700}
kbd{background:#1c2024;color:#fff;border-radius:4px;padding:2px 8px;font-size:14px;
 font-family:ui-monospace,Menlo,Consolas,monospace}
.card{background:#fff;border:1px solid #d8dbe0;border-radius:10px;padding:22px;margin-bottom:20px}
.card.done{opacity:.5;border-color:#00C249}
.top{display:flex;align-items:flex-start;gap:14px;margin-bottom:14px;flex-wrap:wrap}
.num{background:#0A4F44;color:#fff;width:38px;height:38px;border-radius:50%;
 display:flex;align-items:center;justify-content:center;font-weight:700;flex:0 0 38px}
.who{flex:1;min-width:220px}
.who b{display:block;font-size:18px;line-height:1.3}
.tag{display:inline-block;background:#eef0f3;border-radius:20px;padding:3px 12px;
 font-size:13px;font-weight:700;margin-top:5px}
.tag.gs{background:#E3F0FF;color:#0B4A8F}.tag.tb{background:#EDE6F7;color:#4B2B7F}
.row{display:flex;align-items:center;gap:10px;padding:11px 0;border-top:1px solid #eceef1;
 flex-wrap:wrap}
.row .lab{flex:0 0 132px;font-weight:700;font-size:14px}
.row .val{flex:1;min-width:200px;font-family:ui-monospace,Menlo,Consolas,monospace;
 font-size:14px;word-break:break-all;color:#3a4148}
button{font:inherit;font-size:14px;font-weight:700;border:0;border-radius:7px;
 padding:11px 17px;cursor:pointer;background:#0A4F44;color:#fff;min-height:44px}
button:hover{background:#0C5F52}
button.sec{background:#eef0f3;color:#1c2024}
button.ok{background:#00C249;color:#04231E}
.fin{display:flex;align-items:center;gap:12px;margin-top:16px;padding-top:16px;
 border-top:2px solid #eceef1;flex-wrap:wrap}
.fin label{display:flex;align-items:center;gap:9px;font-weight:700;cursor:pointer;
 min-height:44px}
.fin input{width:22px;height:22px}
.prog{position:sticky;top:0;background:#fff;border-bottom:2px solid #0A4F44;padding:13px 0;
 z-index:9;margin-bottom:22px;font-weight:700}
details{margin-top:12px}
summary{cursor:pointer;font-weight:700;color:#0A4F44;padding:9px 0;min-height:44px;
 display:flex;align-items:center}
pre{white-space:pre-wrap;background:#f7f8f9;border:1px solid #e3e6ea;border-radius:7px;
 padding:15px;margin-top:10px;font:15px/1.6 inherit;color:#22282e}
.hint{font-size:15px;color:#5b636c;margin-top:5px}
@media(max-width:620px){.row .lab{flex:0 0 100%}.row .val{flex:0 0 100%}}
"""

JS = """
const K='wellaray-bl-v1';
const st=JSON.parse(localStorage.getItem(K)||'{}');
function paint(){
  let n=0;
  document.querySelectorAll('.card').forEach(c=>{
    const id=c.dataset.id, on=!!st[id];
    c.classList.toggle('done',on);
    const b=c.querySelector('.fin input'); if(b) b.checked=on;
    if(on) n++;
  });
  document.getElementById('prog').textContent =
    n+' of '+document.querySelectorAll('.card').length+' articles finished';
}
function copy(t,btn){
  const done=()=>{const o=btn.textContent;btn.textContent='Copied';btn.classList.add('ok');
    setTimeout(()=>{btn.textContent=o;btn.classList.remove('ok')},1400)};
  const ta=document.createElement('textarea');
  ta.value=t; ta.style.position='fixed'; ta.style.opacity='0';
  document.body.appendChild(ta); ta.select();
  let ok=false; try{ok=document.execCommand('copy')}catch(e){}
  document.body.removeChild(ta);
  if(ok){done();return}
  if(navigator.clipboard) navigator.clipboard.writeText(t).then(done).catch(()=>{});
}
document.addEventListener('click',e=>{
  const b=e.target.closest('button[data-copy]');
  if(b) copy(document.getElementById(b.dataset.copy).textContent,b);
});
document.addEventListener('change',e=>{
  const i=e.target.closest('.fin input');
  if(!i) return;
  const id=i.closest('.card').dataset.id;
  if(i.checked) st[id]=1; else delete st[id];
  localStorage.setItem(K,JSON.stringify(st)); paint();
});
paint();
"""


def card(i, a):
    k, plat, lang, target, anchor, title, paras = a
    url = BASE + target
    body = "\n\n".join(paras).replace("ANCHOR", anchor)
    cls = "gs" if plat == "Google Sites" else "tb"
    lg = "German" if lang == "de" else "English"
    return f"""
<article class="card" data-id="{E(k)}">
  <div class="top">
    <div class="num">{i}</div>
    <div class="who">
      <b>{E(title)}</b>
      <span class="tag {cls}">{E(plat)}</span>
      <span class="tag">{lg}</span>
    </div>
  </div>

  <div class="row">
    <span class="lab">1. Title</span>
    <span class="val" id="t{i}">{E(title)}</span>
    <button data-copy="t{i}">Copy title</button>
  </div>

  <div class="row">
    <span class="lab">2. Article</span>
    <span class="val">{len(body.split())} words &middot; plain text, no symbols</span>
    <button data-copy="b{i}">Copy article</button>
  </div>

  <div class="row">
    <span class="lab">3. These words</span>
    <span class="val">{E(anchor)}</span>
    <button data-copy="a{i}">Copy words</button>
  </div>

  <div class="row">
    <span class="lab">4. This address</span>
    <span class="val">{E(url)}</span>
    <button data-copy="u{i}">Copy address</button>
  </div>

  <details>
    <summary>Show me the article</summary>
    <pre id="b{i}">{E(body)}</pre>
  </details>
  <span style="display:none" id="a{i}">{E(anchor)}</span>
  <span style="display:none" id="u{i}">{E(url)}</span>

  <div class="fin">
    <label><input type="checkbox"> I published this one and the link is blue</label>
  </div>
</article>"""


def main():
    cards = "".join(card(i, a) for i, a in enumerate(order, 1))
    gs = sum(1 for a in order if a[1] == "Google Sites")
    tb = len(order) - gs
    print(f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Wellaray — backlink tasks</title>
<style>{CSS}</style>
</head><body>

<header><div class="wrap">
  <h1>Wellaray — backlink tasks</h1>
  <p>{len(order)} articles. {gs} go on Google Sites, {tb} go on Tumblr.
     Do one card at a time. Finish it completely, then start the next one.</p>
</div></header>

<div class="wrap">

<div class="prog" id="prog">0 of {len(order)} articles finished</div>

<div class="big">
  <h2>What to do, for every card</h2>
  <ol>
    <li>Look at the card. It says <b>Google Sites</b> or <b>Tumblr</b>. Use that one.</li>
    <li>Make a new page there.</li>
    <li>Press <b>Copy title</b>. Paste it as the page title.</li>
    <li>Press <b>Copy article</b>. Paste it as the page text.</li>
    <li><b>Make the link.</b> The 4 steps are in the orange box below. This part matters most.</li>
    <li>Press <b>Publish</b>.</li>
    <li>Open the published page yourself. Check the link is blue and it opens wellaray.shop.</li>
    <li>Tick the box at the bottom of the card.</li>
  </ol>
</div>

<div class="warn">
  <h2>The link. Please read this part twice.</h2>
  <p>A link you cannot click is worth nothing to us. Do these 4 steps every time:</p>
  <ol>
    <li>In the article you just pasted, find the words from <b>Copy words</b>.</li>
    <li>Select those words with your mouse.</li>
    <li>Press <kbd>Ctrl</kbd> + <kbd>K</kbd>.</li>
    <li>Paste the address from <b>Copy address</b>. Press <kbd>Enter</kbd>.</li>
  </ol>
  <p style="margin-top:12px"><b>Then check it:</b></p>
  <ul>
    <li>The words must be <b>blue</b>.</li>
    <li>Click them. They must open <b>wellaray.shop</b>.</li>
    <li>If they are still black, the link did not save. Do the 4 steps again.</li>
  </ul>
  <p style="margin-top:12px">Each article gets <b>one link only</b>. Do not add more.</p>
</div>

<div class="big">
  <h2>Two things to avoid</h2>
  <ul>
    <li>Do not publish two articles on the same day from the same account if you can help
        it. Spread them out.</li>
    <li>Do not change the words in the article. They are written for search.</li>
    <li>If you see a <b>#</b> or a <b>*</b> on your published page, the text went in wrong.
        Delete it, press <b>Copy article</b> again, and paste it again.</li>
  </ul>
</div>

{cards}

<p style="margin-top:30px;color:#5b636c;font-size:15px">
  Your ticks are saved in this browser. You can close the page and come back.
</p>

</div>
<script>{JS}</script>
</body></html>""")


if __name__ == "__main__":
    main()
