from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def change_background(back, front):
    back_img = back
    fore_img = front

    pix = 1, 1

    to_see = fore_img.getpixel(pix)

    for pixel1 in range(fore_img.width):
        for pixel2 in range(fore_img.height):
            current_pixel = pixel1, pixel2
            analyzed_pixel = fore_img.getpixel(current_pixel)
            if analyzed_pixel == to_see:
                fore_img.putpixel(current_pixel, back_img.getpixel(current_pixel))

    return fore_img


def add_text(img, text):
    img = img.convert("RGBA")
    txt = Image.new("RGBA", img.size, (255, 255, 255, 0))

    fnt = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 200)

    draw = ImageDraw.Draw(txt)
    draw.text((10, 60), text, font=fnt, fill=(255, 255, 255, 255))
    out = Image.alpha_composite(img, txt)

    return out


def create_thumbnail():
    background_img = input("Entrez le nom de l'image de fond: ")
    foreground_img = input("Entrez le nom de l'image en premier plan: ")
    text = input("Entrez le texte à mettre sur la couverture: ")

    back_img = Image.open(background_img)
    fore_img = Image.open(foreground_img)

    changed_bg = change_background(back_img, fore_img)
    final = add_text(changed_bg, text)

    final.show()


create_thumbnail()
