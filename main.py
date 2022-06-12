import sys, os, random, json
from time import sleep
# convienience
true = True
false = False


# Defs
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