from os import listdir
from os.path import isfile, join
from PIL import Image
import numpy as np
import pprint

colors = [(26,28,44),(93,39,93),(177,62,83),(239,125,87),(255,205,117),(167,240,112),(56,183,100),(37,113,121),(41,54,111),(59,93,201),(65,166,246),(115,239,247),(244,244,244),(148,176,194),(86,108,134),(51,60,87)]

def get_color_id(r: int, g: int, b: int, a: int)->str:
    """
    Get the pixel color id, it is a str that goes from 0 to h
    """
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

def get_offset_x(img: Image.Image, w: int, h: int)->int:
    """
    Returns the x offset of an image
    """
    offsetx = 0
    for i in range(h):
        for i in range(w):
                if img.getpixel((offsetx, i))[3] == 0:
                    continue
                else:
                    return offsetx
        offsetx+=1
    return offsetx

def get_offset_y(img: Image.Image, w: int, h: int)->int:
    """
    Returns the y offset of an image
    """
    offsety = 0
    for i in range(w):
        for i in range(h):
                if img.getpixel((i, offsety))[3] == 0:
                    continue
                else:
                    return offsety
        offsety+=1
    return offsety

def get_croped_image(img: Image.Image)->tuple[Image.Image, int, int]:
    """
    Removes the borders (transparent) from the image and return the x and y offsets to get it to the right position
    """
    w, h = img.size
    offsetx, offsety = get_offset_x(img, w, h), get_offset_y(img, w, h)
    img_reversed = img.rotate(180)
    neg_offsetx, neg_offsety = get_offset_y(img_reversed, w, h), get_offset_x(img_reversed, w, h)
    img_croped = img.crop((offsetx, offsety, h-neg_offsety, w-neg_offsetx))
    return (img_croped, offsetx, offsety)

def compress_string_image(img: str,w: int,h: int)->str:
    l = []
    for i in range(h):
        l.append(img[i*w:(i+1)*w-1])
    print(l)
    for i in range(len(l)):
        l_of_rep = []
        rep = [0,0,0]
        for k in range(len(l[i])):
            if rep==[0,0,0]:
                rep=[k,k,l[i][k]]
            else:
                if rep[2]==l[i][k]:
                    rep[1]=k
                else:
                    if rep[1]-rep[0]>2:
                        l_of_rep.append(rep)
                    rep = [0,0,0]
        if rep[1]-rep[0]>2:
            l_of_rep.append(rep)
        nv_li = l[i]
        for rep_i in l_of_rep:
            nv_li = nv_li.replace(rep_i[2]*(rep_i[1]-rep_i[0]), "?"+str(rep_i[2])+str(rep_i[1]-rep_i[0])+"!")
        print(nv_li)

def compress2(img: str,w: int,h: int)->str:
    l = []
    de = ""
    de.replace
    char = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","d","e","f","g","h"]
    for i in range(h):
        l.append(img[i*w:(i+1)*w-1])
    print(l)
    result = ""
    for i in range(len(l)):
        nv_li = l[i]
        for k in char:
            for m in range(w,4,-1):
                nv_li = nv_li.replace(k*m, "?"+k+str(m)+"!")
        result+=nv_li
    return result


def convert_all_files(save_to_file: bool, compress_sprites: bool, path: str)->None:
    files_list = [f for f in listdir(path) if isfile(join(path, f))]
    result_file = None
    final_result = {}
    if save_to_file: 
        result_file = open(join(path, "sprites_converted.txt"), "w")

    for file in files_list:
        if not file.endswith(".png"):
            print("Skipping", file, ", because it's not a png image.")
            continue
        image = Image.open(join(path, file))
        image_croped, off_x, off_y = get_croped_image(image)
        w, h = image_croped.size
        result = ""
        for v in range(h):
            for k in range(w):
                result += get_color_id(*image_croped.getpixel((k, v)))
        result = compress2(result, w,h)
        print('Finished,', file, '\n', result, '\n')
        final_result[file.removesuffix(".png")] = (off_x, off_y, w, h, result)
    if save_to_file: 
        result_file.write(file + "\n" + pprint.pformat(final_result, compact=True) + '\n')
        result_file.close()

def gui()->None:
    print("""
  ___          _ _             ___                     _           
 / __|_ __ _ _(_) |_ ___ ___  / __|___ _ ___ _____ _ _| |_ ___ _ _ 
 \__ \ '_ \ '_| |  _/ -_|_-< | (__/ _ \ ' \ V / -_) '_|  _/ -_) '_|
 |___/ .__/_| |_|\__\___/__/  \___\___/_||_\_/\___|_|  \__\___|_|  
     |_|                                                           
  - An Ayabusa software
      
What would you like to do?
    [1] Convert all sprites and print them
    [2] Convert all sprites and save them to file (sprites_converted.txt)
    [other] Quit/Cancel""")
    save_to_file = False
    compress_sprites = True
    path = "./src/sprites/"

    choice = input("Your choice [1]: ")
    if choice == "1" or choice == "":
        save_to_file = False
    elif choice == "2":
        save_to_file = True
    else:
        print("Invalid input exiting the program.")
        exit()

    choice = input("Where are your sprites located ? [./src/sprites/]: ")
    if choice != "":
        path = choice

    choice = input("Would you like to compress the spites ? (Y/N) [Y]: ")
    if choice == "Y" or choice == "":
        compress_sprites = True
    elif choice == "N":
        compress_sprites = False
    else:
        print("Invalid input exiting the program.")
        exit()
    print("Convertion started ...\n")
    convert_all_files(save_to_file, compress_sprites, path)
    print("Convertion finished ...")

# Launch the text UI
gui()