from PIL import Image
import random

INPUT = "original.png"
OUTPUT = "scrambled.png"

image = Image.open(INPUT)
width, height = image.size
pixels = image.load()

scrambled_image = Image.new(image.mode, image.size)
scrambled_pixels = scrambled_image.load()

columns = list(range(width))
random.shuffle(columns)

for new_x, old_x in enumerate(columns):
    for y in range(height):
        scrambled_pixels[new_x, y] = pixels[old_x, y]

scrambled_image.save(OUTPUT)

