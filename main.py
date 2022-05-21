import sys, os, random
from time import sleep
from replit import db

true = True
false = False

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
def resetdb():
  db.clear()
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

def save(localdb):
  try:
    x = db["Name"]
    x = db["Funding"]
    x = db["Missions"]
    x = db["Successful Missions"]
    x = db["Failed Missions"]
    x = db["Research"]
    x = db["Accolades"]
    del x
  except KeyError:
    db["Name"] = ""
    db["Funding"] = 100
    db["Missions"] = []
    db["Successful Missions"] = []
    db["Failed Missions"] = []
    db["Research"] = {
      "Payload Rank": 1,
      "Second Stage Rank": 0,
      "First Stage Rank": 1,
      "Boosters Rank": 0,
    }
    db["Launch Vehicles"] = []
    db["Payloads"] = []
    db["Accolades"] = {
      "Low Earth Orbit": False,
      "Med Earth Orbit": False,
      "High Earth Orbit": False,
      "Moon Fly-by": False,
      "High Moon Orbit": False,
      "Medium Moon Orbit": False,
      "Low Moon Orbit": False,
      "Moon Landing": False,
      "Moon Landing/Return": False,
      "Moon Habitat": False,
      "Space Station": False,
      "Deep Space": False,
      "???": False
    }
    _x = [i for i in localdb]
    for i in _x:
      db[i] = localdb[i]
  else:
    _x = [i for i in localdb]
    for i in _x:
      db[i] = localdb[i]

def load():
  localdb = {}
  _x = [i for i in db]
  for i in _x:
    localdb[i] = db[i]
  return localdb

def awardAccolade(award):
  x = localdb["Accolades"]
  try:
    y = x[award]
  except KeyError:
    print(f"{award} is not a valid award")
  else:
    x[award] = True
    print(f"You have achieved {award}")


localdb = load()
save(localdb)

def intro():
  try:
    x = localdb["Name"]
  except KeyError:
    type("Databases are being reset")
    quit()
  if localdb["Name"] != "":
    type(f"Welcome back \033[38;2;255;250;0m{localdb['Name']}\33[0m!", 0)
    sleep(5)
    type("Reloading ", newline=false)
    rgbcolortype("Save",0,255,0, newline=false)
    type("!")
    sleep(3)
  else:
    type("Welcome to ",0.025, False, False)
    rgbcolortype("Space Agency Simulator", 60, 230, 30, 0.025)
    type("This game has an ", newline=false)
    rgbcolortype("autosave",0,255,0, newline=false)
    type(" feature")
    sleep(1)
    type("You may manually save by selecting the last option on the main menu.")
    sleep(1)
    type("Please enter your agency name", 0.025, newline=False)
    localdb["Name"] = input(": ")
  save(localdb)

def new_pl():
  clr()
  r = localdb["Research"]
  type("What is the name of your payload?")
  pl_name = input(">: ")
  pl = {"Name": pl_name}
  type("What type of payload is it?")
  if r["Payload Rank"] >= 1:
    sleep(1)
    type("1: Satellite")
  if r["Payload Rank"] >= 2:
    sleep(1)
    type("2: Medium Altitude Satellite")
  if r["Payload Rank"] >= 3:
    sleep(1)
    type("3: High Altitude Satillite")
  pl_type = int(input(">: "))
  if pl_type == 1:
    pl["Type"] = "Satellite"
  if pl_type == 2:
    pl["Type"] = "Medium Altitude Satellite"
  if pl_type == 3:
    pl["Type"] = "High Altitude Satellite"
  pl["Orbital Capability"] = pl_type
  localdb["Payloads"].append(pl)
  mainscreen()
  return pl
  
def new_lv():
  clr()
  r = localdb["Research"]
  type("What is the name of your launch vehicle?")
  lv_name = input(">: ")
  lv = {"Name": lv_name}
  type("What first stage engine are you using?")
  sleep(1)
  if r["First Stage Rank"] >= 1:
    type("1: RocketDyne A-7")
  if r["First Stage Rank"] >= 2:
    type("2: RocketDyne H-1")
  if r["First Stage Rank"] >= 3:
    type("3: RocketDyne H-1 x8")
  lv_first_stage_rank = int(input(">: "))
  lv["First Stage Engine"] = lv_first_stage_rank
  sleep(1)
  type("What second stage engine are you using?")
  sleep(1)
  if r["Second Stage Rank"] == 0:
    type("You have not researched second stages")
    lv_second_stage_rank = 0
    sleep(1)
  if r["Second Stage Rank"] >= 1:
    type("1: RocketDyne RL10")
  if r["Second Stage Rank"] >= 2:
    type("2: RocketDyne J-2")
    lv_second_stage_rank = int(input(">: "))
  lv["Second Stage Engine"] = lv_second_stage_rank
  type("What boosters are you using?")
  sleep(1)
  if r["Boosters Rank"] == 0:
    type("You have not researched boosters")
    lv_boosters_rank = 0
    sleep(1)
  lv["Boosters"] = lv_boosters_rank
  type(f"Creating Launch Vehicle {lv['Name']}")
  lx = lv["First Stage Engine"] + lv["Second Stage Engine"] + lv["Boosters"]
  if lv["Second Stage Engine"] == 0 and lv["Boosters"] == 0:
    lv["Payload Capability"] = lx
  elif lv["Second Stage Engine"] > 0 and lv["Boosters"] > 0: 
    lv["Payload Capability"] = lx/3
  else:
    lv["Payload Capability"] = lx/2
  localdb["Launch Vehicles"].append(lv)
  mainscreen()
  return lv
  
