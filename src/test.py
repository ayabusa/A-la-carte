import os

def readBestScore():
  try:
    file=open("alacarte.sav","r")
    best = file.readline()
    file.close()
    return int(best)
  except:
    return 0

def saveScore(score):
  try :
    file=open("alacarte.sav","w")
    file.truncate(0)
    file.write(str(score))
    file.close()
  except: pass

saveScore(3)
print(readBestScore())