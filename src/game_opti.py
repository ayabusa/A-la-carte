_S='poubelle'
_R='planche'
_Q='pain_haut'
_P='pain_bas'
_O='gui_art'
_N='down'
_M=True
_L=None
_K='tomate'
_J='steak'
_I='oignon'
_H='assiette'
_G='steak_cuit'
_F='salade'
_E='caisse'
_D='pain'
_C='tomate_coupe'
_B='salade_cuite'
_A='oignon_coupe'
try:
	import os
	if hasattr(os,'environ'):os.environ['KANDINSKY_OS_MODE']='0';os.environ['KANDINSKY_ZOOM_RATIO']='4'
except:pass
from kandinsky import*
import ion,time,random
print('Game started')
colors=[color(i)for i in[(26,28,44),(93,39,93),(177,62,83),(239,125,87),(255,205,117),(167,240,112),(56,183,100),(37,113,121),(41,54,111),(59,93,201),(65,166,246),(115,239,247),(244,244,244),(148,176,194),(86,108,134),(51,60,87)]]
sprites={_H:(0,3,20,17,'ggggggg000000gggggggggggg00cccccc00gggggggg00cccccccccc00ggggg0cccccccccccccc0ggg0cccccddddddccccc0gg0ccccdccccccdcccc0g0ccccdccccccccdcccc00cccdccccccccccdccd00cccdcccccccccccccd00dccdcccccccccccccd00dcccdccccccccccccd0g0dcccccddcccccccd0gg0dccccccccccccccd0ggg0ddccccccccccdd0ggggg00ddccccccdd00gggggggg00dddddd00gggggggggggg000000ggggggg'),_E:(0,0,20,20,'gg0000000000000000ggg0c0ccccccccccdcdd0g0ccd0ddcccddcdddddc000cdd0cccddcdddddcc00c0de0000000000dccc00cd00eeedddd0dd0ccc00cdc0eddddd0ddd0ccd00ccc0edddd0ccd00cde00ccc0dddd0cdd0e0dee00ccd0ddd0ddd0ed0eed00cdd0dd0ddd0edd0edd00ddc0d0cdd0eddd0dde00ccd00cdd0eeddd0dee00cdd0cdd0eedddd0eee00ddd0dd0eeddddd00ee00ddde0000000000cd0e00dddccccdeecce0ccd000ddccccdeeddeee0dde0g0ccccdeeddeeeee0d0ggg0000000000000000gg'),_O:(0,0,56,55,'ggggggggggggg0cccccccccd0cccccccddd0cccc00gggggggggggggggggggggggggg0cccccccccd0cccccccccdd0cccccd0ggggggggggggggggggggggggg0ccccccccd0ccccccccccdd0cccccd0ggggggggggggggggggggggggg0ccccccccd0ccccccccccddd0ccccdd0ggggggggggggggggggggggg0ccccccccd0ccccccccccccdd0ccdccd0ggggggggggggggggggggggg0ccccccccd0ccccccccccccdd0ccdccdd0gggggggggggggggggggggg0ccccccccd0ccccccccccccdd0cccdcdd0gggggggggggggggggggggg0cccccccd0cccccccccccccdd0cccdcdd0gggggggggggggggggggggg0cccccccd0cccccccccccccdd0cccccdd0gggggggggggggggggggggg0cccccccd0ccccccccccccdd0cccccddd0gggggggggggggggggggggg0cccccccd0ccccccccccccdd0cccccdd0gggggggggggggggggggggg0cccccccd0cccccccccccccd0cccccddd0gggggggggggggggggggggg0cccccccd0ccccccccccccdd0ccccddd0ggggggggggggggggggggggg0cccccccd0cccccccccccdd0cccccdd0gggggggggggggggggggggggg0cccccccd0ccccccccccdd0cccccdd0ggggggggggggggggggggggggg0ddccccd0ccccccccccdd0cccccdd0gggggggggggggggggggggggggg000dddcd0cccccccccdd0cccccdd0gggggggggggggggggggggggggg0ccc000ddcccccccccdd0cccccdd0ggggggggggggggggggggggggggg0ddcccc00ddccccccdd0cccccdd0gggggggggggggggggggggggggggg000ddcccc00dddccc00cccccdd0gggggggggggggggggggggggggggg043300dddccc000dddccccccdd0gggggggggggggggggggggggggggg0044433000ddcccc000ddcccdd0ggggggggggggggggggggggggggggg044444433300ddccccc00dddd0gggggggggggggggggggggggggggggg04444000443300dddcccd00d0gggggggggggggggggggggggggggggg044440444044433000dddddd0ggggggggggggggggggggggggggggggg04444044004444433300dddd0ggggggggggggggggggggggggggggggg0444444400444400043300d0ggggggggggggggggggggggggggggggg044044440044440044044330gggggggggggggggggggggggggggggggg04404444444444004404330ggggggggggggggggggggggggggggggggg04404444444440044404330ggggggggggggggggggggggggggggggggg0444044444444444444330ggggggggggggg0000000ggggggggggggggg044400444444444444330gggggggggg0004444444000ggggggggggggg0044400444444444330gggggggggg04cc44443444330gggggggggggggg00444000444440330ggggggggg04444443444444330gggggggggggggg004444400440330gggggggggg04443444443444330gggggggggggggg040044444433330gggggggggg04344444444444330ggggggggggggg0c0330000033300ggggggggggg04444444444333330gggggggg000g0ccc00330gg000ggggggggggggg04433443333333330ggggggg0ccc0c0cccc00gggggggggggggggggggg000033333330000fggggg00ccccccc0ccccc000ggggggggggggggggg0222000000022200gggg0cccccccccc0ccccccc0ggggggggggggggg0000022222220000c0gggcccddccccccc0ccccccc0ggggggggggggg0c056600000007600cd0ggcddd00ccccccc0ccccccc0ggggggggggg0c00507055767507040cd0gdd00g0cccc0dc0cccccccc0ggggggggg00c04030307060630330cd0gd0ggg0cccccc0dcc0ddcccc0gggg0000c0dc044344040303330ccd0g0gggg0cccccc0dcd000ddccd0000ccccd0dcc0004343333000cccd0ggggg0ccccccc0ccd0gg00dccccccccccdd0dcccc0000000cccccd0gggggg0cccc0d0dccd0gggg00dccccccc00000dddccccccccccddd0ggggggg0cccccc0dcdd0gggggg0dccc000ggggg000dddddddddd000ggggggg0ccccccc0ccd0gggggggg0000ggggggggggg0000000000gggggggggg0cccccc0dcdd0ggggggggggggggggggggggggggggggggggggggggggg0cccc0d0cddd0gggggggggggggggggggggggggggggggggggggggggg0ccccccc0cdd0ggggggggggggggggggggggggggggggggggggggggggg0cccccc0dcdd0ggggggggggggggggggggggggggggggggggggggggggg0cccc0d0cddd0ggggggggggggggggggggggggggggggggggggggggg'),_I:(3,3,16,13,'ggggggggggg00ggggggg00000g0650ggggg021122016650ggg0111c111210660g0211c111210g0500211cc11111200500211c11211110g0g012c112111110ggg012c111112120gggg01121112110gggg01221112110gggggg010122110gggggggg0g00000ggggggg'),_A:(3,5,13,14,'gggggg00000ggggg000ccccc0ggg0cccc000c0gg0c00c100g0c00c0g0c1cc00c00c00g0c11cc1001cc00ccc110gg011cc1000c0ggg0011c0g0c0ggggg00c00g0c0ggggg01cc00c0gggggg011cc10ggggggg00110gggggggggg00gg'),_D:(2,4,17,14,'ggggg0000000ggggggg0004444444000ggg04cc44443444330g0444444344444433004443444443444330043444444444443300444444444433333004433443333333330g000033333330000g0033300000003330004444333344444330g044344444433330ggg0004343333000ggggggg0000000ggggg'),_P:(2,12,17,5,'00333ggggggg3330004444333344444330g044344444433330ggg0004343333000ggggggg0000000ggggg'),_Q:(2,0,17,10,'ggggg0000000ggggggg0004444444000ggg04cc44443444330g0444444344444433004443444443444330043444444444443300444444444433333004433443333333330g000033333330000gggggg0000000ggggg'),_R:(0,5,20,14,'ggggg00000000000000ggggg0333333333333330g00g0333003333333330033003320c0333323330033333330cd022233330032333330ddc023333300332233330ddd033333002200333330ddd033330g00g03333330ddf03330gggg022222220fdf0220ggggg00000000ffff00gggggggggggggg00fdf0gggggggggggggggg0ff0ggggggggggggggggg00gg'),'player_down':(3,0,15,20,'gg00000000000ggg0ccc0ccc0ccc0g0ccc0ccccc0ccc00ccc0ccccc0ccc00ccc0ccccc0ccc0g0ccc0ccc0ccc0ggg000000cc000gggg0ccccccccc0gggg00000000000ggggg04c848c40gggggg044444440ggggggg0000000ggggggg0cccdccc0ggggg0cccccdccc0gggg0c0cfcdc0c0gggg0c0cccdc0c0gggg000cfcdc000gggggg0cccdc0gggggggg0000000ggggggggg00g00ggggg'),'player_left':(3,0,15,20,'gg00000000000ggg0ccc0ccc0ccc0g0ccc0ccccc0ccc00ccc0ccccc0ccc00ccc0ccccc0ccc0g0ccc0ccc0ccc0ggg000000cc000gggg0ccccccccc0gggg00000000000ggggg08c48c440gggggg044444440ggggggg0000000ggggggg0ccdcccc0ggggg0ccccdcccc0gggg0c0cfcd0cc0gggg0c0cccdc0c0gggg000cfcdc000gggggg0cccdc0gggggggg0000000ggggggg000gg000gggg'),'player_right':(2,0,15,20,'gg00000000000ggg0ccc0ccc0ccc0g0ccc0ccccc0ccc00ccc0ccccc0ccc00ccc0ccccc0ccc0g0ccc0ccc0ccc0ggg000cc000000gggg0ccccccccc0gggg00000000000ggggg044c84c80gggggg044444440ggggggg0000000ggggggg0ccccdcc0ggggg0ccccdcccc0gggg0cc0dcfc0c0gggg0c0cdccc0c0gggg000cdcfc000gggggg0cdccc0gggggggg0000000gggggggg000gg000ggg'),'player_up':(3,0,15,20,'gg00000000000ggg0ccc0ccc0ccc0g0ccc0ccccc0ccc00ccc0ccccc0ccc00ccc0ccccc0ccc0g0ccc0ccc0ccc0ggg000000cc000gggg0ccccccccc0gggg00000000000ggggg044444440gggggg044444440ggggggg0000000ggggggg0ccccccc0ggggg0ccccccccc0gggg0c0ccccc0c0gggg0c0ccccc0c0gggg000ccccc000gggggg0ccccc0gggggggg0000000ggggggggg00g00ggggg'),'poele':(0,0,19,19,'gggggg00000000gggggggg000eeeeeeee000gggg0eeeffffffffeee0gg0eeffeeeeeeeeffee0g0efeeeeeeeeeeeefe0g0efeeeeeeeeeeeefe0g0eeeeeeeeeeeeeeee0g00eeeeeeeeeeeeee00g0b0000eeeeee0000f0g000fff000000ffff00g00fffffffffff000f0g0ff0000000000baf0g0ff0fabfffbafffba0g0f0ffbff2f3b3ffff0gg0fff0ffffffff0fff0g0fff0000000000fff0g0fff0gggggggg0fff0g0ff0gggggggggg0ff0gg00gggggggggggg00g'),_S:(0,0,20,20,'ggggg0000000000ggggggggg0ffffffffff0ggggggg0fffffffffffe0ggggg0ffffffffffffef0ggg0fffefffffffffeff0g0ffffefff66f6ffffff00ffffeff6ff66ffefff00ffffeffff666ffffff00ffffef6fffffffffff00ffffe666ff6f6fefff00ffffef6ff666ffefff00ffffeff6ff6fffefff00ffffefffffffffefff00ffffffffffffffffff00ffffeeeeeeeeeeffff00fffeffffffffffefff00ffefff000000fffeff00fefff00000000fffef0g0fff0000000000fffeggg0000000000000000gg'),_F:(1,4,18,13,'gggggggggggg0gggggggggg0000g0070gggggggg07777077570ggggg00755567567570ggg077567777777570gg07657765655767770g077776556556755770000076556556767070ggg075556555670g00ggg075556555670gggggg07665655670gggggggg077777770gggggggggg0000000gggggg'),_B:(2,7,15,9,'gggg0000000ggggg0055765567000g077755555556770g0655655555560g075566566565550g5666656655760g050705576750700g0g0g070606g0gggggggg0g0g0gggg'),_J:(3,3,14,14,'ggg0000000gggggg033322cc0gggg0cc222d2c20gg032d22cc2c220g0322d2c222c0gg022d2c22220gggg0c22cd220ggggg022222d20gggggg0222d2d20gggggg02d2d2220gggggg0c2c222c0gggggg0cc22d220gggggg00cc2220gggggggg00000g'),_G:(3,5,15,9,'gggg0000000ggggg0000223320000g003323332333200033233322333330032333233323320023332333233220022222333222220g0002222222000ggggg0000000gggg'),'tapis':(0,0,20,20,'feeeeeffffffffeeeeefffeeeeeffffffeeeeefffffeeeeeffffeeeeefffffffeeeeeffeeeeefffffffffeeeeeeeeeefffffefffffeeeeeeeefffffeeefffffeeeeeefffffeeeeefffffeeeefffffeeeeeeefffffeefffffeeeeeeeeeffffffffffeeeeefeeeeeffffffffeeeeefffeeeeeffffffeeeeefffffeeeeeffffeeeeefffffffeeeeeffeeeeefffffffffeeeeeeeeeefffffefffffeeeeeeeefffffeeefffffeeeeeefffffeeeeefffffeeeefffffeeeeeeefffffeefffffeeeeeeeeeffffffffffeeeee'),_K:(4,3,12,13,'ggggggg0gggggggg0g060gggggg060700ggggg02277220ggg0276767220g026226227220022c22722120022cc222221002222c222110g0222222210gg0222221110ggg00111100gggggg0000gggg'),_C:(3,4,13,11,'gggggg000ggggggggg02220ggggggg0233220gggggg02434220ggg00233433220g022224344320022334223320g02334320220gg0223442000gggg0222220ggggggg00000gggggg')}
key_pressed=[False]*5
maps=[[[2,2,2,3,3,2,11,2],[12,1,1,1,1,1,1,4],[6,0,0,4,9,0,0,5],[7,0,0,2,8,0,0,2],[1,0,0,1,1,13,13,1]]]
def draw_sprite(sprite_name,x,y,multiplier=1):
	if sprite_name not in sprites:raise ValueError('Sprite name not in sprites')
	offx,offy,w,h,data=sprites[sprite_name];curx,cury=0,0
	for i in range(h):
		for k in range(w):
			px=int(data[w*i+k],18)
			if px!=16 and px!=17:fill_rect(x+offx*multiplier+curx*multiplier,y+offy*multiplier+cury*multiplier,multiplier,multiplier,colors[px])
			curx+=1
		curx=0;cury+=1
