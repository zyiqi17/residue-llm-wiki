# AGENTS.md — 留數定理 LLM Wiki 的規則（Schema）

> 這份文件告訴 AI：這個 Wiki 怎麼組織、怎麼 ingest 新資料、怎麼查詢、怎麼檢查。
> 參考 Karpathy 提出的 LLM Wiki 模式：**原始資料（raw）→ LLM 整理成互相連結的 Wiki → 由 Wiki 產生成品**。

## 1. 目的

- **主題**：複變函數的「留數定理」
- **讀者**：修過微積分、還沒學過複變的大一生
- **用途**：作為知識庫，產生教學 HTML 簡報（`slides/`）

## 2. 資料夾

```
discussion/   先討論、後生成：開工前的討論紀錄（主題、讀者、範圍）
raw/          每份來源的「抽取筆記」，ingest 後不再修改（S1、S2…）
wiki/
  index.md    所有頁面的目錄（每新增一頁都要登記）
  log.md      時間序的操作日誌（ingest / query / lint / 修正）
  sources.md  來源清單與可信度
  concepts/   概念頁，一個概念一頁
pipeline/     檢查程式（驗算數學、檢查 Wiki、檢查簡報）
slides/       由 Wiki 產生的教學簡報
docs/         流程設計、執行紀錄、反思
```

## 3. 概念頁格式（`wiki/concepts/*.md`）

每一頁都必須有以下段落，順序固定：

```markdown
# 頁面標題

> 一句話摘要（給第一次看到的人）

## 直覺
## 正式內容
## 例子
## 常見錯誤        ← 沒有就寫「（尚無）」
## 相關頁面        ← 用相對連結，例如 [留數](residue.md)
## 來源            ← 列出 [S5] 這種來源代號，至少一個
```

- 每個**數學結論**後面標來源，例如 `Res = 1/2 [S5][S8]`
- 每個**可以驗算的數字**後面標驗算編號，例如 `= 10πi ✅V06`，並在 `pipeline/claims.py` 登記
- 檔名用英文小寫加短橫線：`residue-theorem.md`

## 4. Ingest 流程（新增一份資料時）

1. 在 `raw/` 新增 `S編號-簡稱.md`：網址、取用日期、抽取筆記、**抽取品質**（公式是否完整）
2. 抽取品質不合格（公式遺失、內容不相關）→ 在 `wiki/sources.md` 標「淘汰」並寫原因，**不要**用它寫概念頁
3. 合格 → 更新相關概念頁（一份資料通常會動到 2～5 頁），新的數字結論要登記驗算
4. 兩份來源說法衝突 → 在概念頁寫出衝突，以 `pipeline/verify_math.py` 的驗算結果為準
5. 更新 `wiki/index.md` 與 `wiki/log.md`
6. 跑 `python pipeline/check_wiki.py` 和 `python pipeline/verify_math.py`，**全部通過才算 ingest 完成**

## 5. Query 規則（用 Wiki 回答問題或做簡報時）

- 只能使用 Wiki 裡有的內容；Wiki 沒有的，先 ingest 新資料，不要憑記憶補
- 簡報每一頁都要標 `data-wiki`（用了哪一頁）與 `data-checks`（用了哪些驗算編號）

## 6. 檢查規則

| 檢查 | 程式 | 失敗時回到 |
|---|---|---|
| 數學驗算（數值積分 vs. Wiki 寫的答案） | `pipeline/verify_math.py` | 修概念頁 |
| 連結、來源、索引完整 | `pipeline/check_wiki.py` | 修概念頁 / index |
| 簡報可追溯、術語先定義後使用、版面不溢出 | `pipeline/check_slides.py`、`pipeline/render_check.js` | 修簡報（術語順序錯則回到大綱） |

## 7. 語言

繁體中文（台灣用語）。專有名詞第一次出現附英文，例如「留數（residue）」。
