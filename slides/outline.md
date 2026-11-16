# 簡報大綱（由 Wiki 查詢產生）

> 查詢問題：「給修過微積分的大一生，用 10～12 頁講懂留數定理，需要 Wiki 的哪些內容？」
> 依 `wiki/index.md` 的學習路線取材；每頁只用 Wiki 裡有的內容。

| # | 標題 | 取自 Wiki 頁面 | 驗算 | 新定義的術語 | 用到的術語 |
|---|---|---|---|---|---|
| 1 | 繞一圈就知道答案 | index.md | | | |
| 2 | 你已經會算的積分 | real-integrals.md | V12 | | |
| 3 | 在複數平面上積分 | contour-integral-basics.md | | 封閉曲線積分 | |
| 4 | 神奇的 ∮ zⁿ dz | contour-integral-basics.md | V01 V02 | | 封閉曲線積分 |
| 5 | 奇點與極點 | singularities-and-poles.md | | 奇點、極點 | |
| 6 | 羅朗級數：把函數拆開 | laurent-series.md | V04 | 羅朗級數 | 奇點 |
| 7 | 留數：剩下來的東西 | residue.md | V03 | 留數 | 羅朗級數、封閉曲線積分 |
| 8 | 留數定理 | residue-theorem.md | V17 | 留數定理 | 留數、奇點 |
| 9 | 怎麼算留數：蓋住法 | computing-residues.md | V03 V19 | | 極點、留數 |
| 10 | 例題：10πi | residue-theorem.md | V06 | | 留數定理、留數 |
| 11 | 回到開頭：用留數算 π | real-integrals.md | V12 | | 留數定理、極點 |
| 12 | 總結與三個常見錯誤 | common-mistakes.md | | | 留數、留數定理、極點 |

## 設計理由

- **第 2 頁先放熟悉的 ∫ dx/(1+x²) = π**，第 11 頁用留數再算一次：讓聽眾有「原來可以這樣算」的收尾。
- 術語「先定義後使用」：由 `check_slides.py` 自動檢查。
- 主例題選 (5z−2)/(z(z−1))：S5、S7 兩個來源都有，而且兩個留數都是整數，適合初學者。