def new_mission():
  clr()
  x = localdb["Launch Vehicles"]
  y = localdb["Payloads"]
  type("What is the name of your mission?")
  mission_name = input(">: ")
  r = {}
  m = {"Name": mission_name, "Rocket": r, "State": "Not Started", "Goal": 1}
  type("Please select a Launch Vehicle")
  sleep(1)
  try:
    lv = x[0]
  except IndexError:
    type("You have not created any launch vehicles")
    sleep(1)
    mainscreen()
  else:
    w = 1
    for i in x:
      
      type(f"{w}: {i['Name']}")
      w += 1
    ww = input(">: ")
    w = int(ww)
    r["Launch Vehicle"] = x[w-1]
  type("Please select a payload")
  sleep(1)
  try: 
    p = y[0]
  except IndexError:
    type("You have not created any payloads")
    sleep(1)
    mainscreen()
  else:
    z = 1
    for i in y:
      type(f"{z}: {i['Name']}")
      z += 1
    zz = input(">: ")
    z = int(zz)
    r["Payload"] = y[z-1]

  p = r["Payload"]
  
  if p["Orbital Capability"] >= 1:
    type("Your mission is safe to launch!")
    sleep(1)
    type("Please select a goal")
    if p["Orbital Capability"] >= 1:
      type("1: LEO")
    if p["Orbital Capability"] >= 2:
      type("2: MEO")
    if p["Orbital Capability"] >= 3:
      type("3: HEO")
    g = int(input(">: "))
    m["Goal"] = g

    localdb["Missions"].append(m)
    mainscreen()
  else:
    type("Your mission is not safe to launch")
    mainscreen()
  
  return m

def st_mission():
  clr()
  m = localdb["Missions"]
  type("Please select a mission")
  sleep(1)
  try:
    z= m[0]
  except IndexError:
    type("You have no missions planned")
    sleep(1)
    mainscreen()
  else:
    for i in m:
      z = 1
      type(f"{z}: {i['Name']}")
      z += 1
    zz = input(">: ")
    z = int(zz)
    mm = m[z-1]  
  type("Your mission is launching")
  sleep(2)
  mlv = mm["Rocket"]
  mmr = mlv["Launch Vehicle"]
  xx = random.randrange(mmr["Payload Capability"] * 100)
  print(xx)
  if xx < 90 and mm["Goal"] == 1: 
    mm["State"] = "LEO"
    type(f"Mission Success, you have launched a payload into {mm['State']}")
    localdb["Funding"] += 10
    sleep(1)
    awardAccolade("Low Earth Orbit")
    sleep(1)
    localdb["Missions"].remove(mm)
    localdb["Successful Missions"].append(mm)
  elif xx > 90 and xx <100:
    type("Your mission failed to launch")
    sleep(1)
    localdb["Missions"].remove(mm)
    localdb["Failed Missions"].append(mm)
    mm["State"] = "Failed"
  elif xx > 100 < 190 and mm["Goal"] == 2:
    mm["State"] = "MEO"
    type(f"Mission Success, you have launched a payload into {mm['State']}")
    localdb["Funding"] += 25
    sleep(1)
    awardAccolade("Med Earth Orbit")
    localdb["Missions"].remove(mm)
    localdb["Successful Missions"].append(mm)
  elif xx > 190 < 200:
    type("Your mission failed to launch")
    sleep(1)
    localdb["Missions"].remove(mm)
    localdb["Failed Missions"].append(mm)
    mm["State"] = "Failed"
    mainscreen()
  elif xx > 200 < 290 and mm["Goal"] == 2:
    mm["State"] = "HEO"
    type(f"Mission Success, you have launched a payload into {mm['State']}")
    localdb["Funding"] += 50
    sleep(1)
    awardAccolade("High Earth Orbit")
    localdb["Missions"].remove(mm)
    localdb["Successful Missions"].append(mm)
  elif xx > 290 < 300:
    type("Your mission failed to launch")
    sleep(1)
    localdb["Missions"].remove(mm)
    localdb["Failed Missions"].append(mm)
    mm["State"] = "Failed"
    mainscreen()
  else:
    type("Your mission failed to launch")
    sleep(1)
    localdb["Missions"].remove(mm)
    localdb["Failed Missions"].append(mm)
    mm["State"] = "Failed"
    mainscreen()
  mainscreen()

