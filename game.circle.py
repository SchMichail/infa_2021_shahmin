import pygame 
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 800))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
j = 0
''' number figure '''
score = 0
number_circle = 4
g = 0
i = 0 
score_super = 0


def new_ball():
    '''рисует новый шарик '''
    x = randint(100, 1100)
    y = randint(100, 800)
    r = randint(10, 100)
    v_x = randint(-5,5)
    v_y = randint(-5,5)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    return x, y, r, color, v_x, v_y

def super_figure():
    '''рисует бонусную фигуру в виде квдрата'''
    x_1 = randint(100, 950)
    y_1 = randint(100, 700)
    v_x1 = randint(-10, 10)
    v_y1 = randint(-10, 10)
    color1 = COLORS[randint(0,5)]
    '''rect(screen, color1, (x_1, y_1, 50, 50))'''
    return x_1, y_1, v_x1, v_y1, color1
    

pygame.display.update()
clock = pygame.time.Clock()
finished = False

A = [number_circle for j in range(4)]
while j < 4:
    x, y, r , c, v_x, v_y = new_ball()
    A[j] = [x, y, r, c, v_x, v_y]
    j += 1


super_figure()



number_super_figure = 100
B = [number_super_figure for i in range(100)]
while i < 100:
    x_1, y_1, v_x1, v_y1, color1 = super_figure()
    B[i] = [x_1, y_1, v_x1, v_y1, color1, 50, 50]
    i += 1


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            print(event.pos)
            a = event.pos[0]
            b = event.pos[1]
            for j in range(4):
                if (a - A[j][0]) ** 2 + (b - A[j][1]) **2 < A[j][2] ** 2:
                    score += 1
                    ver = randint(0,5)
                    if ver <= 5 :
                        x, y, r, c, v_x, v_y = new_ball()
                        A[j] = [x, y, r, c, v_x, v_y]
                    if ver > 3:
                        g += 1
                        x_1, y_1, v_x1, v_y1, color1 = super_figure()
                        B[g] = [x_1, y_1, v_x1, v_y1, color1, 50, 50]
            for h in range(g + 1):
                if a > B[h][0] and a < B[h][0] + 50 and b > B[h][1] and b < B[h][1] + 50:
                    score_super += 5
                    ver = randint(0,5)
                    if ver > 3:
                        x_1, y_1, v_x1, v_y1, color1 = super_figure()
                        B[h] = [x_1, y_1, v_x1, v_y1, color1, 50, 50]
                    if ver <= 3:
                        B[h] = [0, 0, v_x1, v_y1, color1, 0, 0]
                    h += 1
                    
                    
    screen.fill(BLACK)
    
         
    (x1, y1, x2, fontSize) = (10, 15, 150, 50)
    myFont = pygame.font.SysFont("None", fontSize)
    fontImage = myFont.render("Score: ", 0, "RED", "BLACK")
    Score = str(score + score_super)
    fontImage_score = myFont.render(Score, 0, "RED", "BLACK")
    screen.blit(fontImage, (x1,y1))
    screen.blit(fontImage_score, (x2,y1))

    j = 0
    while j < 4:
        circle(screen, A[j][3], (A[j][0], A[j][1]), A[j][2])
        if A[j][0] - A[j][2] < 0:
            A[j][4] = -1 * A[j][4]
        if A[j][0] + A[j][2] > 1200:         
            A[j][4] = -1 * A[j][4]
        if A[j][1] - A[j][2] < 0:
            A[j][5] = -1 * A[j][5]
        if A[j][1] + A[j][2] > 800:
            A[j][5] = -1 * A[j][5]
        A[j][0] += A[j][4]
        A[j][1] += A[j][5]
        j += 1

    h = 0
    while h < g+1:
        B[h][4] = COLORS[randint(0, 5)]
        rect(screen, B[h][4], (B[h][0], B[h][1], B[h][5], B[h][6]))
        if B[h][0] < 0:
            B[h][2] = -1 * B[h][2]
        if B[h][0] + 50 > 1200:
            B[h][2] = -1 * B[h][2]
        if B[h][1] < 0:
            B[h][3] = -1 * B[h][3]
        if B[h][1] + 50 > 800:
            B[h][3] = -1 * B[h][3]
        B[h][0] += B[h][2]
        B[h][1] += B[h][3]
        h += 1
        
         
    pygame.display.update()


pygame.quit()
