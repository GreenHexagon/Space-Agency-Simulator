import sys, os, random, json
from time import sleep

# convienience
true = True
false = False


# functions
def type(w, delay = 0.025, instant=False, newline=True):
  if instant == True and delay !=0:
    delay = 0
  for char in w:
    sys.stdout.write(char)
    sys.stdout.flush()
    sleep(delay)
  if newline == True:
    print("")
    
def clr():
  os.system('clear')

def rgbcolortype(w, r, g, b, delay=0.025, instant=False, newline=True):
  if instant == True and delay != 0:
    delay =0
  sys.stdout.write(f"\033[38;2;{r};{g};{b}m")
  sys.stdout.flush()
  for c in w:
    sys.stdout.write(c)
    sys.stdout.flush()
    sleep(delay)
  if newline == True:
    print("")
  sys.stdout.write(f"\033[0m")
  sys.stdout.flush()

#classes

class Astronaut():
  def __init__(self, name, missions, missionslist = [], status = "Alive"):
    self.name = name
    self.missions = missions
    self.missionslist = missionslist
    self.status = status
  def update(self, mission: dict, status): 
    self.missions += 1
    self.missionslist.append(mission)
    if status == "Successful":
      pass
    if status == "Failed":
      self.status == f"Deceased: killed on {mission['Name']}"

class Mission()