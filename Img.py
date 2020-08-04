from PIL import Image
from PIL import ImageColor
import numpy as np
import os
import random


def remove_background(path):
    green_screen = Image.open(path)
    pix = 1, 1
    background = 255, 255, 255, 0
    to_see = green_screen.getpixel(pix)
    for pixel1 in range(green_screen.width):
        for pixel2 in range(green_screen.height):
            current_pixel = pixel1, pixel2
            analyzed_pixel = green_screen.getpixel(current_pixel)
            if analyzed_pixel == to_see:
                green_screen.putpixel(current_pixel, background)
    #new_path = random.random() * 100 + path.split(".")[1]
    #green_screen.save(new_path)
    (left, upper, right, lower) = (20, 20, 100, 100)  # temporaire avant que je trouve comment mettre background transparent...
    return green_screen.crop((left, upper, right, lower))


def change_background():
    background_img = input("Entrez le nom de l'image de fond: ")
    foreground_img = input("Entrez le nom de l'image en premier plan: ")
    destination = input("Entrez le nom du nouveau fichier: ")

    cropped_img = remove_background(foreground_img)

    back_img = Image.open(background_img)
    back_img.paste(cropped_img)

    back_img.save(destination)


change_background()
