from PIL import Image
import numpy as np

INPUT = "scrambled.png"
OUTPUT = "unscrambled.png"

image = Image.open(INPUT)
width, height = image.size
arr = np.array(image)

top_row = arr[0, :, :]

brightness = 0.2126 * top_row[:, 0] + 0.7152 * top_row[:, 1] + 0.0722 * top_row[:, 2]

sorted_indices = np.argsort(brightness)

sorted_arr = arr[:, sorted_indices, :]

unscrambled_image = Image.fromarray(sorted_arr.astype(np.uint8))
unscrambled_image.save(OUTPUT)
