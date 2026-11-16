# 操作日誌

> 時間序紀錄，格式：`## [日期] 動作 | 對象`。動作：discuss / fetch / ingest / reject / lint / verify / fix / query / build。

## [2026-11-17] discuss | 主題、讀者、長度
- 決定：留數定理；讀者是修過微積分的大一生；簡報 10～12 頁。見 `discussion/`。

## [2026-11-17] fetch | Wikipedia 4 篇（第 1 輪）
- ❌ 直接抓網址被拒（網址需先出現在搜尋結果中）→ 改成先搜尋再抓。
- ⚠️ 4 篇 Wikipedia 都抓到了，但**所有數學公式在擷取時遺失**，只剩文字。
- 決定：Wikipedia 只用來取「觀念與敘述」，數字與公式改找其他來源。

## [2026-11-17] fetch | 第 2 輪：找公式完整的來源
- 嘗試 MIT OCW 課程頁 → 只是 PDF 連結頁，改抓 PDF 鏡像（S5）。
- S5（Orloff Topic 8）公式完整，但抽取結果出現兩個疑點：例 8.15 的 5/24 vs 1/3、例 8.23 抽取模型推論的正負號。→ 登記為待驗算 V08、V11。
- Brilliant（X3）、prefetch（X4）、Companal（X2）、Wikiversity（X1）、LibreTexts 目錄頁（X5）內容不足或公式遺失 → 淘汰。
- 補抓 S6（Topic 9）、S7（LibreTexts 9.5）、S8、S9（Chong 的初學者教材）。

## [2026-11-17] ingest | S1–S9
- 每份來源寫入 `raw/`，再更新概念頁。共建立 10 個概念頁。
- S5 與 S7 為同一作者的兩個版本，5 個例題互相比對一致。

## [2026-11-17] verify | 第 1 輪數學驗算
- `verify_math.py`：25 項全部通過。
- V08 確認 sinh(z)eᶻ/z⁵ 的留數是 **1/3**（數值 0.333333），S5 抽取筆記中的 5/24 判定為錯誤。
- V11 確認 Res(f, ∞) = **−5**，抽取模型推論的 5 判定為錯誤。

## [2026-11-17] lint | 第 1 輪結構檢查 → fix
- ❌ `common-mistakes.md` 第 15 行：表格儲存格裡的 `|z|` 被當成欄位分隔線，欄位數 5 ≠ 3。
- fix：改寫成 `\|z\|`。重跑 → ✅ 全部通過。

## [2026-11-17] query | 用 Wiki 規劃簡報大綱（slides/outline.md）
- 查詢：「給大一生 10～12 頁講懂留數定理需要哪些內容」→ 依 index.md 學習路線選 8 個概念頁。
- ⚠️ 發現缺口：第 12 頁需要一題「自我檢測」，Wiki 沒有 → **回到 Wiki** 在 `residue-theorem.md` 新增例 7（|z| = 1/2，答案 4πi），登記驗算 V22。
- 第 4 頁要列出 n = −2…2 的表，原本 V02 只驗算 n = ±2 → 擴充 V02 涵蓋 n = 0, 1, 2, −2。
- 重跑驗算與 lint → ✅ 通過。

## [2026-11-17] build | 簡報數學排版
- 原本想用 KaTeX 排版公式，但建置環境連不到 CDN、npm 也無法下載 → 改用 Unicode 符號 + CSS 分數排版，簡報不依賴任何外部套件。

## [2026-11-17] build | 依大綱產生 slides/index.html（12 頁）

## [2026-11-17] lint | 簡報檢查第 1 輪 → fix
- `check_slides.py` 抓到 3 個問題：
  - ❌ 第 9 頁用了 V03，但 V03 在 `residue.md`，不在它標註的 `computing-residues.md` → data-wiki 補上 residue.md
  - ❌ 第 12 頁用了 V22，但 V22 在 `residue-theorem.md` → data-wiki 補上
  - ❌ 第 4 頁文字提到「留數」，但第 7 頁才定義 → 改寫成「後面所有內容都是從這裡來的」
- `render_check.js` 抓到 4 個問題：
  - ❌ JS 錯誤 ×3（三種螢幕各一次）：導覽點的 IntersectionObserver 寫錯，變數 `io` 在宣告前就被使用 → 重寫
  - ❌ 手機出現水平捲軸：第 8 頁兩欄排版中，不換行的公式把欄位撐寬 → 加 `min-width: 0`，手機版公式允許換行
- 重跑 → ✅ 兩支檢查都通過。

## [2026-11-17] lint | 人工看截圖 → 加強檢查程式
- 自動檢查通過，但看截圖發現第 8 頁公式被截斷（公式框可左右捲動，所以「溢出檢查」沒抓到）。
- 改善檢查：`render_check.js` 新增「公式框 scrollWidth > clientWidth」檢查 → 重跑確實抓到 s8。
- fix：公式改成 ∮ f dz = 2πi · Σ Res，並把圖上壓到曲線的標籤拉到外面 → 第 1 次修完仍差 53px，第 2 次精簡後 ✅ 通過。
