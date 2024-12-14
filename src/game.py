from kandinsky import *

print("Game started")
colors = [color(i) for i in [(26,28,44),(93,39,93),(177,62,83),(239,125,87),(255,205,117),(167,240,112),(56,183,100),(37,113,121),(41,54,111),(59,93,201),(65,166,246),(115,239,247),(244,244,244),(148,176,194),(86,108,134),(51,60,87)]]
sprites = {}

class Ingredient:
    def __init__(self, i_nom):
        self.i_nom = i_nom
        self.i_sprite = sprites[i_nom]

class Plat:
    def __init__(self, p_type, p_ingredients):
        self.p_type = p_type
        self.p_ingredients = p_ingredients

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