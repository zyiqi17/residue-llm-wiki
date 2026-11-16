# S9　9.4 Using Contour Integration to Solve Definite Integrals — LibreTexts（Chong）

- 網址：https://phys.libretexts.org/Bookshelves/Mathematical_Physics_and_Pedagogy/Complex_Methods_for_the_Sciences_(Chong)/09:_Contour_Integration/9.04:_Using_Contour_Integration_to_Solve_Definite_Integrals
- 取用日期：2026-11-17
- 抽取方式：WebFetch（由抽取模型整理成筆記）
- **抽取品質：合格（適合初學者的說法）**

## 抽取筆記
- 六步驟：解析延拓（把 x 換成 z）→ 加一段弧把路徑封閉 → 留數定理 → 拆成「實軸 + 弧」→ 證明弧 → 0 → 解出實積分（cos/sin 型取實部或虛部）。
- 弧為什麼消失（直覺）：1/(z²+1) 在半徑 R 的弧上大約 1/R²，弧長大約 R，所以弧的積分大約 1/R → 0。
- 例 A：∫ dx/(x²+1) = π（上半平面極點 i，留數 1/(2i)）。
- 例 B：∫ cos x/(4x²+1) dx = π/(2√e)（極點 i/2，留數 e^{−1/2}/(4i)）。
- 例 C：∫ sin x / x dx = π（主值、繞過原點的小半圓貢獻 −iπ）。
- 選哪個半平面：選讓 e^{iqz} 衰減的那一半（q > 0 選上半平面）。
