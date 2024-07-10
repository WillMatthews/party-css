import math

# all in px
maxTranslation = 0
maxSkew = 10
maxScaleDiff = 0.1

def generate_party_keyframes(steps=20):
    keyframes = []
    for i in range(steps + 1):
        progress = i / steps
        angle = 2 * math.pi * progress

        # Calculate skew
        skew_x = -math.cos(angle) * maxSkew

        # Calculate translation
        translate_x = math.sin(angle) * maxTranslation

        # Calculate scale
        scale_y = 1 + math.sin(angle) * maxScaleDiff

        keyframe = f"{progress * 100:.1f}% {{ transform: skew({skew_x:.2f}deg, 0deg) translateX({translate_x:.2f}px) scaleY({scale_y:.2f}); }}"
        keyframes.append(keyframe)
    return "\n".join(keyframes)

# Generate and print the keyframes
print("@keyframes party {")
print(generate_party_keyframes())
print("}")
