_P='alacarte.sav'
_O='time_icon'
_N='poubelle'
_M='planche'
_L='p_haut'
_K='money_icon'
_J='down'
_I=None
_H='assiette'
_G='s_cuit'
_F='sa'
_E='t_c'
_D='sa_cuite'
_C='p'
_B='o_c'
_A=True
try:
	import os
	if hasattr(os,'environ'):os.environ['KANDINSKY_OS_MODE']='0';os.environ['KANDINSKY_ZOOM_RATIO']='4'
except:pass
from kandinsky import*
import ion,time,random as ra
print('G started')
c=[color(i)for i in[(26,28,44),(93,39,93),(177,62,83),(239,125,87),(255,205,117),(167,240,112),(56,183,100),(37,113,121),(41,54,111),(59,93,201),(65,166,246),(115,239,247),(244,244,244),(148,176,194),(86,108,134),(51,60,87)]]
sprites={_H:(0,3,20,17,'ggggggg000000gggggggggggg00cccccc00gggggggg00cccccccccc00ggggg0cccccccccccccc0ggg0cccccddddddccccc0gg0ccccdccccccdcccc0g0ccccdccccccccdcccc00cccdccccccccccdccd00cccdcccccccccccccd00dccdcccccccccccccd00dcccdccccccccccccd0g0dcccccddcccccccd0gg0dccccccccccccccd0ggg0ddccccccccccdd0ggggg00ddccccccdd00gggggggg00dddddd00gggggggggggg000000ggggggg'),'c':(0,0,20,20,'gg0000000000000000ggg0c0ccccccccccdcdd0g0ccd0ddcccddcdddddc000cdd0cccddcdddddcc00c0de0000000000dccc00cd00eeedddd0dd0ccc00cdc0eddddd0ddd0ccd00ccc0edddd0ccd00cde00ccc0dddd0cdd0e0dee00ccd0ddd0ddd0ed0eed00cdd0dd0ddd0edd0edd00ddc0d0cdd0eddd0dde00ccd00cdd0eeddd0dee00cdd0cdd0eedddd0eee00ddd0dd0eeddddd00ee00ddde0000000000cd0e00dddccccdeecce0ccd000ddccccdeeddeee0dde0g0ccccdeeddeeeee0d0ggg0000000000000000gg'),'ga':(0,0,56,55,'ggggggggggggg0cccccccccd0cccccccddd0cccc00gggggggggggggggggggggggggg0cccccccccd0cccccccccdd0cccccd0ggggggggggggggggggggggggg0ccccccccd0ccccccccccdd0cccccd0ggggggggggggggggggggggggg0ccccccccd0ccccccccccddd0ccccdd0ggggggggggggggggggggggg0ccccccccd0ccccccccccccdd0ccdccd0ggggggggggggggggggggggg0ccccccccd0ccccccccccccdd0ccdccdd0gggggggggggggggggggggg0ccccccccd0ccccccccccccdd0cccdcdd0gggggggggggggggggggggg0cccccccd0cccccccccccccdd0cccdcdd0gggggggggggggggggggggg0cccccccd0cccccccccccccdd0cccccdd0gggggggggggggggggggggg0cccccccd0ccccccccccccdd0cccccddd0gggggggggggggggggggggg0cccccccd0ccccccccccccdd0cccccdd0gggggggggggggggggggggg0cccccccd0cccccccccccccd0cccccddd0gggggggggggggggggggggg0cccccccd0ccccccccccccdd0ccccddd0ggggggggggggggggggggggg0cccccccd0cccccccccccdd0cccccdd0gggggggggggggggggggggggg0cccccccd0ccccccccccdd0cccccdd0ggggggggggggggggggggggggg0ddccccd0ccccccccccdd0cccccdd0gggggggggggggggggggggggggg000dddcd0cccccccccdd0cccccdd0gggggggggggggggggggggggggg0ccc000ddcccccccccdd0cccccdd0ggggggggggggggggggggggggggg0ddcccc00ddccccccdd0cccccdd0gggggggggggggggggggggggggggg000ddcccc00dddccc00cccccdd0gggggggggggggggggggggggggggg043300dddccc000dddccccccdd0gggggggggggggggggggggggggggg0044433000ddcccc000ddcccdd0ggggggggggggggggggggggggggggg044444433300ddccccc00dddd0gggggggggggggggggggggggggggggg04444000443300dddcccd00d0gggggggggggggggggggggggggggggg044440444044433000dddddd0ggggggggggggggggggggggggggggggg04444044004444433300dddd0ggggggggggggggggggggggggggggggg0444444400444400043300d0ggggggggggggggggggggggggggggggg044044440044440044044330gggggggggggggggggggggggggggggggg04404444444444004404330ggggggggggggggggggggggggggggggggg04404444444440044404330ggggggggggggggggggggggggggggggggg0444044444444444444330ggggggggggggg0000000ggggggggggggggg044400444444444444330gggggggggg0004444444000ggggggggggggg0044400444444444330gggggggggg04cc44443444330gggggggggggggg00444000444440330ggggggggg04444443444444330gggggggggggggg004444400440330gggggggggg04443444443444330gggggggggggggg040044444433330gggggggggg04344444444444330ggggggggggggg0c0330000033300ggggggggggg04444444444333330gggggggg000g0ccc00330gg000ggggggggggggg04433443333333330ggggggg0ccc0c0cccc00gggggggggggggggggggg000033333330000fggggg00ccccccc0ccccc000ggggggggggggggggg0222000000022200gggg0cccccccccc0ccccccc0ggggggggggggggg0000022222220000c0gggcccddccccccc0ccccccc0ggggggggggggg0c056600000007600cd0ggcddd00ccccccc0ccccccc0ggggggggggg0c00507055767507040cd0gdd00g0cccc0dc0cccccccc0ggggggggg00c04030307060630330cd0gd0ggg0cccccc0dcc0ddcccc0gggg0000c0dc044344040303330ccd0g0gggg0cccccc0dcd000ddccd0000ccccd0dcc0004343333000cccd0ggggg0ccccccc0ccd0gg00dccccccccccdd0dcccc0000000cccccd0gggggg0cccc0d0dccd0gggg00dccccccc00000dddccccccccccddd0ggggggg0cccccc0dcdd0gggggg0dccc000ggggg000dddddddddd000ggggggg0ccccccc0ccd0gggggggg0000ggggggggggg0000000000gggggggggg0cccccc0dcdd0ggggggggggggggggggggggggggggggggggggggggggg0cccc0d0cddd0gggggggggggggggggggggggggggggggggggggggggg0ccccccc0cdd0ggggggggggggggggggggggggggggggggggggggggggg0cccccc0dcdd0ggggggggggggggggggggggggggggggggggggggggggg0cccc0d0cddd0ggggggggggggggggggggggggggggggggggggggggg'),_K:(0,0,8,11,'ggccccgggcggggcgcggggggccggcgggccggcgggccggccggccggccggccggccggccggggggcgcggggcgggccccgg'),'o':(3,3,16,13,'ggggggggggg00ggggggg00000g0650ggggg021122016650ggg0111c111210660g0211c111210g0500211cc11111200500211c11211110g0g012c112111110ggg012c111112120gggg01121112110gggg01221112110gggggg010122110gggggggg0g00000ggggggg'),_B:(3,5,13,14,'gggggg00000ggggg000ccccc0ggg0cccc000c0gg0c00c100g0c00c0g0c1cc00c00c00g0c11cc1001cc00ccc110gg011cc1000c0ggg0011c0g0c0ggggg00c00g0c0ggggg01cc00c0gggggg011cc10ggggggg00110gggggggggg00gg'),_C:(2,4,17,14,'ggggg0000000ggggggg0004444444000ggg04cc44443444330g0444444344444433004443444443444330043444444444443300444444444433333004433443333333330g000033333330000g0033300000003330004444333344444330g044344444433330ggg0004343333000ggggggg0000000ggggg'),'p_bas':(2,12,17,5,'00333ggggggg3330004444333344444330g044344444433330ggg0004343333000ggggggg0000000ggggg'),_L:(2,0,17,10,'ggggg0000000ggggggg0004444444000ggg04cc44443444330g0444444344444433004443444443444330043444444444443300444444444433333004433443333333330g000033333330000gggggg0000000ggggg'),_M:(0,5,20,14,'ggggg00000000000000ggggg0333333333333330g00g0333003333333330033003320c0333323330033333330cd022233330032333330ddc023333300332233330ddd033333002200333330ddd033330g00g03333330ddf03330gggg022222220fdf0220ggggg00000000ffff00gggggggggggggg00fdf0gggggggggggggggg0ff0ggggggggggggggggg00gg'),'pdown':(3,0,15,20,'gg00000000000ggg0ccc0ccc0ccc0g0ccc0ccccc0ccc00ccc0ccccc0ccc00ccc0ccccc0ccc0g0ccc0ccc0ccc0ggg000000cc000gggg0ccccccccc0gggg00000000000ggggg04c848c40gggggg044444440ggggggg0000000ggggggg0cccdccc0ggggg0cccccdccc0gggg0c0cfcdc0c0gggg0c0cccdc0c0gggg000cfcdc000gggggg0cccdc0gggggggg0000000ggggggggg00g00ggggg'),'pleft':(3,0,15,20,'gg00000000000ggg0ccc0ccc0ccc0g0ccc0ccccc0ccc00ccc0ccccc0ccc00ccc0ccccc0ccc0g0ccc0ccc0ccc0ggg000000cc000gggg0ccccccccc0gggg00000000000ggggg08c48c440gggggg044444440ggggggg0000000ggggggg0ccdcccc0ggggg0ccccdcccc0gggg0c0cfcd0cc0gggg0c0cccdc0c0gggg000cfcdc000gggggg0cccdc0gggggggg0000000ggggggg000gg000gggg'),'pright':(2,0,15,20,'gg00000000000ggg0ccc0ccc0ccc0g0ccc0ccccc0ccc00ccc0ccccc0ccc00ccc0ccccc0ccc0g0ccc0ccc0ccc0ggg000cc000000gggg0ccccccccc0gggg00000000000ggggg044c84c80gggggg044444440ggggggg0000000ggggggg0ccccdcc0ggggg0ccccdcccc0gggg0cc0dcfc0c0gggg0c0cdccc0c0gggg000cdcfc000gggggg0cdccc0gggggggg0000000gggggggg000gg000ggg'),'pup':(3,0,15,20,'gg00000000000ggg0ccc0ccc0ccc0g0ccc0ccccc0ccc00ccc0ccccc0ccc00ccc0ccccc0ccc0g0ccc0ccc0ccc0ggg000000cc000gggg0ccccccccc0gggg00000000000ggggg044444440gggggg044444440ggggggg0000000ggggggg0ccccccc0ggggg0ccccccccc0gggg0c0ccccc0c0gggg0c0ccccc0c0gggg000ccccc000gggggg0ccccc0gggggggg0000000ggggggggg00g00ggggg'),'poele':(0,0,19,19,'gggggg00000000gggggggg000eeeeeeee000gggg0eeeffffffffeee0gg0eeffeeeeeeeeffee0g0efeeeeeeeeeeeefe0g0efeeeeeeeeeeeefe0g0eeeeeeeeeeeeeeee0g00eeeeeeeeeeeeee00g0b0000eeeeee0000f0g000fff000000ffff00g00fffffffffff000f0g0ff0000000000baf0g0ff0fabfffbafffba0g0f0ffbff2f3b3ffff0gg0fff0ffffffff0fff0g0fff0000000000fff0g0fff0gggggggg0fff0g0ff0gggggggggg0ff0gg00gggggggggggg00g'),_N:(0,0,20,20,'ggggg0000000000ggggggggg0ffffffffff0ggggggg0fffffffffffe0ggggg0ffffffffffffef0ggg0fffefffffffffeff0g0ffffefff66f6ffffff00ffffeff6ff66ffefff00ffffeffff666ffffff00ffffef6fffffffffff00ffffe666ff6f6fefff00ffffef6ff666ffefff00ffffeff6ff6fffefff00ffffefffffffffefff00ffffffffffffffffff00ffffeeeeeeeeeeffff00fffeffffffffffefff00ffefff000000fffeff00fefff00000000fffef0g0fff0000000000fffeggg0000000000000000gg'),_F:(1,4,18,13,'gggggggggggg0gggggggggg0000g0070gggggggg07777077570ggggg00755567567570ggg077567777777570gg07657765655767770g077776556556755770000076556556767070ggg075556555670g00ggg075556555670gggggg07665655670gggggggg077777770gggggggggg0000000gggggg'),_D:(2,7,15,9,'gggg0000000ggggg0055765567000g077755555556770g0655655555560g075566566565550g5666656655760g050705576750700g0g0g070606g0gggggggg0g0g0gggg'),'s':(3,3,14,14,'ggg0000000gggggg033322cc0gggg0cc222d2c20gg032d22cc2c220g0322d2c222c0gg022d2c22220gggg0c22cd220ggggg022222d20gggggg0222d2d20gggggg02d2d2220gggggg0c2c222c0gggggg0cc22d220gggggg00cc2220gggggggg00000g'),_G:(3,5,15,9,'gggg0000000ggggg0000223320000g003323332333200033233322333330032333233323320023332333233220022222333222220g0002222222000ggggg0000000gggg'),'tapis':(0,0,20,20,'feeeeeffffffffeeeeefffeeeeeffffffeeeeefffffeeeeeffffeeeeefffffffeeeeeffeeeeefffffffffeeeeeeeeeefffffefffffeeeeeeeefffffeeefffffeeeeeefffffeeeeefffffeeeefffffeeeeeeefffffeefffffeeeeeeeeeffffffffffeeeeefeeeeeffffffffeeeeefffeeeeeffffffeeeeefffffeeeeeffffeeeeefffffffeeeeeffeeeeefffffffffeeeeeeeeeefffffefffffeeeeeeeefffffeeefffffeeeeeefffffeeeeefffffeeeefffffeeeeeeefffffeefffffeeeeeeeeeffffffffffeeeee'),_O:(0,0,8,11,'gggccggggggccgggggccccgggcggggcgcggggcgccgggcggccggcgggccgggcggccggggggcgcggggcgggccccgg'),'t':(4,3,12,13,'ggggggg0gggggggg0g060gggggg060700ggggg02277220ggg0276767220g026226227220022c22722120022cc222221002222c222110g0222222210gg0222221110ggg00111100gggggg0000gggg'),_E:(3,4,13,11,'gggggg000ggggggggg02220ggggggg0233220gggggg02434220ggg00233433220g022224344320022334223320g02334320220gg0223442000gggg0222220ggggggg00000gggggg')}
key_pressed=[False]*5
ma=[[[2,2,2,3,3,2,11,2],[12,1,1,1,1,1,1,4],[6,0,0,4,9,0,0,5],[7,0,0,2,8,0,0,2],[1,0,0,1,1,13,13,1]]]
def fr(x,y,w,h,c):fill_rect(x,y,w,h,c)
def dt(t,x,y,c,b,f=False):draw_string(t,x,y,c,b,f)
def tm():return time.monotonic()
def kd(k):return ion.keydown(k)
def ds(sprite_name,x,y,mu=1):
	offx,offy,w,h,data=sprites[sprite_name];curx,cury=0,0
	for i in range(h):
		for k in range(w):
			px=int(data[w*i+k],18)
			if px!=16 and px!=17:fr(x+offx*mu+curx*mu,y+offy*mu+cury*mu,mu,mu,c[px])
			curx+=1
		curx=0;cury+=1
