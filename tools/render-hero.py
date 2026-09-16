#!/usr/bin/env python3
"""README 맨 위 그림(docs/assets/hero*.svg)을 그린다. 어두운 테마와 밝은 테마로 하나씩 만든다.

묶은 것과 고르는 기준만 보여 준다. 검사 규칙 예시는 싣지 않는다. 근거 없이 정한 규칙을
2026-09-17 에 뺐고, 비교 분석이 채택한 지표가 나오면 그때 다시 넣는다.

사용: python3 tools/render-hero.py
"""
import pathlib
import unicodedata
from xml.sax.saxutils import escape

REPO = pathlib.Path(__file__).resolve().parent.parent

# (묶은 것, 하는 일, 어디서 왔나)
ROWS = [
    ("윤문", "이미 쓴 글을 사실과 숫자는 두고 문체만 다듬는다", "im-not-ai"),
    ("글자 수", "한국어 글자 수를 어림하지 않고 스크립트로 센다", "k-skill"),
    ("검사 규칙", "사람 글과 Claude 글을 비교해 근거가 생기면 넣는다", "분석 중"),
]
TEXT = {
    "tag1": "원하는 것만 묶고 맘대로 커스텀한 Claude Code 플러그인",
    "tag2": "내가 쓰려고 분석한 한국어 도구들",
    "cap": "묶은 것",
    "criteria": [("첫째", "의미가 절대 손실되지 않는 명확한 한국어"),
                 ("둘째", "번역체 교정과 AI 표현 최소화")],
    "foot": "네트워크를 쓰지 않습니다 · MIT",
}
THEME = {
    "dark": {"bg": "#1e2229", "text": "#e6eaf0", "dim": "#9aa4b2", "accent": "#7ee0a3",
             "chip": "#2d333d", "chipt": "#ffd166", "rule": "#39404b", "stage": "#262b33"},
    "light": {"bg": "#f6f7f9", "text": "#1f2328", "dim": "#59636e", "accent": "#1a7f37",
              "chip": "#e7ebf0", "chipt": "#9a6700", "rule": "#d0d7de", "stage": "#eceff3"},
}
W, H, M = 1280, 640, 64
SANS = "'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', sans-serif"
MONO = "'SF Mono', Menlo, Consolas, monospace"
X_NAME, X_DESC, X_FROM = 272, 560, 1216


def width(s, size):
    # 대략의 글자 폭. 한글은 1em, 로마자와 빈칸은 0.55em 으로 잡는다.
    return sum(size if unicodedata.east_asian_width(c) in "WF" else size * 0.55 for c in s)


def check_fit():
    for name, desc, _src in ROWS:
        if X_DESC + width(desc, 20) > X_FROM - 120:
            raise SystemExit(f"「{desc}」 가 칸을 넘친다")


def t(x, y, s, size, fill, weight=400, family=SANS, anchor="start"):
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}">{escape(s)}</text>')


def render(theme):
    c = THEME[theme]
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
         f'<rect width="{W}" height="{H}" rx="16" fill="{c["bg"]}"/>',
         t(M, 112, "korean-writing", 56, c["text"], 700, MONO),
         t(W - M, 84, TEXT["tag1"], 20, c["dim"], 400, anchor="end"),
         t(W - M, 116, TEXT["tag2"], 24, c["text"], 700, anchor="end"),
         f'<line x1="{M}" y1="148" x2="{W - M}" y2="148" stroke="{c["rule"]}" stroke-width="2"/>',
         t(M, 186, TEXT["cap"], 14, c["dim"], 700)]
    y = 240
    for name, desc, src in ROWS:
        o.append(f'<rect x="{M}" y="{y - 24}" width="{X_NAME - M - 20}" height="34" rx="17" fill="{c["chip"]}"/>')
        o.append(t(M + 16, y, name, 16, c["chipt"], 700))
        o.append(t(X_DESC, y, desc, 20, c["text"]))
        o.append(t(X_FROM, y, src, 15, c["dim"], 400, anchor="end"))
        y += 62
    y += 16
    n = len(TEXT["criteria"])
    sw = (W - 2 * M - (n - 1) * 16) / n
    for i, (head, body) in enumerate(TEXT["criteria"]):
        x = M + i * (sw + 16)
        o.append(f'<rect x="{x:.0f}" y="{y}" width="{sw:.0f}" height="72" rx="12" fill="{c["stage"]}"/>')
        o.append(t(x + 20, y + 30, head, 15, c["chipt"], 700))
        o.append(t(x + 20, y + 54, body, 17, c["text"]))
    o.append(t(M, H - 36, "claude plugin install korean-writing", 18, c["dim"], 400, MONO))
    o.append(t(W - M, H - 36, TEXT["foot"], 16, c["dim"], 400, anchor="end"))
    o.append("</svg>")
    return "\n".join(o) + "\n"


def main():
    check_fit()
    for theme in ("dark", "light"):
        name = "hero" + ("-light" if theme == "light" else "") + ".svg"
        (REPO / "docs" / "assets" / name).write_text(render(theme), encoding="utf-8")
        print("그렸다:", "docs/assets/" + name)


if __name__ == "__main__":
    main()
