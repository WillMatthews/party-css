#!/usr/bin/env python3
import math
import argparse

MINIFY = False

class CSSGenerator:
    def __init__(self):
        # 🦜 colors can be obtained from extract-colours.py
        self.colors = [
            "#ff8d8b", "#fed689", "#88ff89", "#87ffff", "#8bb5fe",
            "#d78cff", "#ff8cff", "#ff68f7", "#fe6cb7", "#ff6968"
        ]
        self._css = None
        self.minify = MINIFY

    def _generate_root_variables(self):
        return """:root {
  --max-translation: 0;   /* x pixels */
  --translation-phase: 0; /* radians */
  --max-skew: 18;         /* degrees */
  --max-scale-diff: 0.15; /* scale factor */
  --anim-freq: 2;         /* Hz */

  --anim-time: calc(1/var(--anim-freq) * 1s);
}
"""

    def _generate_element_style(self):
        return """
.🦜 {
  animation: 🎉 var(--anim-time) infinite linear, 🎨 var(--anim-time) infinite linear;
  transform-origin: bottom center;
}
"""

    def _generate_tint_keyframes(self):
        keyframes = ["  0%,\n  100% { background-color: #ff8d8b; }"]
        num_colors = len(self.colors)
        pct_step = 100 / (num_colors - 1)
        for i, color in enumerate(self.colors[1:-1], 1):
            keyframes.append(f"{i * pct_step:.2f}% {{ background-color: {color}; }}")
        return "\n  ".join(keyframes)

    def _trunc_number(self, num):
        if self.minify:
            return num.rstrip("0").rstrip(".")
        return num

    def _make_party_keyframe(self, progress, angle):
        skew_x = -math.cos(angle)
        scale_y = math.sin(angle)
        progress_str = f"  {self._trunc_number(f'{progress * 100:.1f}')}%"

        skew_str = ""
        if not math.isclose(skew_x, 0, abs_tol=1e-6) or not self.minify:
            skew_multiplier = self._trunc_number(f"{skew_x:.4f}")
            skew_str = f" skewX(calc(var(--max-skew) * {skew_multiplier}deg))"

        translate_angle = self._trunc_number(f"{angle:.4f}")
        translate_str = (
            f"translateX(calc(var(--max-translation) * "
            f"sin({translate_angle} + var(--translation-phase)) px))"
        )

        scale_y_multiplier = self._trunc_number(f"{scale_y:.4f}")
        scale_str = f"scaleY(calc(1 + var(--max-scale-diff) * {scale_y_multiplier}))"
        if math.isclose(scale_y, 0, abs_tol=1e-6) and self.minify:
            scale_str = f"scaleY(1)"

        return f"{progress_str} {{ transform:{skew_str} {translate_str} {scale_str}; }}"

    def _generate_party_keyframes(self, steps=20):
        keyframes = []
        for i in range(steps + 1):
            progress = i / steps
            angle = 2 * math.pi * progress
            keyframes.append(self._make_party_keyframe(progress, angle))
        return "\n".join(keyframes)

    def generate_css(self):
        if self._css is None:
            css = [
                self._generate_root_variables(),
                self._generate_element_style(),
                "@keyframes 🎨 {",
                self._generate_tint_keyframes(),
                "}",
                "",
                "@keyframes 🎉 {",
                self._generate_party_keyframes(),
                "}"
            ]
            self._css = "\n".join(css)
        return self._css

    def get_css(self):
        return self.generate_css()

def gen_bookmarklet(css_generator):
    bookmarklet = """
javascript:(function(){
  var s = document.createElement('style');
  s.innerHTML = `
<<CSS>>
  `;
  document.head.appendChild(s);
})();
"""
    return bookmarklet.replace("<<CSS>>", css_generator.get_css())

def main():
    parser = argparse.ArgumentParser(description="Generate CSS animations for party effect.")
    parser.add_argument('-o', '--output', help="Output file path. If not specified, prints to console.")
    parser.add_argument('-b', '--bookmarklet', action='store_true', help="Generate bookmarklet.")
    args = parser.parse_args()

    css_generator = CSSGenerator()

    if args.output:
        with open(args.output, 'w') as f:
            f.write(css_generator.get_css())
        print(f"CSS written to {args.output}")
    elif args.bookmarklet:
        with open("bookmarklet.js", 'w') as f:
            f.write(gen_bookmarklet(css_generator))
    else:
        print(css_generator.get_css())

if __name__ == "__main__":
    main()
