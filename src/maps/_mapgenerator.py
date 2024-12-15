from os import listdir
from os.path import isfile, join
import pprint
from PIL import Image

colors_value = {(86,108,134): (0, "sol"),
                (239,125,87): (1, "ombre"),
                (255,205,117): (2, "table"),
                (51,60,87): (3, "poele"),
                (41,54,111): (4, "coupecoupe"),
                (244,244,244): (5, "pile assiettes"),
                (93,39,93): (6, "oignons"),
                (167,240,112): (7, "salade"),
                (177,62,83): (8, "viande")
                }

def get_color_id(r, g, b, a):
    if (r,g,b) not in colors_value: raise ValueError('Could not find color id')
    return colors_value[(r,g,b)][0]

def generate_all_maps(path: str)->None:
    files_list = [f for f in listdir(path) if isfile(join(path, f))]
    final_result = {}
    result_file = open(join(path, "generated_maps.txt"), "w")

    for file in files_list:
        if not file.endswith(".png"):
            print("Skipping", file, ", because it's not a png image.")
            break
        image = Image.open(join(path, file))
        w, h = image.size
        result = []
        for v in range(h):
            line = []
            for k in range(w):
                print('getting pixel:', k, v, image.getpixel((k, v)))
                line.append(get_color_id(*image.getpixel((k, v))))
            result.append(line)
        print('Finished,', file, '\n', result, '\n')
        final_result[file.removesuffix(".png")] = result
        result_file.write(file + "\n" + pprint.pformat(final_result, compact=True) + '\n')
        result_file.close()

def gui()->None:
    print("""
  __  __                 ___                       _           
 |  \/  |__ _ _ __ ___  / __|___ _ _  ___ _ _ __ _| |_ ___ _ _ 
 | |\/| / _` | '_ (_-< | (_ / -_) ' \/ -_) '_/ _` |  _/ _ \ '_|
 |_|  |_\__,_| .__/__/  \___\___|_||_\___|_| \__,_|\__\___/_|  
             |_|                                                                                                        
  - An Ayabusa software
      
""")

    path = "./src/maps/"
    choice = input("Where are your maps located ? [./src/maps/]: ")
    if choice != "":
        path = choice

    print("Convertion started ...\n")
    generate_all_maps(path)
    print("Convertion finished ...")

# Launch the text UI
gui()