def view_mission():
  clr()
  x = localdb["Successful Missions"]
  a = localdb["Accolades"]

  if x == []:
    type("Launch a mission first")
    sleep(1)
    mainscreen()
  type("Which orbit?")
  if a["Low Earth Orbit"] == True:
    type("1: Low Earth Orbit") 
  if a["Med Earth Orbit"] == True:
    type("2: Med Earth Orbit")
  if a["High Earth Orbit"] == True:
    type("3: High Earth Orbit")
  oz = int(input(">: "))
  if oz == 1:
    z = "LEO"
  if oz == 2:
    z = "MEO"
  if oz == 3:
    z = "HEO"
  xz = 1
  type("Which mission?")
  for i in x:
    if i["State"] == z:
      type(f"{xz}: {i['Name']}")
    else:
      pass
    xz += 1
  zz = int(input(">: "))
  try: 
    sm = x[zz-1]
  except IndexError:
    type("Next time Pick from the list given")
    mainscreen()
  else:
    pass
  type(f"Name: {sm['Name']}")
  type(f"Rocket: {sm['Rocket']['Launch Vehicle']['Name']} \nPayload: {sm['Rocket']['Payload']['Name']} {sm['Rocket']['Payload']['Type']}")
  type(f"Orbit: {sm['State']}")
  type("Press any key to return to the main screen")
  input("")
  save(localdb)
  mainscreen()

def view_pmissions():
  clr()
  s = localdb["Successful Missions"]
  f = localdb["Failed Missions"]

  if f == [] and s == []:
    type("Launch a mission first")
    sleep(1)
    mainscreen()
  type("Succesful Missions")
  for i in s:
    type(f"{i['Name']}: {i['State']}")
  sleep(1)
  type("Failed Missions")
  for i in f:
    type(f"{i['Name']}: {i['State']}")
  sleep(1)
  type("Press any key to return to the main screen")
  input("")
  save(localdb)
  mainscreen()

def view_lv():
  clr()
  lvs = localdb["Launch Vehicles"]
  type("Your Launch Vechicles")
  if lvs == []:
    type("You have no launch vehicles")
    sleep(1)
    mainscreen()
  for i in lvs:
    rgbcolortype(f"{i['Name']}",255,165,0)
    sleep(1)
  type("Press any key to return to the main menu")
  input("")
  save(localdb)
  mainscreen()

def view_pl():
  clr()
  pls = localdb["Payloads"]

  type("Your Payloads")
  if pls == []:
    type("You have no payloads")
    sleep(1)
    mainscreen()
  
  for i in pls:
    rgbcolortype(f"{i['Name']}",255,165,0)
    sleep(1)
  type("Press any key to return to the main menu")
  input("")
  save(localdb)
  mainscreen()
def research():
  clr()

  type("What to research?")
  sleep(1)
  type("1: First Stages")
  type("2: Second Stages")
  type("3: Payloads")

  xr = int(input(">: "))
  if xr == 1:
    if localdb["Funding"] < 10:
      type("You don't have enough money")
      mainscreen()
    localdb["Research"]["First Stage Rank"] += 1
    localdb["Funding"] -= 10
    mainscreen()
  if xr == 2:
    if localdb["Funding"] < 25:
      type("You don't have enough money")
      mainscreen()
    localdb["Research"]["Second Stage Rank"] += 1
    localdb["Funding"] -= 50
    mainscreen()
  if xr == 3:
    if localdb["Funding"] < 50:
      type("You don't have enough money")
      mainscreen()
    localdb["Research"]["Payload Rank"] += 1
    localdb["Funding"] -= 50
    save(localdb)
    mainscreen()

def mainscreen():
  clr()
  type(f"""\033[38;2;255;250;0m{localdb["Name"]}\33[0m
\033[38;2;60;230;30m{localdb["Funding"]}M USD\33[0m
\033[38;2;255;165;0m       
1: New Mission
2: Start Mission
3: New Launch Vehicle
4: New Payload
5: View Space
6: View Past Missions
7: View Launch Vehicles
8: View Payloads
9: Research New Items
0: Save """, 0)
  n_input = input(">:\33[0m")
  try:
    mainscreen_input = int(n_input)
  except ValueError:
    type("Choose a number, Not a letter, or nothing")
    sleep(3)
    mainscreen()
  if mainscreen_input == 1:
    new_mission()
    save(localdb)
  if mainscreen_input == 2:
    st_mission()
    save(localdb)
  if mainscreen_input == 3:
    new_lv()
    save(localdb)
  if mainscreen_input == 4:
    new_pl()
    save(localdb)
  if mainscreen_input == 5:
    view_mission()
    save(localdb)
  if mainscreen_input == 6:
    view_pmissions()
    save(localdb)
  if mainscreen_input == 7:
    view_lv()
    save(localdb)
  if mainscreen_input == 8:
    view_pl()
    save(localdb)
  if mainscreen_input == 9:
    research()
    save(localdb)
  if mainscreen_input == 0:
    save(localdb)
    clr()
    type('saved', 0.025)
    sleep(2)
    save(localdb)
    mainscreen()
  if mainscreen_input > 9:
    type("Not an accepted value", 0)
    save(localdb)
    sleep(3)
    mainscreen()



intro()
mainscreen()