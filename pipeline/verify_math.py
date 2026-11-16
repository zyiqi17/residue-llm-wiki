"""檢查節點①：把 Wiki 裡登記的數學結論，用數值方法重算一次。

用法：python pipeline/verify_math.py
- 封閉曲線積分：梯形法（被積函數在圓上是週期函數，梯形法誤差指數下降）
- 留數：在該點周圍的小圓上積分再除以 2πi；自動挑「函數值不會爆掉的最小半徑」
- 實積分：scipy.integrate.quad（cos 型用 weight='cos'）
全部通過時 exit code = 0，有任何失敗則 = 1（給迴圈判斷要不要回去修 Wiki）
"""
import sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from claims import CLAIMS

NS = {k: getattr(np, k) for k in ["exp", "sin", "cos", "sinh", "cosh", "log", "sqrt", "pi"]}
NS["I"] = 1j


def fz(expr):
    code = compile(expr, "<f>", "eval")
    return lambda z: eval(code, {"__builtins__": {}}, {**NS, "z": z, "x": z})


def contour(f, center, radius, n=8192):
    t = 2 * np.pi * np.arange(n) / n
    z = center + radius * np.exp(1j * t)
    with np.errstate(all="ignore"):
        vals = f(z) * np.ones_like(z)
    return np.mean(vals * 1j * radius * np.exp(1j * t)) * 2 * np.pi


def residue(f, point):
    for r in [1e-3, 1e-2, 5e-2, 0.1, 0.2]:
        t = 2 * np.pi * np.arange(2048) / 2048
        with np.errstate(all="ignore"):
            vals = f(point + r * np.exp(1j * t))
        if np.all(np.isfinite(vals)) and np.max(np.abs(vals)) < 1e9:
            return contour(f, point, r, 2048) / (2j * np.pi)
    return np.nan


def real(f, a, b, expr):
    from scipy.integrate import quad
    g = lambda x: float(np.real(f(x)))
    if "cos(x)" in expr and np.isinf(a):           # 振盪積分：∫ cos(x) h(x) = 2∫_0^∞ cos(x) h(x)
        h = fz(expr.replace("cos(x)", "1"))
        val, _ = quad(lambda x: float(np.real(h(x))), 0, np.inf, weight="cos", wvar=1)
        return 2 * val
    return quad(g, a, b, limit=500)[0]


def check(cid, c):
    f = fz(c["f"])
    if c["kind"] == "contour":
        got = contour(f, c["center"], c["radius"])
    elif c["kind"] == "residue":
        got = residue(f, c["point"])
    else:
        got = real(f, c["a"], c["b"], c["f"])
    ok = abs(got - c["expected"]) < 1e-6 * max(1, abs(c["expected"]))
    return ok, got


def main():
    fails, total = [], 0
    for cid, spec in CLAIMS.items():
        for c in (spec if isinstance(spec, list) else [spec]):
            total += 1
            ok, got = check(cid, c)
            got_s = f"{complex(got).real:.6f}{complex(got).imag:+.6f}i"
            print(f"{'✅' if ok else '❌'} {cid:5s} {c['text']:<42s} 數值 = {got_s}")
            if not ok:
                fails.append(cid)
    print(f"\n驗算 {total} 項，通過 {total - len(fails)} 項，失敗 {len(fails)} 項 {fails if fails else ''}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
