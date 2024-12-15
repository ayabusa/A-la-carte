from kandinsky import *

print("Game started")
colors = [color(i) for i in [(26,28,44),(93,39,93),(177,62,83),(239,125,87),(255,205,117),(167,240,112),(56,183,100),(37,113,121),(41,54,111),(59,93,201),(65,166,246),(115,239,247),(244,244,244),(148,176,194),(86,108,134),(51,60,87)]]
sprites = {'assiette': (0, 2, 20, 17,
              'ggggggg000000gggggggggggg00cccccc00gggggggg00cccccccccc00ggggg0cccccccccccccc0ggg0cccccddddddccccc0gg0ccccdccccccdcccc0g0ccccdccccccccdcccc00cccdccccccccccdccd00cccdcccccccccccccd00dccdcccccccccccccd00dcccdccccccccccccd0g0dcccccddcccccccd0gg0dccccccccccccccd0ggg0ddccccccccccdd0ggggg00ddccccccdd00gggggggg00dddddd00gggggggggggg000000ggggggg'),
 'oignon': (3, 3, 16, 13,
            'ggggggggggg00ggggggg00000g0650ggggg021122016650ggg0111c111210660g0211c111210g0500211cc11111200500211c11211110g0g012c112111110ggg012c111112120gggg01121112110gggg01221112110gggggg010122110gggggggg0g00000ggggggg'),
 'oignon_coupe': (3, 5, 13, 14,
                  'gggggg00000ggggg000ccccc0ggg0cccc000c0gg0c00c100g0c00c0g0c1cc00c00c00g0c11cc1001cc00ccc110gg011cc1000c0ggg0011c0g0c0ggggg00c00g0c0ggggg01cc00c0gggggg011cc10ggggggg00110gggggggggg00gg'),
 'planche': (0, 5, 20, 14,
             'ggggg00000000000000ggggg0333333333333330g00g0333003333333330033003320c0333323330033333330cd022233330032333330ddc023333300332233330ddd033333002200333330ddd033330g00g03333330ddf03330gggg022222220fdf0220ggggg00000000ffff00gggggggggggggg00fdf0gggggggggggggggg0ff0ggggggggggggggggg00gg'),
 'player_down': (3, 0, 15, 20,
                 'gg00000000000ggg0ccc0ccc0ccc0g0ccc0ccccc0ccc00ccc0ccccc0ccc00ccc0ccccc0ccc0g0ccc0ccc0ccc0ggg000000cc000gggg0ccccccccc0gggg00000000000ggggg04c848c40gggggg044444440ggggggg0000000ggggggg0cccdccc0ggggg0cccccdccc0gggg0c0cfcdc0c0gggg0c0cccdc0c0gggg000cfcdc000gggggg0cccdc0gggggggg0000000ggggggggg00g00ggggg'),
 'player_left': (3, 0, 15, 20,
                 'gg00000000000ggg0ccc0ccc0ccc0g0ccc0ccccc0ccc00ccc0ccccc0ccc00ccc0ccccc0ccc0g0ccc0ccc0ccc0ggg000000cc000gggg0ccccccccc0gggg00000000000ggggg08c48c440gggggg044444440ggggggg0000000ggggggg0ccdcccc0ggggg0ccccdcccc0gggg0c0cfcd0cc0gggg0c0cccdc0c0gggg000cfcdc000gggggg0cccdc0gggggggg0000000ggggggg000gg000gggg'),
 'player_right': (2, 0, 15, 20,
                  'gg00000000000ggg0ccc0ccc0ccc0g0ccc0ccccc0ccc00ccc0ccccc0ccc00ccc0ccccc0ccc0g0ccc0ccc0ccc0ggg000cc000000gggg0ccccccccc0gggg00000000000ggggg044c84c80gggggg044444440ggggggg0000000ggggggg0ccccdcc0ggggg0ccccdcccc0gggg0cc0dcfc0c0gggg0c0cdccc0c0gggg000cdcfc000gggggg0cdccc0gggggggg0000000gggggggg000gg000ggg'),
 'player_up': (3, 0, 15, 20,
               'gg00000000000ggg0ccc0ccc0ccc0g0ccc0ccccc0ccc00ccc0ccccc0ccc00ccc0ccccc0ccc0g0ccc0ccc0ccc0ggg000000cc000gggg0ccccccccc0gggg00000000000ggggg044444440gggggg044444440ggggggg0000000ggggggg0ccccccc0ggggg0ccccccccc0gggg0c0ccccc0c0gggg0c0ccccc0c0gggg000ccccc000gggggg0ccccc0gggggggg0000000ggggggggg00g00ggggg'),
 'poele': (0, 0, 19, 19,
           'gggggg00000000gggggggg000eeeeeeee000gggg0eeeffffffffeee0gg0eeffeeeeeeeeffee0g0efeeeeeeeeeeeefe0g0efeeeeeeeeeeeefe0g0eeeeeeeeeeeeeeee0g00eeeeeeeeeeeeee00g0b0000eeeeee0000f0g000fff000000ffff00g00fffffffffff000f0g0ff0000000000baf0g0ff0fabfffbafffba0g0f0ffbff2f3b3ffff0gg0fff0ffffffff0fff0g0fff0000000000fff0g0fff0gggggggg0fff0g0ff0gggggggggg0ff0gg00gggggggggggg00g'),
 'salade': (1, 4, 18, 13,
            'gggggggggggg0gggggggggg0000g0070gggggggg07777077570ggggg00755567567570ggg077567777777570gg07657765655767770g077776556556755770000076556556767070ggg075556555670g00ggg075556555670gggggg07665655670gggggggg077777770gggggggggg0000000gggggg'),
 'salade_cuite': (2, 7, 15, 9,
                  'gggg0000000ggggg0055765567000g077755555556770g0655655555560g075566566565550g5666656655760g050705576750700g0g0g070606g0gggggggg0g0g0gggg')}

class Ingredient:
    def __init__(self, i_nom):
        self.i_nom = i_nom
        self.i_sprite = sprites[i_nom]

class Plat:
    def __init__(self, p_type, p_ingredients):
        self.p_type = p_type
        self.p_ingredients = p_ingredients

def draw_sprite(sprite_name: str, x: int, y: int, multiplier=1)->None:
    if sprite_name not in sprites: raise ValueError('Sprite name not in sprites')
    offx, offy, w, h, data = sprites[sprite_name]
    curx, cury = x+offx, y+offy
    for i in range(h):
        for k in range(w):
            px = int(data[w*i+k], 18)
            if px != 16 and px != 17:
                fill_rect(curx*multiplier,cury*multiplier,multiplier,multiplier,colors[px])
            curx += 1
        curx=x+offx
        cury+=1


def draw_map(mapid: int):
    if mapid==0:
        fill_rect(0,40,320,182,colors[4]) # table
        fill_rect(40,80,240,4,colors[3])
        fill_rect(40,84,240,2,colors[1])
        fill_rect(40,86,240,8,colors[2])
        fill_rect(40,94,240,12,colors[15])
        fill_rect(40,106,240,116,colors[14]) # sol
        fill_rect(120,120,80,80,colors[4]) # table 2
        fill_rect(120,200,80,4,colors[3])
        fill_rect(122,204,76,2,colors[1])
        fill_rect(122,206,76,8,colors[2])
        fill_rect(122,214,76,8,colors[15])

draw_map(0)
draw_sprite("player_up", 0, 0, 2)