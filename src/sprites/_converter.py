from os import listdir
from os.path import isfile, join
from PIL import Image
import numpy as np

path = "./src/sprites/"
files_list = [f for f in listdir(path) if isfile(join(path, f))]
colors = [(26,28,44),(93,39,93),(177,62,83),(239,125,87),(255,205,117),(167,240,112),(56,183,100),(37,113,121),(41,54,111),(59,93,201),(65,166,246),(115,239,247),(244,244,244),(148,176,194),(86,108,134),(51,60,87)]

def get_color_id(r, g, b, a)->str:
    if a ==0: # if transparent
        return "g"
    try:
        i = colors.index((r,g,b))
    except: # if color is invalid
        return "h"
    if i < 10: # if id is in [0,9]
        return str(i)
    else: # else we do letters
        match i:
            case 10:
                return "a"
            case 11:
                return "b"
            case 12:
                return "c"
            case 13:
                return "d"
            case 14:
                return "e"
            case 15:
                return "f"

def get_offset_x(img, w, h)->int:
    offsetx = 0
    for i in range(h):
        for i in range(w):
                if img.getpixel((offsetx, i))[3] == 0:
                    continue
                else:
                    return offsetx
        offsetx+=1
    return offsetx

def get_offset_y(img, w, h)->int:
    offsety = 0
    for i in range(w):
        for i in range(h):
                if img.getpixel((i, offsety))[3] == 0:
                    continue
                else:
                    return offsety
        offsety+=1
    return offsety

def get_croped_image(img)-> tuple[Image.Image, int, int]:
    w, h = img.size
    offsetx, offsety = get_offset_x(image, w, h), get_offset_y(img, w, h)
    img_reversed = image.rotate(180)
    neg_offsetx, neg_offsety = get_offset_y(img_reversed, w, h), get_offset_x(img_reversed, w, h)
    img_croped = img.crop((offsetx, offsety, h-neg_offsety, w-neg_offsetx))
    print("w;", w, "h",h,"x:",offsetx, "y:", offsety, "neg x:", neg_offsetx, "neg y:", neg_offsety)
    print(h-offsetx-neg_offsetx, w-offsety-neg_offsety)
    return (img_croped, offsetx, offsety)

image = Image.open(join(path, "salade.png"))
image_croped, off_x, off_y = get_croped_image(image)
w, h = image_croped.size
result = ""
for v in range(h):
    for k in range(w):
        result += get_color_id(*image_croped.getpixel((k, v)))
print('result is,', result)
image_croped.show()
exit()


for file in files_list:
    if not file.endswith(".png"):
        print("Skipping", file, ", because it's not a png image.")
        break
    image = Image.open(join(path, file))
    w, h = image.size
    offsetx, offsety = 0,0 

