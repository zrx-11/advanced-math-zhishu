#!/usr/bin/env python3
"""双视口冒烟检查：桌面/手机、章节/概念/诊断，测内边距与横向溢出。"""
import json, pathlib, sys
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDEX = (ROOT / "index.html").as_uri()
OUT = ROOT / "_build" / "shots"
OUT.mkdir(parents=True, exist_ok=True)

def check(page, label, url, shot):
    errs = []
    page.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
    page.goto(url, wait_until="load")
    page.wait_for_timeout(1200)
    stats = page.evaluate("""() => {
      const main = document.querySelector('.main') || document.querySelector('main');
      const nav = document.querySelector('#nav');
      const r = main ? main.getBoundingClientRect() : null;
      const bodyW = document.body.clientWidth;
      const tbl = Array.from(document.querySelectorAll('table')).map(t=>t.scrollWidth - t.clientWidth).filter(x=>x>2);
      const katex = document.querySelectorAll('.katex').length;
      return {
        mainLeft: r ? Math.round(r.left) : null,
        mainRight: r ? Math.round(bodyW - r.right) : null,
        bodyW,
        tableOverflow: tbl,
        katex,
        navH: nav ? Math.round(nav.getBoundingClientRect().height) : null,
        navMaxH: nav ? getComputedStyle(nav).maxHeight : null,
        textLen: (document.querySelector('#view')||{}).innerText?.length || 0
      };
    }""")
    page.screenshot(path=str(OUT / shot), full_page=False)
    print(label, json.dumps(stats, ensure_ascii=False), "console_errors=", len(errs))
    if errs: print("   ", errs[:3])
    return stats

def run():
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/local/bin/chromium", args=["--no-sandbox"])
        for w, h, tag in [(390, 844, "mobile"), (1440, 900, "desktop")]:
            page = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
            print(f"=== {tag} {w}x{h} ===")
            check(page, "首页", INDEX, f"{tag}-home.png")
            check(page, "章节 ch05", INDEX + "#/book/food-math/chapter/ch05", f"{tag}-ch05.png")
            check(page, "概念 c18（深度折叠）", INDEX + "#/book/food-math/concept/c18", f"{tag}-c18.png")
            # 展开深度片段
            page.evaluate("""() => { const d=document.querySelector('details.depth-fragment'); if(d) d.open=true; }""")
            page.wait_for_timeout(400)
            page.screenshot(path=str(OUT / f"{tag}-c18-open.png"))
            check(page, "诊断页", INDEX + "#/book/food-math/diagnosis", f"{tag}-diag.png")
            check(page, "测验 ch06", INDEX + "#/book/food-math/quiz/ch06", f"{tag}-quiz.png")
            page.close()
        b.close()

if __name__ == "__main__":
    run()
