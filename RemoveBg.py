from PIL import Image


def remove_background(path):
    green_screen = Image.open(path)
    pix = 1, 1
    background = (255, 255, 255, 0)
    to_see = green_screen.getpixel(pix)
    for pixel1 in range(green_screen.width):
        for pixel2 in range(green_screen.height):
            current_pixel = pixel1, pixel2
            analyzed_pixel = green_screen.getpixel(current_pixel)
            if analyzed_pixel == to_see or background[1] - analyzed_pixel[1] <= 30:
                green_screen.putpixel(current_pixel, background)
    green_screen.save('Imgs/test.jpg')


remove_background(input("Entrez le chemin de l'image: "))
