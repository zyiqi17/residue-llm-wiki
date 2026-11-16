// 檢查節點④：用無頭瀏覽器實際打開簡報，檢查版面
// 用法：node pipeline/render_check.js [截圖輸出資料夾]
// 檢查：JS 錯誤、每頁在 1280×720 是否塞得下（不溢出）、手機寬度是否有水平捲軸
const { chromium } = require("playwright");
const path = require("path");

(async () => {
  const file = "file://" + path.resolve(__dirname, "../slides/index.html");
  const outDir = process.argv[2];
  const browser = await chromium.launch();
  const problems = [];

  for (const [w, h, label] of [[1280, 720, "筆電"], [1440, 900, "桌機"], [390, 844, "手機"]]) {
    const page = await browser.newPage({ viewport: { width: w, height: h } });
    page.on("pageerror", e => problems.push(`[${label}] JS 錯誤：${e.message}`));
    await page.goto(file);
    await page.waitForTimeout(500);

    if (w < 760) {
      const hs = await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1);
      if (hs) problems.push(`[${label}] 出現水平捲軸`);
    } else {
      const over = await page.$$eval(".slide", (ss, vh) => ss.map((s, i) => {
        const inner = s.querySelector(".inner");
        const need = inner.scrollHeight + 56 + 64;           // 內容 + 上下留白
        return need > vh ? `第 ${i + 1} 頁內容高 ${need}px > 視窗 ${vh}px` : null;
      }).filter(Boolean), h);
      over.forEach(o => problems.push(`[${label}] ${o}`));
      // v2 加強：公式框可以左右捲動，所以上面的檢查抓不到「公式被截斷」→ 直接比較寬度
      const cut = await page.$$eval(".eq", es => es.map(e => {
        const s = e.closest(".slide");
        return e.scrollWidth > e.clientWidth + 1 ? `${s.id} 的公式被截斷（需要 ${e.scrollWidth}px，只有 ${e.clientWidth}px）` : null;
      }).filter(Boolean));
      cut.forEach(o => problems.push(`[${label}] ${o}`));
      if (outDir && w === 1280) {
        const n = await page.$$eval(".slide", ss => ss.length);
        for (let i = 0; i < n; i++) {
          await page.evaluate(i => { document.documentElement.style.scrollBehavior = "auto"; document.querySelectorAll(".slide")[i].scrollIntoView({ behavior: "instant" }); }, i);
          await page.waitForTimeout(150);
          await page.screenshot({ path: `${outDir}/slide-${String(i + 1).padStart(2, "0")}.png` });
        }
      }
    }
    await page.close();
  }
  await browser.close();
  problems.forEach(p => console.log("❌", p));
  console.log(problems.length ? `\n共 ${problems.length} 個問題` : "✅ 版面檢查全部通過");
  process.exit(problems.length ? 1 : 0);
})();
