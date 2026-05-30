import os
import random
from PIL import Image, ImageDraw, ImageFont

output_dir = "minds"
os.makedirs(output_dir, exist_ok=True)

img_size = (300, 300)

colors = [
    (255, 0, 0),     # Red
    (0, 255, 0),     # Green
    (0, 0, 255),     # Blue
    (255, 255, 0),   # Yellow
    (0, 255, 255)    # Cyan
]

font_path = "arial.ttf"

for i in range(1, 101):

    image = Image.new("RGB", img_size)

    num_cols = random.randint(1, 5)
    col_width = img_size[0] // num_cols
    draw_bg = ImageDraw.Draw(image)
    for col in range(num_cols):
        x0 = col * col_width
        x1 = (col + 1) * col_width if col < num_cols - 1 else img_size[0]
        color = random.choice(colors)
        draw_bg.rectangle([x0, 0, x1, img_size[1]], fill=color)

    text = f"ctf{{mind{i:03d}}}"
    text_color = random.choice(colors)

    font = ImageFont.truetype(font_path, 46)

    temp = Image.new("L", img_size)
    draw_temp = ImageDraw.Draw(temp)
    bbox = draw_temp.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    x = (img_size[0] - text_w) // 2
    y = (img_size[1] - text_h) // 2

    padding = 10
    rect_coords = [
        x - padding,
        y - padding,
        x + text_w + padding,
        y + text_h + padding
    ]
    draw_bg.rectangle(rect_coords, fill=(255, 255, 255))

    mask = Image.new("1", img_size, 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.text((x, y), text, fill=1, font=font)

    color_layer = Image.new("RGB", img_size, text_color)

    image.paste(color_layer, mask=mask)

    filename = os.path.join(output_dir, f"mind{i:03d}.png")
    image.save(filename)
