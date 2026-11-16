#!/usr/bin/env bash
# 依序執行所有檢查節點；任何一關失敗就停下，並告訴你要回到哪一步。
# 用法：bash pipeline/run_all.sh
cd "$(dirname "$0")/.."

echo "① 數學驗算 ─────────────"
python3 pipeline/verify_math.py || { echo "→ 回到 Wiki 修正概念頁的數字"; exit 1; }

echo; echo "② Wiki 結構檢查 ─────────"
python3 pipeline/check_wiki.py || { echo "→ 回到 Wiki 修正連結 / 來源 / 索引"; exit 1; }

echo; echo "③ 簡報追溯與術語檢查 ─────"
python3 pipeline/check_slides.py || { echo "→ 回到簡報（術語順序錯就回到大綱）"; exit 1; }

echo; echo "④ 簡報版面檢查 ──────────"
node pipeline/render_check.js || { echo "→ 回到簡報修版面"; exit 1; }

echo; echo "🎉 全部通過，可以發布"
