from PIL import Image
from PIL import ImageColor
import numpy as np
import os

greenScreen = Image.open('greenscreen.jpg')

pix = 1, 1

background = 255, 255, 255, 0

toSee = greenScreen.getpixel(pix)

for pixel1 in range(greenScreen.width):
    for pixel2 in range(greenScreen.height):
        currPixel = pixel1, pixel2
        analyzedPixel = greenScreen.getpixel(currPixel)
        if analyzedPixel == toSee:
            greenScreen.putpixel(currPixel, background)

greenScreen.save('test.jpg')
