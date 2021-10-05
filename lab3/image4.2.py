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
Green1 = "green"
Green2 = (0, 100, 0)
Gray = (192, 192, 192)
Yellow = "yellow"

def triangle(a, b, r, x, color):
    a = np.pi/180*a
    pg.draw.polygon(screen, color, ([x - ((b + r) * np.sin(a)), 480 - ((b + r) * np.cos(a))],
                                [(b * np.cos(a)) / 1.74 + x - (r * np.sin(a)), 480 - (r * np.cos(a)) - (b * np.sin(a) / 1.74)],
                                 [x - (r * np.sin(a)) - (b * np.cos(a) / 1.74), 480 - (r * np.cos(a)) + (b * np.sin(a) / 1.74)]), 0)
                                 
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

screen = pg.display.set_mode((1500,900))
fontColor = (White)
screen.fill(fontColor)




circle(Orange2, 400, 840, 220)
re_ct(Moccasin, 600, 600, 630, 600, 820, 80,  800, 80)
re_ct(Moccasin, 170, 600, 200, 600, 40, 80,  20, 80)
pentagon(Orange4, 210, 650, 90)
pentagon(Orange4, 590, 650, 90)
pg.draw.ellipse(screen, Moccasin, (5, 80, 100, 130), 0)
pg.draw.ellipse(screen, Moccasin, (730, 80, 100, 130), 0)







for i in range(14):
    triangle(73-11*i, 60, 180, 400, Violet)

    
circle(Moccasin, 400, 480, 180)
circle(Blue_1, 320, 410, 40)
circle(Blue_1, 470, 410, 40)
circle(Black, 320, 415, 15)
circle(Black, 470, 415, 15)
triangle_no_circle(Red, 280, 500, 510, 500, 395, 580)
triangle_no_circle(Brown, 385, 460, 405, 460, 395, 475)







circle(Green2, 1150, 840, 220)
re_ct(Moccasin, 1340, 600, 1370, 600, 1480, 80,  1460, 80)
re_ct(Moccasin, 920, 600, 950, 600, 790, 80,  770, 80)
pentagon(Green1, 960, 650, 90)
pentagon(Green1, 1340, 650, 90)
pg.draw.ellipse(screen, Moccasin, (755, 80, 100, 130), 0)
pg.draw.ellipse(screen, Moccasin, (1400, 80, 100, 130), 0)


for i in range(14):
    triangle(73-11*i, 60, 180, 1150, Yellow)

    
circle(Moccasin, 1150, 480, 180)
circle(Gray, 1070, 410, 40)
circle(Gray, 1220, 410, 40)
circle(Black, 1070, 415, 15)
circle(Black, 1220, 415, 15)
triangle_no_circle(Red, 1030, 500, 1260, 500, 1145, 580)
triangle_no_circle(Brown, 1135, 460, 1155, 460, 1145, 475)





(x,y,fontSize) = (0,15,143)
myFont = pg.font.SysFont("None", fontSize)
fontImage = myFont.render("PYTHON is REALLY AMAZING!", 0, "black", "green")
screen.blit(fontImage, (x,y))



    
mainLoop = True
while mainLoop:
    clock.tick(FPS) 
    for event in pg.event.get():
        if event.type == QUIT:
            mainLoop = False
        pg.display.update()
