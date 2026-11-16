"""檢查節點③：簡報檢查。

用法：python pipeline/check_slides.py
檢查：
  1. 頁數在 10～12 頁（討論時決定的長度）
  2. 可追溯：每頁的 data-wiki 指向存在的 Wiki 頁面
  3. 可追溯：每頁的 data-checks 都登記在 claims.py，而且「出現在該頁引用的 Wiki 頁面裡」
     （數字不能憑空出現在簡報上）
  4. 讀者檢查：術語「先定義、後使用」
     - data-uses 的術語必須在更前面的頁面 data-defines 過
     - 掃描每頁的文字，術語第一次出現的頁碼不能早於定義它的那一頁（封面除外）
"""
import re, sys, os
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "pipeline"))
from claims import CLAIMS


class Slides(HTMLParser):
    def __init__(self):
        super().__init__(); self.slides = []; self.depth = 0; self.skip = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "section" and "slide" in (a.get("class") or ""):
            self.slides.append({**a, "text": ""}); self.depth = 1; return
        if self.depth:
            self.depth += tag not in ("br", "img", "line", "circle", "polygon", "path", "ellipse")
        if tag in ("script", "style"): self.skip += 1
    def handle_endtag(self, tag):
        if tag in ("script", "style"): self.skip -= 1
        if self.depth and tag not in ("br",):
            self.depth -= 1
    def handle_data(self, data):
        if self.slides and self.depth and not self.skip:
            self.slides[-1]["text"] += data


p = Slides(); p.feed(open(os.path.join(ROOT, "slides/index.html"), encoding="utf-8").read())
S = p.slides
problems = []
def bad(i, msg): problems.append(f"第 {i + 1} 頁（{S[i]['id']}）：{msg}")

# 1. 頁數
if not 10 <= len(S) <= 12:
    problems.append(f"頁數 {len(S)}，不在 10～12 頁")

# 2、3. 可追溯
for i, s in enumerate(S):
    pages = s.get("data-wiki", "").split()
    if not pages:
        bad(i, "沒有標 data-wiki"); continue
    wiki_text = ""
    for pg in pages:
        path = os.path.join(ROOT, "wiki", pg)
        if not os.path.exists(path):
            bad(i, f"data-wiki 指向不存在的頁面 {pg}")
        else:
            wiki_text += open(path, encoding="utf-8").read()
    for cid in s.get("data-checks", "").split():
        if cid not in CLAIMS:
            bad(i, f"{cid} 沒有登記在 claims.py")
        elif f"✅{cid}" not in wiki_text:
            bad(i, f"{cid} 不在它引用的 Wiki 頁面 {pages} 裡（數字來源對不上）")

# 4. 術語先定義後使用
defined_at = {}
for i, s in enumerate(S):
    for t in s.get("data-defines", "").split():
        defined_at.setdefault(t, i)
for i, s in enumerate(S):
    for t in s.get("data-uses", "").split():
        if t not in defined_at:
            bad(i, f"用到術語「{t}」，但沒有任何一頁定義它")
        elif defined_at[t] >= i:
            bad(i, f"用到術語「{t}」，但它在第 {defined_at[t] + 1} 頁才定義")
for t, d in defined_at.items():
    for i, s in enumerate(S[1:d], start=1):          # 封面（第 1 頁）不檢查
        if t in s["text"]:
            bad(i, f"文字裡提到「{t}」，但它在第 {d + 1} 頁才定義（讀者還看不懂）")

print(f"檢查 {len(S)} 頁簡報、{len(defined_at)} 個術語")
for x in problems:
    print("❌", x)
print("✅ 簡報檢查全部通過" if not problems else f"\n共 {len(problems)} 個問題")
sys.exit(1 if problems else 0)