def save_data(hs):
	try:f=open(_P,'w');f.truncate(0);f.write(hs)
	except:return
class I:
	def __init__(self,i_nom):self.i_nom=i_nom
class A:
	def __init__(self):self.ai=[]
	def r(self,x,y,mu):
		ds(_H,x,y,mu)
		if self.ai==[]:return
		if _C in self.ai:ds('p_bas',x,y,mu)
		if _D in self.ai:ds(_D,x+mu,y-mu,mu)
		if _G in self.ai:ds(_G,x,y-2*mu,mu)
		if _B in self.ai:ds(_B,x+mu,y-4*mu,mu)
		if _E in self.ai:ds(_E,x-2*mu,y-mu,mu)
		if _C in self.ai:ds(_L,x,y,mu)
class M:
	def __init__(self):
		self.mi=[_C,_G];self.m_time=tm(),ra.randint(40,60)
		if ra.getrandbits(1)==1:self.mi.append(_D)
		if ra.getrandbits(1)==1:self.mi.append(_B)
		if ra.getrandbits(1)==1:self.mi.append(_E)
	def is_finished(self):return tm()-self.m_time[0]>self.m_time[1]
	def r_r(self,place):of=place*61;fr(of+4,26,38,12,c[3]);dt(str(int(self.m_time[1]-(tm()-self.m_time[0]))//60)+':'+str(int(self.m_time[1]-(tm()-self.m_time[0]))%60),of+5,26,c[12],c[3],_A);fr(of+2,26,2,14,c[0]);fr(of+4,38,38,2,c[0]);fr(of+41,37,2,2,c[0])
	def f_r(self,place):
		of=place*61;fr(of+3,3,27,34,c[3]);fr(of+30,3,27,34,c[3]);fr(of+3,2,54,2,c[0]);fr(of+3,36,54,2,c[0]);fr(of+2,3,2,34,c[0]);fr(of+56,3,2,34,c[0]);a=A();a.ai=self.mi;a.r(of+5,5,1)
		if _D in self.mi:ds(_D,of+26,8,1)
		if _B in self.mi:ds(_B,of+39,16,1)
		if _E in self.mi:ds(_E,of+39,1,1)
		dt(str(int(self.m_time[1]-(tm()-self.m_time[0]))//60)+':'+str(int(self.m_time[1]-(tm()-self.m_time[0]))%60),of+5,26,c[12],c[3],_A);fr(of+2,26,2,14,c[0]);fr(of+4,38,38,2,c[0]);fr(of+41,37,2,2,c[0])
class P:
	def __init__(self,g,x,y):self.x=x;self.y=y;self.g=g;self.di=_J;self.h=I(_F);assiette=A();assiette.r(0,0,2)
	def dp(self):
		ds(_C+self.di,self.x*40,self.y*40+40,2)
		if type(self.h)==I:ds(self.h.i_nom,self.x*40+10,self.y*40+60)
		elif type(self.h)==A:self.h.r(self.x*40+10,self.y*40+60,1)
	def mv(self,x_mod,y_mod):
		e=ma[g.mapid][self.y][self.x];self.g.de(e,self.x,self.y);new_el=ma[self.g.mapid][self.y+y_mod][self.x+x_mod]
		if self.y+y_mod<4 and new_el in[0,1]:self.y+=y_mod;self.x+=x_mod
		self.dp()
	def dpa(self):
		dir,e,elx,ely=self.di,_I,_I,_I
		if dir=='up':e,elx,ely=self.g.map[self.y-1][self.x],self.x,self.y-1
		elif dir==_J:e,elx,ely=self.g.map[self.y+1][self.x],self.x,self.y+1
		elif dir=='left':e,elx,ely=self.g.map[self.y][self.x-1],self.x-1,self.y
		else:e,elx,ely=self.g.map[self.y][self.x+1],self.x+1,self.y
		if self.h!=_I:self.h=self.g.pi(elx,ely,self.h);self.dp()
		else:self.h=self.g.ri(elx,ely);self.dp()
class G:
	def __init__(self,mapid):self.mapid=mapid;self.map=ma[mapid];self.player=P(self,1,1);self.ms=[];self.old_missions=[];self.pmi=tm(),3;self.g_timer=tm(),5;self.g_money=25
	def gover(self):
		global hg;fr(52,12,216,196,c[4]);fr(50,12,2,196,c[0]);fr(268,12,2,196,c[0]);fr(52,10,216,2,c[0]);fr(52,67,216,2,c[0]);fr(52,208,216,2,c[0]);ds('ga',52,12);dt('GAME OVER',115,25,c[0],c[4]);dt('Ton score: '+str(self.g_money),65,85,c[0],c[4])
		if self.g_money>hg:hg=self.g_money
		dt('Meilleur score: '+str(self.g_money),65,110,c[0],c[4]);dt('OK pour aller au menu',60,190,c[0],c[4],_A)
	def dms(self):
		if tm()-self.pmi[0]>self.pmi[1]:self.ms.append(M());self.pmi=tm(),ra.randint(15,25)
		for i in range(len(self.ms)):
			if self.ms[i].is_finished():self.g_money-=2;self.ms.pop(i);break
		if self.old_missions!=self.ms:
			fr(0,0,320,40,c[2]);self.old_missions=[]
			for i in range(len(self.ms)):self.ms[i].f_r(i);self.old_missions.append(self.ms[i])
		else:
			for i in range(len(self.ms)):self.ms[i].r_r(i)
	def dts(self):
		for i in range(5):
			for k in range(8):
				e=self.map[i][k]
				if type(e)==tuple and len(e)==4:
					if tm()>e[2]+e[3]:
						if e[1]=='s':self.map[i][k]=e[0],_G
						if e[1]==_F:self.map[i][k]=e[0],_D
						if e[1]=='o':self.map[i][k]=e[0],_B
						if e[1]=='t':self.map[i][k]=e[0],_E
						self.de(self.map[i][k],k,i)
					else:self.draw_progressbar(k,i,(tm()-e[2])*18//e[3])
	def gui_f_r(self):fr(0,208,48,14,c[3]);fr(0,206,48,2,c[2]);fr(48,208,2,14,c[2]);fr(47,207,2,2,c[2]);dt('15',2,209,c[12],c[3],_A);ds(_K,38,209);fr(272,208,48,14,c[9]);fr(272,206,48,2,c[8]);fr(270,208,2,14,c[8]);fr(271,207,2,2,c[8]);dt('00:00',273,209,c[12],c[9],_A);ds(_O,310,209)
	def gui_r_r(self):
		dt(str(self.g_money),2,209,c[12],c[3],_A);seconds=str(int(self.g_timer[1]-(tm()-self.g_timer[0]))%60)
		if len(seconds)==1:seconds='0'+seconds
		dt('0'+str(int(self.g_timer[1]-(tm()-self.g_timer[0]))//60)+':'+seconds,273,209,c[12],c[9],_A)
	def draw_progressbar(self,x,y,progress):fr(x*40,y*40+40,40,10,c[0]);fr(x*40+2,y*40+42,36,6,c[7]);fr(x*40+2,y*40+42,int(progress)*2,6,c[5])
	def sk(self):
		if kd(ion.KEY_OK)or kd(ion.KEY_HOME)or kd(ion.KEY_POWER):self.player.dpa();time.sleep(.2)
		elif kd(ion.KEY_UP):self.player.di='up';self.player.mv(0,-1);time.sleep(.1)
		elif kd(ion.KEY_DOWN):self.player.di=_J;self.player.mv(0,1);time.sleep(.1)
		elif kd(ion.KEY_LEFT):self.player.di='left';self.player.mv(-1,0);time.sleep(.1)
		elif kd(ion.KEY_RIGHT):self.player.di='right';self.player.mv(1,0);time.sleep(.1)
	def ra(self):self.dm(self.mapid);self.player.dp()
	def de(self,el,x,y):
		e=el
		if type(e)==tuple:e=e[0]
		if e==0:fr(x*40,y*40+40,40,40,c[14])
		elif e==1:fr(x*40,y*40+40,40,4,c[3]);fr(x*40,y*40+40+4,40,2,c[1]);fr(x*40,y*40+40+6,40,8,c[2]);fr(x*40,y*40+40+14,40,12,c[15]);fr(x*40,y*40+40+26,40,14,c[14])
		elif e==2:fr(x*40,y*40+40,40,40,c[4])
		elif e==3:fr(x*40,y*40+40,40,40,c[4]);ds('poele',x*40,y*40+40,2)
		elif e==4:fr(x*40,y*40+40,40,40,c[4]);ds(_M,x*40,y*40+40,2)
		elif e==5:fr(x*40,y*40+40,40,40,c[4]);ds(_H,x*40,y*40+42,2);ds(_H,x*40,y*40+38,2);ds(_H,x*40,y*40+34,2)
		elif e==6:fr(x*40,y*40+40,40,40,c[4]);ds('c',x*40,y*40+40,2);ds('o',x*40,y*40+40,2)
		elif e==7:fr(x*40,y*40+40,40,40,c[4]);ds('c',x*40,y*40+40,2);ds(_F,x*40,y*40+40,2)
		elif e==8:fr(x*40,y*40+40,40,40,c[4]);ds('c',x*40,y*40+40,2);ds('s',x*40,y*40+40,2)
		elif e==9:fr(x*40,y*40+40,40,40,c[4]);ds('c',x*40,y*40+40,2);ds(_C,x*40,y*40+40,2)
		elif e==11:fr(x*40,y*40+40,40,40,c[4]);ds(_N,x*40,y*40+40,2)
		elif e==12:fr(x*40,y*40+40,40,40,c[4]);ds('c',x*40,y*40+40,2);ds('t',x*40,y*40+40,2)
		elif e==13:ds('tapis',x*40,y*40+40,2)
		if type(el)==tuple:ds(el[1],x*40,y*40+40,2)
	def dm(self,mapid):
		for l in range(5):
			for c in range(8):e=self.map[l][c];self.de(e,c,l)
	def pi(self,elx,ely,h):
		old_el=self.map[ely][elx]
		if type(old_el)==tuple and type(old_el[1])!=A:return h
		if type(h)==I:
			result=_I;e=old_el,h.i_nom
			if old_el==11:return
			elif old_el==2:0
			elif old_el==3 and h.i_nom=='s':e=e[0],e[1],tm(),8
			elif old_el==4 and(h.i_nom=='o'or h.i_nom==_F or h.i_nom=='t'):e=e[0],e[1],tm(),5
			elif type(old_el)==tuple and type(old_el[1])==A:
				n=h.i_nom
				if n==_D or n==_E or n==_B or n==_C or n==_G:
					if n not in self.map[ely][elx][1].ai:self.map[ely][elx][1].ai.append(n);self.map[ely][elx][1].r(elx*40,ely*40+40,2)
					else:return h
				else:return h
				return
			else:return h
			self.map[ely][elx]=e;g.de(e,elx,ely);return result
		elif type(h)==A:
			if old_el==11:return
			elif old_el==2:self.map[ely][elx]=old_el,h;h.r(elx*40,ely*40+40,2);return
			elif old_el==13:
				for i in self.ms:
					if set(i.mi)==set(h.ai):self.g_money+=10;self.ms.remv(i);return
				return h
			else:return h
	def ri(self,elx,ely):
		e=self.map[ely][elx]
		if type(e)==int:
			if e==5:return A()
			elif e==6:return I('o')
			elif e==7:return I(_F)
			elif e==8:return I('s')
			elif e==9:return I(_C)
			elif e==12:return I('t')
			return
		elif type(e[1])==A:self.map[ely][elx]=2;self.de(2,elx,ely);return e[1]
		if e[0]==2:self.map[ely][elx]=2;self.de(2,elx,ely);return I(e[1])
		elif e[0]==3 or e[0]==4:self.map[ely][elx]=e[0];self.de(e[0],elx,ely);return I(e[1])
		else:return
class Gui:
	def __init__(self):self.se=0;self.r();self.state=0
	def redraw_text(self):
		dt('A la carte',200,10,c[3],c[15]);but_c=[c[4]]*3;but_c[self.se]=c[3];but=['Jouer','Aide']
		for i in range(len(but)):dt(but[i],200,40+i*20,but_c[i],c[15])
	def r(self):fr(0,0,320,222,c[15]);ds('ga',0,0,4);self.redraw_text()
	def render_help(self):pass
	def loop(self):
		while _A:
			if kd(ion.KEY_OK)or kd(ion.KEY_HOME):
				if self.state==0:
					if self.se==1:self.render_help();self.state=1
					else:break
				else:self.r();self.state=0
				time.sleep(.3)
			elif kd(ion.KEY_UP):
				if self.state==1:continue
				self.se=(self.se-1)%2;self.redraw_text();time.sleep(.2)
			elif kd(ion.KEY_DOWN):
				if self.state==1:continue
				self.se=(self.se+1)%2;self.redraw_text();time.sleep(.2)
		return self.se
hg=0
try:
	with open(_P,'r')as f:hg=int(f.readline())
except:pass
gui=Gui()
gui.loop()
g=G(0)
g.ra()
g.gui_f_r()
fr(0,0,320,40,c[2])
while _A:
	if tm()-g.g_timer[0]>g.g_timer[1]:
		g.gover()
		while not(kd(ion.KEY_OK)or kd(ion.KEY_HOME)or kd(ion.KEY_POWER)):0
		gui=Gui();time.sleep(1);gui.loop();g=G(0);g.ra();g.gui_f_r();fr(0,0,320,40,c[2])
	g.sk();g.dts();g.dms();g.gui_r_r()