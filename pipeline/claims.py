"""Wiki 裡每個 ✅V編號 的數學結論，在這裡登記成「可以用電腦驗算」的形式。

kind:
  contour : 數值計算 ∮_{|z-center|=radius} f(z) dz，和 expected 比較
  residue : 在 point 周圍小圓上數值積分 / 2πi，和 expected 比較
  real    : 數值計算 ∫_a^b f(x) dx，和 expected 比較
"""
from math import pi, sqrt, e, sin, cos

I = 1j

CLAIMS = {
    # ---- contour-integral-basics.md ----
    "V01": dict(kind="contour", f="1/z", center=0, radius=1, expected=2*pi*I,
                text="∮_{|z|=1} dz/z = 2πi"),
    "V02": dict(kind="contour", f="1 + z + z**2 + 1/z**2", center=0, radius=1, expected=0,
                text="∮_{|z|=1} zⁿ dz = 0（n = 0, 1, 2, −2）"),
    # ---- residue.md / laurent-series.md ----
    "V03": dict(kind="residue", f="z/(z**2+1)", point=I, expected=0.5,
                text="Res(z/(z²+1), i) = 1/2"),
    "V04": dict(kind="residue", f="exp(1/(2*z))", point=0, expected=0.5,
                text="Res(e^{1/(2z)}, 0) = 1/2"),
    "V05": dict(kind="contour", f="z**2*sin(1/z)", center=0, radius=1, expected=-pi*I/3,
                text="∮_{|z|=1} z² sin(1/z) dz = −πi/3"),
    "V20": dict(kind="residue", f="1/z**3 + 2/z**2 + 4/z + 5 + 6*z", point=0, expected=4,
                text="Res(1/z³+2/z²+4/z+5+6z, 0) = 4"),
    # ---- computing-residues.md ----
    "V08": dict(kind="residue", f="sinh(z)*exp(z)/z**5", point=0, expected=1/3,
                text="Res(sinh z·eᶻ/z⁵, 0) = 1/3（來源衝突：5/24）"),
    "V09": dict(kind="residue", f="1/(z*(z**2+1)*(z-2)**2)", point=2, expected=-13/100,
                text="Res(1/(z(z²+1)(z−2)²), 2) = −13/100"),
    "V18": dict(kind="residue", f="1/(z*(z**2+1)*(z-2)**2)", point=0, expected=1/4,
                text="Res(1/(z(z²+1)(z−2)²), 0) = 1/4"),
    "V19": dict(kind="residue", f="5/(I-3*z)", point=I/3, expected=-5/3,
                text="Res(5/(i−3z), i/3) = −5/3"),
    "V10": dict(kind="residue", f="1/sin(z)", point=pi, expected=-1,
                text="Res(1/sin z, π) = −1"),
    # ---- residue-theorem.md ----
    "V06": dict(kind="contour", f="(5*z-2)/(z*(z-1))", center=0, radius=2, expected=10*pi*I,
                text="∮_{|z|=2} (5z−2)/(z(z−1)) dz = 10πi"),
    "V22": dict(kind="contour", f="(5*z-2)/(z*(z-1))", center=0, radius=0.5, expected=4*pi*I,
                text="∮_{|z|=1/2} (5z−2)/(z(z−1)) dz = 4πi"),
    "V07": dict(kind="contour", f="1/(z*(z-2)**4)", center=2, radius=1, expected=-pi*I/8,
                text="∮_{|z−2|=1} 1/(z(z−2)⁴) dz = −πi/8"),
    "V17": [dict(kind="contour", f="1/(z*(z**2+1))", center=I, radius=0.5, expected=-pi*I,
                 text="1/(z(z²+1)) 只圍 i → −πi"),
            dict(kind="contour", f="1/(z*(z**2+1))", center=0.5*I, radius=0.8, expected=pi*I,
                 text="1/(z(z²+1)) 圍 i 與 0 → πi"),
            dict(kind="contour", f="1/(z*(z**2+1))", center=0, radius=2, expected=0,
                 text="1/(z(z²+1)) 三個都圍 → 0")],
    "V21": [dict(kind="contour", f="1/(z**2+1)", center=I, radius=1, expected=pi,
                 text="1/(z²+1) 只圍 i → π"),
            dict(kind="contour", f="1/(z**2+1)", center=0, radius=2, expected=0,
                 text="1/(z²+1) 兩個都圍 → 0")],
    # V10 的第二部分：圍住 0, π, 2π
    "V10b": dict(kind="contour", f="1/sin(z)", center=pi, radius=4, expected=2*pi*I,
                 text="1/sin z 圍住 0、π、2π → 2πi"),
    # ---- residue-at-infinity.md ----
    "V11": dict(kind="contour", f="-(5*z-2)/(z*(z-1))/(2*pi*1j)", center=0, radius=2, expected=-5,
                text="Res(f, ∞) = −(1/2πi)∮ f dz = −5"),
    # ---- real-integrals.md ----
    "V12": dict(kind="real", f="1/(1+x**2)", a=float("-inf"), b=float("inf"), expected=pi,
                text="∫ dx/(1+x²) = π"),
    "V13": dict(kind="real", f="1/(1+x**2)**2", a=float("-inf"), b=float("inf"), expected=pi/2,
                text="∫ dx/(1+x²)² = π/2"),
    "V14": dict(kind="real", f="1/(1+x**4)", a=float("-inf"), b=float("inf"), expected=pi/sqrt(2),
                text="∫ dx/(1+x⁴) = π/√2"),
    "V15": dict(kind="real", f="cos(x)/(4*x**2+1)", a=float("-inf"), b=float("inf"), expected=pi/(2*sqrt(e)),
                text="∫ cos x/(4x²+1) dx = π/(2√e)"),
    "V16": dict(kind="real", f="1/(1+0.25-2*0.5*cos(x))", a=0, b=2*pi, expected=2*pi/(1-0.25),
                text="∫₀^{2π} dθ/(1+a²−2a cos θ) = 2π/(1−a²)，a = 0.5"),
}
