# 🐱 留數定理 LLM Wiki → 教學 HTML 簡報

先用 **LLM Wiki** 整理「留數定理」的知識，再只用 Wiki 的內容產生一份給大一生的**教學簡報**。

- 🎞️ **教學簡報**：https://zyiqi17.github.io/residue-llm-wiki/slides/
- 📚 **Wiki 目錄**：[wiki/index.md](wiki/index.md)
- 🔁 **流程設計**：[docs/workflow.md](docs/workflow.md)
- 🧾 **執行紀錄**：[docs/run-log.md](docs/run-log.md)　🪞 **反思**：[docs/reflection.md](docs/reflection.md)

## Wiki 有什麼

- **主題**：複變函數的留數定理
- **讀者**：修過微積分、還沒學過複變的大一生
- **ingest 了 9 份資料**（另有 5 份因公式遺失或內容不足而淘汰）：Wikipedia 4 篇、MIT 18.04 講義 2 份、LibreTexts 3 頁 → [來源清單](wiki/sources.md)
- **10 個概念頁**，每頁固定有「直覺／正式內容／例子／常見錯誤」
- **22 個數字結論**都用程式數值驗算過（[pipeline/claims.py](pipeline/claims.py)）

## 資料夾

```
discussion/  先討論、後生成的紀錄
raw/         每份來源的抽取筆記（S1–S9 採用、X1–X5 淘汰）
wiki/        LLM Wiki：index、log、sources、concepts/
pipeline/    檢查程式：數學驗算、Wiki lint、簡報追溯、版面
slides/      教學 HTML 簡報（outline.md 是大綱）
docs/        流程圖、執行紀錄、反思
AGENTS.md    Wiki 的規則（schema）
```

## 自己跑一次檢查

```bash
pip install numpy scipy
npm install playwright   # 只有版面檢查需要
bash pipeline/run_all.sh
```

> 本專案由 Claude 協助建立，流程、檢查與執行紀錄見 docs/。
