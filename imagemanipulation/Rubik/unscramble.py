from PIL import Image, ImageDraw
import sys
import numpy as np
import math

INPUT = "scrambled.png"
OUTPUT = "uscrambled.png"

def rotate(chunks):

    tl = chunks[0]
    tr = chunks[6]
    bl = chunks[2]
    br = chunks[8]

    chunks[0] = tr
    chunks[6] = br
    chunks[2] = tl
    chunks[8] = bl

    l = chunks[1]
    r = chunks[7]
    t = chunks[3]
    b = chunks[5]

    chunks[3] = r
    chunks[7] = b
    chunks[5] = l
    chunks[1] = t

    return chunks

def spiral(img, size, px, py):
    
    chunks = []

    chunksize = int(size / 3)

    for x in range(3):
        for y in range(3):
            chunk = (
                px + x * chunksize, 
                py + y * chunksize, 
                px + (x+1) * chunksize, 
                py + (y+1) * chunksize,
                )
            chunks.append(img.crop(chunk))

    chunks = rotate(chunks)

    i = 0
    for x in range(3):
        for y in range(3):
            img.paste(chunks[i], (x * chunksize + px, y * chunksize + py))
            i += 1

image = Image.open(INPUT)
width, height = image.size

spiral(image, width, 0, 0)

for x in range(3):
    for y in range(3):
        spiral(image, width/3, x*math.ceil(width/3), y*math.ceil(width/3))
        for sx in range(3):
            for sy in range(3):
                spiral(image, width/3/3, x*int(width/3) + sx*int(width/3/3), y*int(width/3) + sy*int(width/3/3))

image.save(OUTPUT)
