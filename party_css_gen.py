#!/usr/bin/env python3
import math
import argparse

MINIFY = True

def gen_bookmarklet(css):
    bookmarklet ="""javascript:(function(){
    var s = document.createElement('style');
    s.innerHTML = `
    <<CSS>>
    `;
    document.head.appendChild(s);
})();
"""
    bookmarklet = bookmarklet.replace("<<CSS>>", css)
    return bookmarklet

def generate_root_variables():
    return """:root {
  --max-translation: 0;   /* x pixels */
  --translation-phase: 0; /* degrees */
  --max-skew: 18;         /* degrees */
  --max-scale-diff: 0.15; /* scale factor */
  --anim-freq: 2;         /* Hz */

  --anim-time: calc(1/var(--anim-freq) * 1s);
}
"""

def generate_element_style():
    return """
.🦜 {
  animation: 🎉 var(--anim-time) infinite linear, 🎨 var(--anim-time) infinite linear;
  transform-origin: bottom center;
}
"""

def generate_tint_keyframes():
    colors = [
        "#ff8d8b", "#fed689", "#88ff89", "#87ffff", "#8bb5fe",
        "#d78cff", "#ff8cff", "#ff68f7", "#fe6cb7", "#ff6968"
    ]
    keyframes = ["0%, 100% { background-color: #ff8d8b; }"]
    num_colors = len(colors)
    pct_step = 100 / (num_colors - 1)
    for i, color in enumerate(colors[1:-1], 1):
        keyframes.append(f"{i * pct_step:.2f}% {{ background-color: {color}; }}")
    return "\n".join(keyframes)

def trunc_number(num):
    """Truncates ending zeros from a number. E.g. '1.000' -> '1', '1.100' -> '1.1'
    Makes the CSS output more concise, but uglier."""
    if MINIFY:
        return num.rstrip("0").rstrip(".")
    return num

def make_party_keyframe(progress, angle):
    skew_x = -math.cos(angle)
    scale_y = math.sin(angle)

    progress_str = f"{trunc_number(f'{progress * 100:.1f}')}%"

    # backspace character:
    skew_str = ""
    if not math.isclose(skew_x, 0, abs_tol=1e-6) or not MINIFY:
        skewMultiplier = trunc_number(f"{skew_x:.4f}")
        skew_str = f"skewX(calc(var(--max-skew) * {skewMultiplier}deg))"

    translateAngle = trunc_number(f"{angle:.4f}")
    translate_str = (
        f"translateX(calc(var(--max-translation) * "
        f"sin({translateAngle} + var(--translation-phase)) px))"
    )

    scaleYMultiplier = trunc_number(f"{scale_y:.4f}")
    scale_str = f"scaleY(calc(1 + var(--max-scale-diff) * {scaleYMultiplier}))"
    if math.isclose(scale_y, 0, abs_tol=1e-6) or not MINIFY:
        scale_str = f"scaleY(1)"

    if len(skew_str) > 0:
        skew_str += " "

    return f"{progress_str} {{ transform: {skew_str}{translate_str} {scale_str}; }}"

def generate_party_keyframes(steps=20):
    keyframes = []
    for i in range(steps + 1):
        progress = i / steps
        angle = 2 * math.pi * progress
        keyframes.append(make_party_keyframe(progress, angle))
    return "\n".join(keyframes)

def generate_css():
    css = []
    css.append(generate_root_variables())
    css.append(generate_element_style())
    css.append("@keyframes 🎨 {")
    css.append(generate_tint_keyframes())
    css.append("}")
    css.append("")
    css.append("@keyframes 🎉 {")
    css.append(generate_party_keyframes())
    css.append("}")
    return "\n".join(css)

def main():
    parser = argparse.ArgumentParser(description="Generate CSS animations for party effect.")
    parser.add_argument('-o', '--output', help="Output file path. If not specified, prints to console.")
    parser.add_argument('-b', '--bookmarklet', action='store_true', help="Generate bookmarklet.")

    args = parser.parse_args()

    css_output = generate_css()

    if args.output:
        with open(args.output, 'w') as f:
            f.write(css_output)
        print(f"CSS written to {args.output}")
    elif args.bookmarklet:
        with open("bookmarklet.js", 'w') as f:
            f.write(gen_bookmarklet(css_output))

    else:
        print(css_output)


if __name__ == "__main__":
    main()
