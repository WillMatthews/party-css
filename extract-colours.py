import requests
from io import BytesIO
from PIL import Image, ImageSequence

# URL of the party parrot 🦜🦜🦜🦜🦜
gif_url = "https://cultofthepartyparrot.com/parrots/hd/parrot.gif"

# Download the 🦜 GIF
print("Downloading the 🦜...")
response = requests.get(gif_url)
gif = Image.open(BytesIO(response.content))

# Extract the median 🦜 color from each 🦜 frame
frame_colors = []
for frame in ImageSequence.Iterator(gif):
    frame = frame.convert('RGBA')  # Convert frame to RGBA
    colors = frame.getcolors(maxcolors=1000)  # Get colors in the frame
    if colors:
        # Sort colors by count and exclude white
        non_white_colors = [color for color in sorted(colors, key=lambda x: x[0], reverse=True) if color[1] != (255, 255, 255, 0)]
        if non_white_colors:
            # Calculate median color from all non-white colors weighted by their count
            total_count = sum(count for count, _ in non_white_colors)
            cumulative_count = 0
            median_threshold = total_count / 2
            
            # Find the median color by cumulative count
            median_color = non_white_colors[0][1]
            for count, color in non_white_colors:
                cumulative_count += count
                if cumulative_count >= median_threshold:
                    median_color = color
                    break
            
            frame_colors.append(median_color)

hex_colors = ['#%02x%02x%02x' % (r, g, b) for (r, g, b, a) in frame_colors]

print("🦜 Frame colors:")

for i, color in enumerate(hex_colors):
    ansiColor = f"\033[38;2;{frame_colors[i][0]};{frame_colors[i][1]};{frame_colors[i][2]}m"

    print (f"{ansiColor}Frame {str(i+1).rjust(2, '0')}: {color}" + "\033[0m")
