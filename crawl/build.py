#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the VA crawl-request page from to_index.json.

    python3 build.py > ../docs/index.html

⚠ This exists because the page was previously updated by regex-swapping rows inside the
built HTML. Each row is `<li><div class="row">label + button</div></li>`; the swap matched
only `label ... button`, so eighteen rows were concatenated into ONE row container and the
whole page collapsed into one letter per line. Generate the page, never patch it.
"""
import html, json, os, sys, collections

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/root/workspace/wellaray")
from manifest import all_pages, GEOS

E = html.escape
META = {"https://wellaray.shop" + p["url"]: (p["owned"], p["volume"], p["geo"])
        for p in all_pages()}
GEO_TITLE = {"de": ("Deutschland", "de-DE · AT · CH"),
             "uk": ("United Kingdom", "en-GB"),
             "en": ("US · Canada · Australia · New Zealand", "en-US")}

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{font:17px/1.6 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;
 color:#1c2024;background:#f4f5f7;padding:0 0 80px}
.wrap{max-width:960px;margin:0 auto;padding:0 20px}
header{background:#0A4F44;color:#fff;padding:34px 0 30px;margin-bottom:26px}
header h1{font-size:27px;line-height:1.25;margin-bottom:8px}
header p{opacity:.92;font-size:16px;max-width:72ch}
.big{background:#fff;border:2px solid #0A4F44;border-radius:10px;padding:22px;margin:0 0 24px}
.big h2{font-size:20px;margin-bottom:10px;color:#0A4F44}
.big ol,.big ul{margin:12px 0 0 22px}.big li{margin-bottom:9px}
.prog{position:sticky;top:0;background:#fff;border-bottom:2px solid #0A4F44;
 padding:13px 0;z-index:9;margin-bottom:22px;font-weight:700}
h2.geo{font-size:21px;margin:32px 0 4px;color:#0A4F44}
h2.geo .hl{font-weight:400;font-size:15px;color:#5b636c}
h2.geo .vol{font-weight:700;font-size:15px;color:#0A4F44}
ol.urls{list-style:none;margin-top:14px}
ol.urls li{margin-bottom:10px}
.row{display:flex;align-items:center;gap:12px;background:#fff;border:1px solid #d8dbe0;
 border-radius:9px;padding:14px 16px}
.row.done{opacity:.5;border-color:#00C249;background:#F6FFF9}
.tick{display:flex;align-items:center;gap:12px;flex:1;min-width:0;cursor:pointer;
 min-height:44px}
.tick input{width:22px;height:22px;flex:0 0 22px}
.n{background:#eef0f3;border-radius:50%;width:30px;height:30px;flex:0 0 30px;
 display:flex;align-items:center;justify-content:center;font-weight:700;font-size:14px}
.meta{min-width:0;flex:1}
.meta code{display:block;font:14px/1.45 ui-monospace,Menlo,Consolas,monospace;
 word-break:break-all;color:#1c2024}
.meta em{display:block;font-style:normal;font-size:14px;color:#5b636c;margin-top:3px}
button{font:inherit;font-size:14px;font-weight:700;border:0;border-radius:7px;
 padding:11px 18px;cursor:pointer;background:#0A4F44;color:#fff;min-height:44px;
 flex:0 0 auto}
button:hover{background:#0C5F52}
button.ok{background:#00C249;color:#04231E}
@media(max-width:640px){.row{flex-wrap:wrap}.meta code{font-size:13px}}
"""

