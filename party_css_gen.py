#!/usr/bin/env python3
import math
import argparse

def generate_root_variables():
    return """
:root {
  --max-translation: 0;   /* x pixels */
  --max-skew: 18;         /* degrees */
  --max-scale-diff: 0.15; /* scale factor */
  --anim-freq: 2;         /* Hz */

  --anim-time: calc(1/var(--anim-freq) * 1s);
}
"""

def generate_element_style():
    return """
.🦜 {
  animation: 🎉 var(--anim-time) infinite linear, tint var(--anim-time) infinite linear;
  transform-origin: bottom center;
}
"""

def generate_tint_keyframes():
    colors = [
        "#FF6B6B", "#FF6BB5", "#FF81FF", "#D081FF",
        "#81ACFF", "#81FFFF", "#81FF81", "#FFD081", "#FF6B6B"
    ]
    keyframes = ["0%, 100% { background-color: #FF6B6B; }"]
    for i, color in enumerate(colors[1:-1], 1):
        keyframes.append(f"{i * 12.5}% {{ background-color: {color}; }}")
    return "\n".join(keyframes)

def generate_party_keyframes(steps=20):
    keyframes = []
    for i in range(steps + 1):
        progress = i / steps
        angle = 2 * math.pi * progress
        skew_x = -math.cos(angle)
        translate_x = math.sin(angle)
        scale_y = math.sin(angle)
        keyframe = f"{progress * 100:.1f}% {{ transform: skew(calc(var(--max-skew) * {skew_x:.4f}deg), 0deg) translateX(calc(var(--max-translation) * {translate_x:.4f}px)) scaleY(calc(1 + var(--max-scale-diff) * {scale_y:.4f})); }}"
        keyframes.append(keyframe)
    return "\n".join(keyframes)

def generate_css():
    css = []
    css.append(generate_root_variables())
    css.append(generate_element_style())
    css.append("@keyframes tint {")
    css.append(generate_tint_keyframes())
    css.append("}")
    css.append("@keyframes 🎉 {")
    css.append(generate_party_keyframes())
    css.append("}")
    return "\n".join(css)

def main():
    parser = argparse.ArgumentParser(description="Generate CSS animations for party effect.")
    parser.add_argument('-o', '--output', help="Output file path. If not specified, prints to console.")
    args = parser.parse_args()

    css_output = generate_css()

    if args.output:
        with open(args.output, 'w') as f:
            f.write(css_output)
        print(f"CSS written to {args.output}")
    else:
        print(css_output)

if __name__ == "__main__":
    main()
