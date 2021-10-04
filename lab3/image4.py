import pygame as pg
from pygame.locals import *
import numpy as np

             
FPS = 30
Moccasin = (255, 228, 181)
White = (255, 255, 255)
Violet = "violet"
Blue_1 = (0, 190, 255)
Black = "black"
Red = "red"
Brown = (139, 69, 19)
Orange = (255, 165, 0)
Orange2 = (235, 140, 0)
Orange3 = (255, 69, 0)
Orange4 = (255, 99, 71)


def triangle(a, b, r):
    a = np.pi/180*a
    pg.draw.polygon(screen, Violet, ([500 - ((b + r) * np.sin(a)), 480 - ((b + r) * np.cos(a))],
                                [(b * np.cos(a)) / 1.74 + 500 - (r * np.sin(a)), 480 - (r * np.cos(a)) - (b * np.sin(a) / 1.74)],
                                 [500 - (r * np.sin(a)) - (b * np.cos(a) / 1.74), 480 - (r * np.cos(a)) + (b * np.sin(a) / 1.74)]), 0)
                                 
def circle(circle_collor, x, y, R):
    pg.draw.circle(screen, circle_collor, (x,y), R, 0)

def triangle_no_circle(Collor_triangle_no_circle, x1, y1, x2, y2, x3, y3):
    pg.draw.polygon(screen, Collor_triangle_no_circle, ([x1,y1], [x2, y2], [x3, y3]), 0)
    
def pentagon(pentagon_collor, x0, y0, R):
    f = 54 * (np.pi/180)
    x1 = x0 + R * np.cos(f)
    y1 = y0 + R * np.sin(f)
    x2 = x0 - R * np.cos(f)
    y2 =  y0 + (R * np.sin(f))
    x3 = x0 - R
    y3 = y0
    x4 = x0
    y4 = y0 - R
    x5 = x0 + R
    y5 = y0
    
    pg.draw.polygon(screen, pentagon_collor, [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)], 0)

def re_ct(collor, x1, y1, x2, y2, x3, y3, x4, y4):
    pg.draw.polygon(screen, collor, [(x1, y1), (x2, y2), (x3, y3), (x4, y4)], 0)


pg.init()
clock = pg.time.Clock()

screen = pg.display.set_mode((1000,900))

fontColor = (White)
screen.fill(fontColor)
(x,y,fontSize) = (0,10,156)
myFont = pg.font.SysFont("None", fontSize)



circle(Orange2, 500, 840, 250)
re_ct(Moccasin, 740, 600, 770, 600, 960, 80,  940, 80)
re_ct(Moccasin, 230, 600, 260, 600, 100, 80,  80, 80)
pentagon(Orange4, 280, 640, 90)
pentagon(Orange4, 720, 640, 90)
pg.draw.ellipse(screen, Moccasin, (65, 80, 100, 130), 0)
pg.draw.ellipse(screen, Moccasin, (875, 80, 100, 130), 0)



fontImage = myFont.render("Python is Amazing", 0, "black", "green")
screen.blit(fontImage, (x,y))



for i in range(14):
    triangle(73-11*i, 60, 200)

    
circle(Moccasin, 500, 480, 200)
circle(Blue_1, 420, 410, 40)
circle(Blue_1, 570, 410, 40)
circle(Black, 420, 415, 15)
circle(Black, 570, 415, 15)
triangle_no_circle(Red, 380, 500, 610, 500, 495, 580)
triangle_no_circle(Brown, 485, 460, 505, 460, 495, 475)


    
mainLoop = True
while mainLoop:
    clock.tick(FPS) 
    for event in pg.event.get():
        if event.type == QUIT:
            mainLoop = False
        pg.display.update()

