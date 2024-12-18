from kandinsky import *
import ion, time

print("Game started")
colors = [color(i) for i in [(26,28,44),(93,39,93),(177,62,83),(239,125,87),(255,205,117),(167,240,112),(56,183,100),(37,113,121),(41,54,111),(59,93,201),(65,166,246),(115,239,247),(244,244,244),(148,176,194),(86,108,134),(51,60,87)]]
sprites ={'assiette': (0, 2, 20, 17,
              'ggggggg000000gggggggggggg00cccccc00gggggggg00cccccccccc00ggggg0cccccccccccccc0ggg0cccccddddddccccc0gg0ccccdccccccdcccc0g0ccccdccccccccdcccc00cccdccccccccccdccd00cccdcccccccccccccd00dccdcccccccccccccd00dcccdccccccccccccd0g0dcccccddcccccccd0gg0dccccccccccccccd0ggg0ddccccccccccdd0ggggg00ddccccccdd00gggggggg00dddddd00gggggggggggg000000ggggggg'),
 'caisse': (0, 0, 20, 20,
            'gg0000000000000000ggg0c0ccccccccccdcdd0g0ccd0ddcccddcdddddc000cdd0cccddcdddddcc00c0de0000000000dccc00cd00eeedddd0dd0ccc00cdc0eddddd0ddd0ccd00ccc0edddd0ccd00cde00ccc0dddd0cdd0e0dee00ccd0ddd0ddd0ed0eed00cdd0dd0ddd0edd0edd00ddc0d0cdd0eddd0dde00ccd00cdd0eeddd0dee00cdd0cdd0eedddd0eee00ddd0dd0eeddddd00ee00ddde0000000000cd0e00dddccccdeecce0ccd000ddccccdeeddeee0dde0g0ccccdeeddeeeee0d0ggg0000000000000000gg'),
 'oignon': (3, 3, 16, 13,
            'ggggggggggg00ggggggg00000g0650ggggg021122016650ggg0111c111210660g0211c111210g0500211cc11111200500211c11211110g0g012c112111110ggg012c111112120gggg01121112110gggg01221112110gggggg010122110gggggggg0g00000ggggggg'),
 'oignon_coupe': (3, 5, 13, 14,
                  'gggggg00000ggggg000ccccc0ggg0cccc000c0gg0c00c100g0c00c0g0c1cc00c00c00g0c11cc1001cc00ccc110gg011cc1000c0ggg0011c0g0c0ggggg00c00g0c0ggggg01cc00c0gggggg011cc10ggggggg00110gggggggggg00gg'),
 'pain': (2, 4, 17, 14,
          'ggggg0000000ggggggg0004444444000ggg04cc44443444330g0444444344444433004443444443444330043444444444443300444444444433333004433443333333330g000033333330000g0033300000003330004444333344444330g044344444433330ggg0004343333000ggggggg0000000ggggg'),
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
                  'gggg0000000ggggg0055765567000g077755555556770g0655655555560g075566566565550g5666656655760g050705576750700g0g0g070606g0gggggggg0g0g0gggg'),
 'steak': (3, 3, 14, 14,
           'ggg0000000gggggg033322cc0gggg0cc222d2c20gg032d22cc2c220g0322d2c222c0gg022d2c22220gggg0c22cd220ggggg022222d20gggggg0222d2d20gggggg02d2d2220gggggg0c2c222c0gggggg0cc22d220gggggg00cc2220gggggggg00000g'),
 'steak_cuit': (3, 5, 15, 9,
                'gggg0000000ggggg0000223320000g003323332333200033233322333330032333233323320023332333233220022222333222220g0002222222000ggggg0000000gggg')}

key_pressed = [False]*5

maps = [[[2, 2, 2, 3, 3, 2, 2, 2], [2, 1, 1, 1, 1, 1, 1, 4], [6, 0, 0, 4, 9, 0, 0, 5], [7, 0, 0, 2, 8, 0, 0, 2], [1, 0, 0, 1, 1, 0, 0, 1]]]

class Ingredient:
    def __init__(self, i_nom):
        self.i_nom = i_nom

class Plat:
    def __init__(self, p_type, p_ingredients):
        self.p_type=p_type
        self.p_ingredients=p_ingredients

class Player:
    def __init__(self, game: object, x:int, y:int) -> None:
        self.x = x
        self.y = y
        self.game = game
        self.direction = "down"
        self.holding=Ingredient("salade")
    def draw_player(self)->None:
        self.game.draw_sprite("player_"+self.direction, self.x*40, self.y*40+40, 2)
        if self.holding != None:
            self.game.draw_sprite(self.holding.i_nom, self.x*40+10, self.y*40+60)
    def move(self, x_mod: int, y_mod: int)->None:
        el = maps[game.mapid][self.y][self.x]
        self.game.draw_element(el, self.x, self.y)
        new_el=maps[self.game.mapid][self.y+y_mod][self.x+x_mod]
        if self.y+y_mod<4 and new_el in [0,1]:
            self.y+=y_mod
            self.x+=x_mod
        self.draw_player()
    def do_pickup_action(self)->None:
        dir,el,elx,ely=self.direction,None,None,None
        if dir=="up": el,elx,ely=self.game.map[self.y-1][self.x],self.x,self.y-1
        elif dir=="down": el,elx,ely=self.game.map[self.y+1][self.x],self.x,self.y+1
        elif dir=="left": el,elx,ely=self.game.map[self.y][self.x-1],self.x-1,self.y
        else: el,elx,ely=self.game.map[self.y][self.x+1],self.x+1,self.y
        if self.holding != None:
            el = (el,self.holding.i_nom)
            self.game.map[ely][elx]=el
            game.draw_element(el, elx, ely)
            self.holding = None
            self.draw_player()
        else:
            self.holding = self.game.recup_ingredient(elx,ely)
            self.draw_player()

