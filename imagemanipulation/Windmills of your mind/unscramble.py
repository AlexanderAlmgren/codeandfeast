from PIL import Image, ImageDraw
import sys

ROTATION = -45
CIRCLE_COUNT = 24
SHRINK_PER_STEP = 20

INPUT = "scrambled.png"
OUTPUT = "unscrambled.png"

image = Image.open(INPUT)
width, height = image.size
centerx, centery = width // 2, height // 2

for i in range(CIRCLE_COUNT):

    radius = (width // 2) - i * SHRINK_PER_STEP

    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse(
        (centerx - radius, centery - radius, centerx + radius, centery + radius),
        fill=255
    )
    draw.ellipse(
        (centerx - radius + SHRINK_PER_STEP, centery - radius + SHRINK_PER_STEP, centerx + radius - SHRINK_PER_STEP, centery + radius - SHRINK_PER_STEP),
        fill=0
    )

    rotated = image.rotate(ROTATION * (i+1), resample=Image.BICUBIC, center=(centerx, centery))

    image = Image.composite(rotated, image, mask)

image.save(OUTPUT)