class Ingredient:
	def __init__(self,i_nom):self.i_nom=i_nom
class Assiette:
	def __init__(self):self.a_ingredients=[]
	def render(self,x,y,multiplier):
		draw_sprite(_H,x,y,multiplier)
		if self.a_ingredients==[]:return
		if _D in self.a_ingredients:draw_sprite(_P,x,y,multiplier)
		if _B in self.a_ingredients:draw_sprite(_B,x+multiplier,y-multiplier,multiplier)
		if _G in self.a_ingredients:draw_sprite(_G,x,y-2*multiplier,multiplier)
		if _A in self.a_ingredients:draw_sprite(_A,x+multiplier,y-4*multiplier,multiplier)
		if _C in self.a_ingredients:draw_sprite(_C,x-2*multiplier,y-multiplier,multiplier)
		if _D in self.a_ingredients:draw_sprite(_Q,x,y,multiplier)
class Mission:
	def __init__(self):
		self.m_ingredients=[_D,_G];self.m_time=time.monotonic(),random.randint(40,60)
		if random.getrandbits(1)==1:self.m_ingredients.append(_B)
		if random.getrandbits(1)==1:self.m_ingredients.append(_A)
		if random.getrandbits(1)==1:self.m_ingredients.append(_C)
	def is_finished(self):return time.monotonic()-self.m_time[0]>self.m_time[1]
	def re_render(self,place):offst=place*61;fill_rect(offst+4,26,38,12,colors[3]);draw_string(str(int(self.m_time[1]-(time.monotonic()-self.m_time[0]))//60)+':'+str(int(self.m_time[1]-(time.monotonic()-self.m_time[0]))%60),offst+5,26,colors[12],colors[3],_M);fill_rect(offst+2,26,2,14,colors[0]);fill_rect(offst+4,38,38,2,colors[0]);fill_rect(offst+41,37,2,2,colors[0])
	def first_render(self,place):
		offst=place*61;fill_rect(offst+3,3,27,34,colors[3]);fill_rect(offst+30,3,27,34,colors[3]);fill_rect(offst+3,2,54,2,colors[0]);fill_rect(offst+3,36,54,2,colors[0]);fill_rect(offst+2,3,2,34,colors[0]);fill_rect(offst+56,3,2,34,colors[0]);a=Assiette();a.a_ingredients=self.m_ingredients;a.render(offst+5,5,1)
		if _B in self.m_ingredients:draw_sprite(_B,offst+26,8,1)
		if _A in self.m_ingredients:draw_sprite(_A,offst+39,16,1)
		if _C in self.m_ingredients:draw_sprite(_C,offst+39,1,1)
		draw_string(str(int(self.m_time[1]-(time.monotonic()-self.m_time[0]))//60)+':'+str(int(self.m_time[1]-(time.monotonic()-self.m_time[0]))%60),offst+5,26,colors[12],colors[3],_M);fill_rect(offst+2,26,2,14,colors[0]);fill_rect(offst+4,38,38,2,colors[0]);fill_rect(offst+41,37,2,2,colors[0])
class Player:
	def __init__(self,game,x,y):self.x=x;self.y=y;self.game=game;self.direction=_N;self.holding=Ingredient(_F);assiette=Assiette();assiette.render(0,0,2)
	def draw_player(self):
		draw_sprite('player_'+self.direction,self.x*40,self.y*40+40,2)
		if type(self.holding)==Ingredient:draw_sprite(self.holding.i_nom,self.x*40+10,self.y*40+60)
		elif type(self.holding)==Assiette:self.holding.render(self.x*40+10,self.y*40+60,1)
	def move(self,x_mod,y_mod):
		el=maps[game.mapid][self.y][self.x];self.game.draw_element(el,self.x,self.y);new_el=maps[self.game.mapid][self.y+y_mod][self.x+x_mod]
		if self.y+y_mod<4 and new_el in[0,1]:self.y+=y_mod;self.x+=x_mod
		self.draw_player()
	def do_pickup_action(self):
		dir,el,elx,ely=self.direction,_L,_L,_L
		if dir=='up':el,elx,ely=self.game.map[self.y-1][self.x],self.x,self.y-1
		elif dir==_N:el,elx,ely=self.game.map[self.y+1][self.x],self.x,self.y+1
		elif dir=='left':el,elx,ely=self.game.map[self.y][self.x-1],self.x-1,self.y
		else:el,elx,ely=self.game.map[self.y][self.x+1],self.x+1,self.y
		if self.holding!=_L:self.holding=self.game.poser_ingredient(elx,ely,self.holding);self.draw_player()
		else:self.holding=self.game.recup_ingredient(elx,ely);self.draw_player()
class Game:
	def __init__(self,mapid):self.mapid=mapid;self.map=maps[mapid];self.player=Player(self,1,1);self.missions=[];self.old_missions=[];self.pro_mission=time.monotonic(),3
	def do_mission_step(self):
		if time.monotonic()-self.pro_mission[0]>self.pro_mission[1]:self.missions.append(Mission());self.pro_mission=time.monotonic(),random.randint(20,30)
		for i in range(len(self.missions)):
			if self.missions[i].is_finished():self.missions.pop(i);break
		if self.old_missions!=self.missions:
			fill_rect(0,0,320,40,colors[2]);self.old_missions=[]
			for i in range(len(self.missions)):self.missions[i].first_render(i);self.old_missions.append(self.missions[i])
		else:
			for i in range(len(self.missions)):self.missions[i].re_render(i)
	def do_timer_step(self):
		for i in range(5):
			for k in range(8):
				el=self.map[i][k]
				if type(el)==tuple and len(el)==4:
					if time.monotonic()>el[2]+el[3]:
						if el[1]==_J:self.map[i][k]=el[0],_G
						if el[1]==_F:self.map[i][k]=el[0],_B
						if el[1]==_I:self.map[i][k]=el[0],_A
						if el[1]==_K:self.map[i][k]=el[0],_C
						self.draw_element(self.map[i][k],k,i)
					else:self.draw_progressbar(k,i,(time.monotonic()-el[2])*18//el[3])
	def draw_progressbar(self,x,y,progress):fill_rect(x*40,y*40+40,40,10,colors[0]);fill_rect(x*40+2,y*40+42,36,6,colors[7]);fill_rect(x*40+2,y*40+42,int(progress)*2,6,colors[5])
	def scan_keyboard(self):
		if ion.keydown(ion.KEY_OK)or ion.keydown(ion.KEY_HOME)or ion.keydown(ion.KEY_POWER):self.player.do_pickup_action();time.sleep(.2)
		elif ion.keydown(ion.KEY_UP):self.player.direction='up';self.player.move(0,-1);time.sleep(.1)
		elif ion.keydown(ion.KEY_DOWN):self.player.direction=_N;self.player.move(0,1);time.sleep(.1)
		elif ion.keydown(ion.KEY_LEFT):self.player.direction='left';self.player.move(-1,0);time.sleep(.1)
		elif ion.keydown(ion.KEY_RIGHT):self.player.direction='right';self.player.move(1,0);time.sleep(.1)
	def render_all(self):self.draw_map(self.mapid);self.player.draw_player()
	def draw_element(self,element,x,y):
		el=element
		if type(el)==tuple:el=el[0]
		if el==0:fill_rect(x*40,y*40+40,40,40,colors[14])
		elif el==1:fill_rect(x*40,y*40+40,40,4,colors[3]);fill_rect(x*40,y*40+40+4,40,2,colors[1]);fill_rect(x*40,y*40+40+6,40,8,colors[2]);fill_rect(x*40,y*40+40+14,40,12,colors[15]);fill_rect(x*40,y*40+40+26,40,14,colors[14])
		elif el==2:fill_rect(x*40,y*40+40,40,40,colors[4])
		elif el==3:fill_rect(x*40,y*40+40,40,40,colors[4]);draw_sprite('poele',x*40,y*40+40,2)
		elif el==4:fill_rect(x*40,y*40+40,40,40,colors[4]);draw_sprite(_R,x*40,y*40+40,2)
		elif el==5:fill_rect(x*40,y*40+40,40,40,colors[4]);draw_sprite(_H,x*40,y*40+42,2);draw_sprite(_H,x*40,y*40+38,2);draw_sprite(_H,x*40,y*40+34,2)
		elif el==6:fill_rect(x*40,y*40+40,40,40,colors[4]);draw_sprite(_E,x*40,y*40+40,2);draw_sprite(_I,x*40,y*40+40,2)
		elif el==7:fill_rect(x*40,y*40+40,40,40,colors[4]);draw_sprite(_E,x*40,y*40+40,2);draw_sprite(_F,x*40,y*40+40,2)
		elif el==8:fill_rect(x*40,y*40+40,40,40,colors[4]);draw_sprite(_E,x*40,y*40+40,2);draw_sprite(_J,x*40,y*40+40,2)
		elif el==9:fill_rect(x*40,y*40+40,40,40,colors[4]);draw_sprite(_E,x*40,y*40+40,2);draw_sprite(_D,x*40,y*40+40,2)
		elif el==11:fill_rect(x*40,y*40+40,40,40,colors[4]);draw_sprite(_S,x*40,y*40+40,2)
		elif el==12:fill_rect(x*40,y*40+40,40,40,colors[4]);draw_sprite(_E,x*40,y*40+40,2);draw_sprite(_K,x*40,y*40+40,2)
		elif el==13:draw_sprite('tapis',x*40,y*40+40,2)
		if type(element)==tuple:draw_sprite(element[1],x*40,y*40+40,2)
	def draw_map(self,mapid):
		for l in range(5):
			for c in range(8):el=self.map[l][c];self.draw_element(el,c,l)
	def poser_ingredient(self,elx,ely,holding):
		old_el=self.map[ely][elx]
		if type(old_el)==tuple and type(old_el[1])!=Assiette:return holding
		if type(holding)==Ingredient:
			result=_L;el=old_el,holding.i_nom
			if old_el==11:return
			elif old_el==2:0
			elif old_el==3 and holding.i_nom==_J:el=el[0],el[1],time.monotonic(),8
			elif old_el==4 and(holding.i_nom==_I or holding.i_nom==_F or holding.i_nom==_K):el=el[0],el[1],time.monotonic(),5
			elif type(old_el)==tuple and type(old_el[1])==Assiette:
				n=holding.i_nom
				if n==_B or n==_C or n==_A or n==_D or n==_G:
					if n not in self.map[ely][elx][1].a_ingredients:self.map[ely][elx][1].a_ingredients.append(n);self.map[ely][elx][1].render(elx*40,ely*40+40,2)
					else:return holding
				else:return holding
				return
			else:return holding
			self.map[ely][elx]=el;game.draw_element(el,elx,ely);return result
		elif type(holding)==Assiette:
			if old_el==11:return
			elif old_el==2:self.map[ely][elx]=old_el,holding;holding.render(elx*40,ely*40+40,2);return
			else:return holding
	def recup_ingredient(self,elx,ely):
		el=self.map[ely][elx]
		if type(el)==int:
			if el==5:return Assiette()
			elif el==6:return Ingredient(_I)
			elif el==7:return Ingredient(_F)
			elif el==8:return Ingredient(_J)
			elif el==9:return Ingredient(_D)
			elif el==12:return Ingredient(_K)
			return
		elif type(el[1])==Assiette:self.map[ely][elx]=2;self.draw_element(2,elx,ely);return el[1]
		if el[0]==2:self.map[ely][elx]=2;self.draw_element(2,elx,ely);return Ingredient(el[1])
		elif el[0]==3 or el[0]==4:self.map[ely][elx]=el[0];self.draw_element(el[0],elx,ely);return Ingredient(el[1])
		else:return
class Gui:
	def __init__(self):self.selected=0;self.render()
	def redraw_text(self):
		draw_string('A la carte',200,10,colors[3],colors[15]);but_colors=[colors[4]]*3;but_colors[self.selected]=colors[3];but=['Jouer','Options','Aide']
		for i in range(len(but)):draw_string(but[i],200,40+i*20,but_colors[i],colors[15])
	def render(self):fill_rect(0,0,320,222,colors[15]);draw_sprite(_O,0,0,4);self.redraw_text()
	def loop(self):
		while _M:
			if ion.keydown(ion.KEY_OK)or ion.keydown(ion.KEY_HOME):break
			elif ion.keydown(ion.KEY_UP):self.selected=(self.selected-1)%3;self.redraw_text();time.sleep(.2)
			elif ion.keydown(ion.KEY_DOWN):self.selected=(self.selected+1)%3;self.redraw_text();time.sleep(.2)
		return self.selected
gui=Gui()
gui.loop()
game=Game(0)
game.render_all()
fill_rect(0,0,320,40,colors[2])
while _M:game.scan_keyboard();game.do_timer_step();game.do_mission_step()