JS = """
const K='wellaray-crawl-v2';
const st=JSON.parse(localStorage.getItem(K)||'{}');
function paint(){
  let n=0;
  document.querySelectorAll('.row').forEach(r=>{
    const u=r.querySelector('.tick input').dataset.u, on=!!st[u];
    r.classList.toggle('done',on);
    r.querySelector('.tick input').checked=on;
    if(on)n++;
  });
  document.getElementById('prog').textContent =
    n+' of '+document.querySelectorAll('.row').length+' submitted';
}
function copy(t,btn){
  const done=()=>{const o=btn.textContent;btn.textContent='Copied';btn.classList.add('ok');
    setTimeout(()=>{btn.textContent=o;btn.classList.remove('ok')},1300)};
  const ta=document.createElement('textarea');
  ta.value=t;ta.style.position='fixed';ta.style.opacity='0';
  document.body.appendChild(ta);ta.select();
  let ok=false;try{ok=document.execCommand('copy')}catch(e){}
  document.body.removeChild(ta);
  if(ok){done();return}
  if(navigator.clipboard)navigator.clipboard.writeText(t).then(done).catch(()=>{});
}
document.addEventListener('click',e=>{
  const b=e.target.closest('button.copy');
  if(b) copy(b.dataset.u,b);
});
document.addEventListener('change',e=>{
  const i=e.target.closest('.tick input');
  if(!i)return;
  if(i.checked) st[i.dataset.u]=1; else delete st[i.dataset.u];
  localStorage.setItem(K,JSON.stringify(st));paint();
});
paint();
"""


def main():
    urls = json.load(open(os.path.join("/root/workspace/wellaray", "to_index.json"),
                          encoding="utf-8"))
    by = collections.OrderedDict()
    for u in urls:
        owned, vol, geo = META.get(u, ("", 0, "?"))
        by.setdefault(geo, []).append((u, owned, vol))
    for g in by:
        by[g].sort(key=lambda x: -x[2])

    n = 0
    blocks = []
    for geo in ("de", "uk", "en"):
        rows = by.get(geo)
        if not rows:
            continue
        name, codes = GEO_TITLE[geo]
        tot = sum(r[2] for r in rows)
        items = []
        for u, owned, vol in rows:
            n += 1
            items.append(
                f'<li><div class="row">'
                f'<label class="tick"><input type="checkbox" data-u="{E(u)}">'
                f'<span class="n">{n}</span>'
                f'<span class="meta"><code>{E(u)}</code>'
                f'<em>{E(owned)} · {vol:,}/mo</em></span></label>'
                f'<button type="button" class="copy" data-u="{E(u)}">Copy</button>'
                f'</div></li>')
        blocks.append(
            f'<h2 class="geo">{E(name)} <span class="hl">{E(codes)}</span> '
            f'<span class="vol">{tot:,} searches/mo</span></h2>'
            f'<ol class="urls">{"".join(items)}</ol>')

    print(f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>wellaray.shop — Request Indexing</title>
<style>{CSS}</style>
</head><body>

<header><div class="wrap">
  <h1>wellaray.shop — Request Indexing</h1>
  <p>{n} pages Google has not crawled yet. 23 of 41 are already indexed.
     Biggest pages first — do them from the top.</p>
</div></header>

<div class="wrap">
<div class="prog" id="prog">0 of {n} submitted</div>

<div class="big">
  <h2>What to do</h2>
  <ol>
    <li>Open <b>Google Search Console</b> and pick the <b>wellaray.shop</b> property.</li>
    <li>Press <b>Copy</b> on the first line here.</li>
    <li>Paste it into the search box at the very top of Search Console. Press Enter.</li>
    <li>Wait for it to finish, then click <b>Request Indexing</b>.</li>
    <li>Come back and tick the box on that line.</li>
    <li>Do the next one.</li>
  </ol>
</div>

<div class="big">
  <h2>If it says you have run out</h2>
  <p>Google allows only about <b>10 to 12 requests a day per account</b>. When it stops
     letting you, that is normal — it is not an error.</p>
  <ul>
    <li>Add another Gmail as an <b>Owner</b> of the property, then sign in as that one and
        carry on. Each owner gets their own daily allowance.</li>
    <li>Split the list by country block so two people never submit the same address.</li>
    <li>Or simply come back tomorrow and continue from where you stopped.</li>
  </ul>
  <p style="margin-top:10px">Your ticks are saved in your own browser, so each person
     keeps their own progress.</p>
</div>

{"".join(blocks)}

<p style="margin-top:30px;color:#5b636c;font-size:15px">
  This page is hidden from Google. Ticks are saved in this browser only.
</p>

</div>
<script>{JS}</script>
</body></html>""")


if __name__ == "__main__":
    main()
