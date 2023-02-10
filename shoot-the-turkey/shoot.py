WIDTH= 600
HEIGHT=600
from random import randint
import time
turkey= Actor("turkey")

start_time=time.time()
elapsed_time=0
time_limit=10

def draw():
    screen.clear()
    turkey.draw()

def update():
    elapsed_time = time.time() - start_time
    if elapsed_time>time_limit:
        print ("GAME OVER")
        exit()

def place_turkey():
    turkey.x=randint(10,600)
    turkey.y=randint(10,600)


def on_mouse_down(pos):
    if turkey.collidepoint(pos):
        print("Good shot!")
        place_turkey()
    else:
        print ("You missed lol!")
        quit()



