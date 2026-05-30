import os
import math
from PIL import Image

folder_path = "minds"

colors ={
    (255, 0, 0): "red",
    (0, 255, 0): "green",
    (0, 0, 255): "blue",
    (255, 255, 0): "yellow",
    (0, 255, 255): "cyan",
    (255, 255, 255): "white"
}

# https://stackoverflow.com/questions/15285534/isprime-function-for-python-language
def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  # since all primes > 3 are of the form 6n ± 1
  # start with f=5 (which is prime)
  # and test f, f+2 for being prime
  # then loop by 6. 
  f = 5
  while f <= r:
    #print('\t',f)
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True    
 
def getprimecount(counts):
    primecount = 0
    for color_name in counts:
        if is_prime(counts[color_name]):
            primecount += 1
    
    return primecoun``t

for filename in sorted(os.listdir(folder_path)):
    if filename.startswith("mind") and filename.endswith(".png"):
        file_path = os.path.join(folder_path, filename)
        
        image = Image.open(file_path)
        width, height = image.size
        pixels = image.load()
        
        counts = {name: 0 for name in colors.values()}
        
        for x in range(width):
            for y in range(height):
                pixel = pixels[x, y]
                
                if pixel in colors:
                    color_name = colors[pixel]
                    counts[color_name] += 1

    primecount = getprimecount(counts)

    hash = counts["red"] * 2 + counts["green"] * 3 + counts["blue"] * 5 + counts["yellow"] * 7 + counts["cyan"] * 11    

    if primecount == 0:
        hash += counts["red"]
    if primecount == 1:
        hash += counts["green"]
    if primecount == 2:
        hash += counts["blue"]
    if primecount >= 3:
        hash += abs(counts["yellow"] - counts["cyan"])

    hash += counts["red"] & counts["green"]
    hash += counts["green"] | counts["blue"]
    hash -= counts["yellow"] ^ counts["cyan"]

    if hash == 402931:
        print(f"Hash found!")
        print(f"{filename}")
        exit()
