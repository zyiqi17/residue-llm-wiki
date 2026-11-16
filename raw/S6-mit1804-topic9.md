# S6　MIT 18.04 Topic 9: Definite integrals using the residue theorem（J. Orloff 講義 PDF）

- 網址：https://ocw.tau.edu.ng/courses/mathematics/18-04-complex-variables-with-applications-spring-2018/lecture-notes/MIT18_04S18_topic9.pdf
- 取用日期：2026-11-17
- 抽取方式：WebFetch（由抽取模型整理成筆記）
- **抽取品質：合格（公式大致完整；後段微分方程例題係數無法辨識，不使用）**

## 抽取筆記
- 一般步驟：找一個在實軸上等於被積函數的解析函數 → 選一條包含實軸線段的封閉曲線 → 其他段要能算 → 用留數定理 → 組合得到答案。
- 定理 9.1：若 |z| 大時 |f(z)| ≤ M/|z|^a 且 a > 1，則上半圓弧的積分 → 0（估計：≤ πM R^{1−a}）。
- 有理函數：分母次數 ≥ 分子次數 + 2 時，∫_{−∞}^{∞} f dx = 2πi × (上半平面留數和)。
- 例 9.3：∫ dx/(1+x²)² = π/2（i 是二階極點，留數 −i/4）。
- 例 9.4：∫ dx/(1+x⁴) = π/√2。
- 例 9.5：∫₀^∞ cos(ax)/(x²+b²) dx = π e^{−ab}/(2b)（a, b > 0），把 cos 換成 e^{iax} 再取實部。
- 三角積分：z = e^{iθ}，cos θ = (z + 1/z)/2，sin θ = (z − 1/z)/(2i)，dθ = dz/(iz)。
- 例 9.6：∫₀^{2π} dθ/(1 + a² − 2a cos θ) = 2π/(1−a²)（|a| < 1）。
- 例 9.15：∫₀^∞ sin x / x dx = π/2。
