from PIL import Image, ImageDraw, ImageFont
import math


def create_image_from_string(text, output_file="output.png", line_thickness=3):
    # Image dimensions
    width, height = 2550, 3300
    n = len(text)

    if n == 0:
        raise ValueError("Input string must not be empty.")

    # Create white background image
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Find best grid (rows x cols)
    best_size = 0
    best_rows, best_cols = 0, 0

    for rows in range(1, n + 1):
        cols = math.ceil(n / rows)

        square_width = width / cols
        square_height = height / rows
        square_size = min(square_width, square_height)

        if square_size > best_size:
            best_size = square_size
            best_rows, best_cols = rows, cols

    square_size = int(best_size)

    # Center the grid
    total_width = square_size * best_cols
    total_height = square_size * best_rows

    x_offset = (width - total_width) // 2
    y_offset = (height - total_height) // 2

    # Try to load a decent font; fallback if unavailable
    try:
        font_size = int(square_size * 0.25)
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    # Draw squares + text
    count = 0
    for r in range(best_rows):
        for c in range(best_cols):
            if count >= n:
                break

            x1 = x_offset + c * square_size
            y1 = y_offset + r * square_size
            x2 = x1 + square_size
            y2 = y1 + square_size

            # Draw square
            draw.rectangle(
                [x1, y1, x2, y2],
                outline="black",
                width=line_thickness
            )

            # Prepare label
            label = f"{count+1}-{text[count]}"

            # Measure text
            bbox = draw.textbbox((0, 0), label, font=font)
            text_w = bbox[2] - bbox[0]
            text_h = bbox[3] - bbox[1]

            # Center text
            text_x = x1 + (square_size - text_w) // 2
            text_y = y1 + (square_size - text_h) // 2

            draw.text((text_x, text_y), label, fill="black", font=font)

            count += 1
        if count >= n:
            break

    # Save image
    image.save(output_file)
    print(f"Saved image to {output_file}")


if __name__ == "__main__":
    string = input()
    create_image_from_string(string, line_thickness=6)
