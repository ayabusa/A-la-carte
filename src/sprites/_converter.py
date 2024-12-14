from os import listdir
from os.path import isfile, join
from PIL import Image
import numpy as np

path = "./src/sprites/"
files_list = [f for f in listdir(path) if isfile(join(path, f))]

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
for i in range(w):
    for i in range(h):
        result.
image_croped.show()
exit()


for file in files_list:
    if not file.endswith(".png"):
        print("Skipping", file, ", because it's not a png image.")
        break
    image = Image.open(join(path, file))
    w, h = image.size
    offsetx, offsety = 0,0 