class Game:
    def __init__(self, mapid:int):
        self.mapid = mapid
        self.map = maps[mapid]
        self.player = Player(self, 1,1)
    def scan_keyboard(self):
        if ion.keydown(ion.KEY_OK) or ion.keydown(ion.KEY_HOME):
            self.player.do_pickup_action()
            time.sleep(0.1)
        elif ion.keydown(ion.KEY_TOOLBOX) or ion.keydown(ion.KEY_POWER):
            print("hello")
            time.sleep(0.1)
        elif ion.keydown(ion.KEY_UP):
            self.player.direction="up"
            self.player.move(0,-1)
            time.sleep(0.1)
        elif ion.keydown(ion.KEY_DOWN):
            self.player.direction="down"
            self.player.move(0,1)
            time.sleep(0.1)
        elif ion.keydown(ion.KEY_LEFT):
            self.player.direction="left"
            self.player.move(-1,0)
            time.sleep(0.1)
        elif ion.keydown(ion.KEY_RIGHT):
            self.player.direction="right"
            self.player.move(1,0)
            time.sleep(0.1)
    def render_all(self):
        """Render literraly everything, this should not be called too many times"""
        self.draw_map(self.mapid)
        self.player.draw_player()
    def draw_element(self, element, x:int, y:int)->None:
        el=element
        if type(el)==tuple: el=el[0]
        if el==0:
            fill_rect(x*40, y*40+40, 40, 40, colors[14])
        elif el==1:
            fill_rect(x*40, y*40+40, 40, 4, colors[3])
            fill_rect(x*40, y*40+40+4, 40, 2, colors[1])
            fill_rect(x*40, y*40+40+6, 40, 8, colors[2])
            fill_rect(x*40, y*40+40+14, 40, 12, colors[15])
            fill_rect(x*40, y*40+40+26, 40, 14, colors[14])
        elif el==2:
            fill_rect(x*40, y*40+40, 40, 40, colors[4])
        elif el==3:
            fill_rect(x*40, y*40+40, 40, 40, colors[4])
            game.draw_sprite("poele", x*40, y*40+40, 2)
        elif el==4:
            fill_rect(x*40, y*40+40, 40, 40, colors[4])
            game.draw_sprite("planche", x*40, y*40+40, 2)
        elif el==5:
            fill_rect(x*40, y*40+40, 40, 40, colors[4])
            game.draw_sprite("assiette", x*40, y*40+42, 2)
            game.draw_sprite("assiette", x*40, y*40+38, 2)
            game.draw_sprite("assiette", x*40, y*40+34, 2)
        elif el==6:
            fill_rect(x*40, y*40+40, 40, 40, colors[4])
            game.draw_sprite("caisse", x*40, y*40+40, 2)
            game.draw_sprite("oignon", x*40, y*40+40, 2)
        elif el==7:
            fill_rect(x*40, y*40+40, 40, 40, colors[4])
            game.draw_sprite("caisse", x*40, y*40+40, 2)
            game.draw_sprite("salade", x*40, y*40+40, 2)
        elif el==8:
            fill_rect(x*40, y*40+40, 40, 40, colors[4])
            game.draw_sprite("caisse", x*40, y*40+40, 2)
            game.draw_sprite("steak", x*40, y*40+40, 2)
        elif el==9:
            fill_rect(x*40, y*40+40, 40, 40, colors[4])
            game.draw_sprite("caisse", x*40, y*40+40, 2)
            game.draw_sprite("pain", x*40, y*40+40, 2)
        if type(element)==tuple: 
            game.draw_sprite(element[1], x*40, y*40+40, 2)

    def draw_map(self, mapid: int):
            for l in range(5):
                for c in range(8):
                    el = self.map[l][c]
                    self.draw_element(el, c, l)
    def draw_sprite(self, sprite_name: str, x: int, y: int, multiplier=1)->None:
        if sprite_name not in sprites: raise ValueError('Sprite name not in sprites')
        offx, offy, w, h, data = sprites[sprite_name]
        curx, cury = 0,0
        for i in range(h):
            for k in range(w):
                px = int(data[w*i+k], 18)
                if px != 16 and px != 17:
                    fill_rect(x+offx+curx*multiplier,y+offy+cury*multiplier,multiplier,multiplier,colors[px])
                curx += 1
            curx=0
            cury+=1
    def recup_ingredient(self, elx:int,ely:int)->Ingredient:
        el=self.map[ely][elx]
        if type(el)!=tuple: 
            if el==6: return Ingredient("oignon")
            elif el==7: return Ingredient("salade")
            elif el==8: return Ingredient("steak")
            elif el==9: return Ingredient("pain")
            return None
        if el[0]==2:
            print("element picked")
            self.map[ely][elx]=2
            self.draw_element(2,elx,ely)
            return Ingredient(el[1])
        else:
            print("element not pickable")
            return None

game = Game(0)
game.render_all()
while True:
    game.scan_keyboard()