import requests
from io import BytesIO
from PIL import Image, ImageSequence

# URL of the party parrot 🦜🦜🦜🦜🦜
gif_url = "https://cultofthepartyparrot.com/parrots/hd/parrot.gif"

# Download the 🦜 GIF
response = requests.get(gif_url)
gif = Image.open(BytesIO(response.content))

# Extract the first non-white 🦜 color from each 🦜 frame
frame_colors = []
for frame in ImageSequence.Iterator(gif):
    frame = frame.convert('RGBA')  # Convert frame to RGBA
    colors = frame.getcolors(maxcolors=1000)  # Get colors in the frame
    if colors:
        # Sort colors by count and exclude white
        non_white_colors = [color for color in sorted(colors, key=lambda x: x[0], reverse=True) if color[1] != (255, 255, 255, 0)]
        if non_white_colors:
            first_non_white_color = non_white_colors[0][1]
            frame_colors.append(first_non_white_color)

hex_colors = ['#%02x%02x%02x' % (r, g, b) for (r, g, b, a) in frame_colors]
print(hex_colors)
