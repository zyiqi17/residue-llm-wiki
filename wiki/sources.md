# 來源清單

> 每個來源的抽取筆記在 [`raw/`](../raw/)。「可信度」是 ingest 時依抽取品質給的評分。

## 採用（9 份）

| 代號 | 來源 | 類型 | 可信度 | 主要用在 |
|---|---|---|---|---|
| S1 | [Residue theorem — Wikipedia](https://en.wikipedia.org/wiki/Residue_theorem) | 百科 | ★★☆ 公式遺失，只用文字敘述 | 定理一般形式、繞數 |
| S2 | [Residue (complex analysis) — Wikipedia](https://en.wikipedia.org/wiki/Residue_(complex_analysis)) | 百科 | ★★☆ 公式遺失 | 留數定義、計算方法清單 |
| S3 | [Laurent series — Wikipedia](https://en.wikipedia.org/wiki/Laurent_series) | 百科 | ★★☆ 公式遺失 | 羅朗級數觀念、奇點分類、歷史 |
| S4 | [Cauchy's integral formula — Wikipedia](https://en.wikipedia.org/wiki/Cauchy%27s_integral_formula) | 百科 | ★★☆ 公式遺失 | 柯西積分公式與推論 |
| S5 | [MIT 18.04 Topic 8: Residue Theorem（Orloff）](https://ocw.iti.hr/courses/mathematics/18-04-complex-variables-with-applications-spring-2018/lecture-notes/MIT18_04S18_topic8.pdf) | 大學講義 | ★★★ 公式完整（1 處數值疑義，見 V08） | 定義、計算公式、大部分例題 |
| S6 | [MIT 18.04 Topic 9: Definite integrals（Orloff）](https://ocw.tau.edu.ng/courses/mathematics/18-04-complex-variables-with-applications-spring-2018/lecture-notes/MIT18_04S18_topic9.pdf) | 大學講義 | ★★★ | 實積分方法與例題 |
| S7 | [9.5 Cauchy Residue Theorem — LibreTexts（Orloff）](https://math.libretexts.org/Bookshelves/Analysis/Complex_Variables_with_Applications_(Orloff)/09%3A_Residue_Theorem/9.05%3A_Cauchy_Residue_Theorem) | 線上教科書 | ★★★ 與 S5 交叉比對一致 | 定理敘述、證明想法 |
| S8 | [9.3 Poles — LibreTexts（Chong）](https://phys.libretexts.org/Bookshelves/Mathematical_Physics_and_Pedagogy/Complex_Methods_for_the_Sciences_(Chong)/09%3A_Contour_Integration/9.03%3A_Poles) | 線上教科書 | ★★★ 適合初學者 | 「剩下來的東西」直覺、方向符號 |
| S9 | [9.4 Definite Integrals — LibreTexts（Chong）](https://phys.libretexts.org/Bookshelves/Mathematical_Physics_and_Pedagogy/Complex_Methods_for_the_Sciences_(Chong)/09:_Contour_Integration/9.04:_Using_Contour_Integration_to_Solve_Definite_Integrals) | 線上教科書 | ★★★ 適合初學者 | 六步驟、弧消失的直覺 |

## 淘汰（5 份）

| 代號 | 來源 | 淘汰原因 |
|---|---|---|
| X1 | [Real integrals with residue theorem — Wikiversity](https://en.wikiversity.org/wiki/Complex_Analysis/Real_integrals_with_residue_theorem) | 公式與答案全部遺失 |
| X2 | [Semicircular contour method — Companal](https://companal.subwiki.org/wiki/Semicircular_contour_integration_method) | 內容太少 |
| X3 | [Residue theorem — Brilliant](https://brilliant.org/wiki/residue-theorem/) | 擷取到的只有繞數介紹 |
| X4 | [Residue theorem — prefetch.eu](https://prefetch.eu/know/concept/residue-theorem) | 只有簡單極點，已被 S5、S8 涵蓋 |
| X5 | [09: Residue Theorem 目錄頁 — LibreTexts](https://math.libretexts.org/Bookshelves/Analysis/Complex_Variables_with_Applications_(Orloff)/09%3A_Residue_Theorem) | 只是目錄，改抓子頁 S7 |

## 來源之間的衝突

| 項目 | 說法 A | 說法 B | 判定 |
|---|---|---|---|
| sinh(z)eᶻ/z⁵ 在 0 的留數 | S5 抽取筆記：5/24 | 級數乘開：1/3 | **1/3**（驗算 V08） |
| Res(f, ∞)，f = (5z−2)/(z(z−1)) | 抽取模型推論：5 | S5 講義：−5 | **−5**（驗算 V11） |
