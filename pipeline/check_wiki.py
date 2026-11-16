"""檢查節點②：Wiki 結構檢查（lint）。

用法：python pipeline/check_wiki.py
檢查：
  1. 概念頁有 AGENTS.md §3 規定的段落，順序正確
  2. 每個概念頁的「來源」至少一個，且引用的 [S#] 都是 sources.md 裡「採用」的來源
  3. 每個 [S#] 在 raw/ 有對應的抽取筆記
  4. 相對連結都指得到檔案
  5. 每個概念頁都有登記在 index.md（沒有孤兒頁）
  6. 每個 ✅V## 都有登記在 pipeline/claims.py；claims.py 的每一項也都有被 Wiki 用到
  7. Markdown 表格每一列欄位數一致
"""
import re, sys, os, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "pipeline"))
from claims import CLAIMS

REQUIRED = ["## 直覺", "## 正式內容", "## 例子", "## 常見錯誤", "## 相關頁面", "## 來源"]
problems = []
def bad(page, msg): problems.append(f"{os.path.relpath(page, ROOT)}: {msg}")

sources_md = open(os.path.join(ROOT, "wiki/sources.md"), encoding="utf-8").read()
adopted = set(re.findall(r"^\| (S\d+) \|", sources_md, re.M))
raw_ids = {os.path.basename(p).split("-")[0] for p in glob.glob(os.path.join(ROOT, "raw/*.md"))}
index = open(os.path.join(ROOT, "wiki/index.md"), encoding="utf-8").read()

concept_pages = sorted(glob.glob(os.path.join(ROOT, "wiki/concepts/*.md")))
all_md = concept_pages + [os.path.join(ROOT, f"wiki/{n}.md") for n in ["index", "sources", "log"]]
used_claims = set()

for page in all_md:
    text = open(page, encoding="utf-8").read()
    is_concept = "/concepts/" in page

    if is_concept:
        # 1. 段落
        pos = [text.find(h) for h in REQUIRED]
        missing = [h for h, p in zip(REQUIRED, pos) if p < 0]
        if missing:
            bad(page, f"缺少段落 {missing}")
        elif pos != sorted(pos):
            bad(page, "段落順序錯誤")
        # 2. 來源
        src_section = text.split("## 來源")[-1]
        if not re.search(r"\[S\d+\]", src_section):
            bad(page, "「來源」段落沒有任何來源")
        for s in set(re.findall(r"\[(S\d+)\]", text)):
            if s not in adopted:
                bad(page, f"引用了未採用的來源 {s}")
            if s not in raw_ids:
                bad(page, f"{s} 在 raw/ 沒有抽取筆記")
        # 5. 索引
        if f"concepts/{os.path.basename(page)}" not in index:
            bad(page, "沒有登記在 index.md")

    # 4. 連結
    for target in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", text):
        if target.startswith("http"):
            continue
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(page), target))):
            bad(page, f"連結指不到檔案：{target}")

    # 6. 驗算編號
    for cid in re.findall(r"✅(V\d+)", text):
        used_claims.add(cid)
        if cid not in CLAIMS:
            bad(page, f"{cid} 沒有登記在 claims.py")

    # 7. 表格欄位數（去掉 \| 跳脫後計算）
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        if lines[i].startswith("|"):
            block = []
            while i < len(lines) and lines[i].startswith("|"):
                block.append((i + 1, lines[i])); i += 1
            counts = [(n, len(re.split(r"(?<!\\)\|", l.strip())) - 2) for n, l in block]
            expect = counts[0][1]
            for n, c in counts:
                if c != expect:
                    bad(page, f"第 {n} 行表格欄位數 {c}，應為 {expect}（儲存格裡的 | 要寫成 \\|）")
        else:
            i += 1

unused = {k for k in CLAIMS if not k.endswith("b")} - used_claims
for k in sorted(unused):
    problems.append(f"pipeline/claims.py: {k} 沒有被任何 Wiki 頁面使用")

print(f"檢查 {len(concept_pages)} 個概念頁、{len(adopted)} 個採用來源、{len(used_claims)} 個驗算編號")
for p in problems:
    print("❌", p)
print("✅ Wiki 檢查全部通過" if not problems else f"\n共 {len(problems)} 個問題")
sys.exit(1 if problems else 0)
