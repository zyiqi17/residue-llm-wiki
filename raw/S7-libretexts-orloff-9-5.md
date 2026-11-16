# S7　9.5 Cauchy Residue Theorem — LibreTexts（Orloff, Complex Variables with Applications）

- 網址：https://math.libretexts.org/Bookshelves/Analysis/Complex_Variables_with_Applications_(Orloff)/09%3A_Residue_Theorem/9.05%3A_Cauchy_Residue_Theorem
- 取用日期：2026-11-17
- 抽取方式：WebFetch（由抽取模型整理成筆記）
- **抽取品質：合格（與 S5 同作者，可交叉比對）**

## 抽取筆記
- 定理假設：f 在區域 A 除孤立奇點外解析；C 是 A 中的簡單封閉曲線、不經過奇點、逆時針。
- 結論：∮_C f dz = 2πi × (C 內部留數和)。
- 證明想法：在每個奇點周圍挖小圓、加切口，使新的曲線內部沒有極點 → 柯西定理得 0 → 切口抵消 → 只剩小圓積分，每個 = 2πi × 留數。
- 例 9.5.2：∮_{|z|=2} (5z−2)/(z(z−1)) dz = 10πi（與 S5 例 8.19 一致）。
- 例 9.5.3：z² sin(1/z) = z − (1/6)/z + …，Res = −1/6，積分 −iπ/3（與 S5 一致）。
- 例 9.5.4：1/(z(z−2)⁴) 在 z = 2 的展開 1/(2(z−2)⁴) − 1/(4(z−2)³) + 1/(8(z−2)²) − 1/(16(z−2)) + …，Res = −1/16（與 S5 一致）。
- 例 9.5.5：1/sin z 圍 0, π, 2π → 2πi（與 S5 一致）。
