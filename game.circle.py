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
height_square = 50
score = 0
number_circle = 4
g = 0
#Чиcло квадратиков на экране
score_super = 0

def Start():
    '''Функция рисует на чёрном экране красную кнопку Start'''
    (x, y, fontSize) = (500, 350, 100)
    myFont = pygame.font.SysFont("None", fontSize)
    fontImage = myFont.render("Start ", 0, "RED", "BLACK")
    screen.blit(fontImage, (x,y))


def run_game(x, y):
    '''Функция не даёт запуститься игре пока не будет
    мышкой нажата кнопка Start'''
    game = True
    while game:
        clock.tick(FPS)
        for event in pygame.event.get():
            print("game_-1 = ", game)
            if event.type == pygame.MOUSEBUTTONDOWN:
                a = event.pos[0]
                b = event.pos[1]
                print(a, b)
                print("QWERTY === ", x, y)
                if a > x and a < x + 100 and b > y and b < y + 100:
                    #Условие попадания в кнопку страт кликом мышки
                    game = False


def new_ball():
    '''рисует новый шарик '''
    x = x_circle = randint(100, 1100)
    y = y_circle = randint(100, 800)
    r = circle_radius = randint(10, 100)
    v_x = v_x_speed_circle = randint(-5,5)
    v_y = v_y_speed_circle = randint(-5,5)
    color = color_circle = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    return x, y, r, color, v_x, v_y

def super_figure():
    '''рисует бонусную фигуру в виде квдрата'''
    x_1  = x_square = randint(100, 950)
    y_1 = y_square = randint(100, 700)
    v_x1 = v_x1_square_speed = randint(-10, 10)
    v_y1 = v_y1_square_speed = randint(-10, 10)
    color1 = color_square = COLORS[randint(0,5)]
    return x_1, y_1, v_x1, v_y1, color1


def circle_speed():
    '''данная функция передвигает шарики на экране с учётом
    отражения от стен, в массиве А содержатся параметры шариков'''
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


def square_speed():
    '''Данная функция передвигает квадратики на экране с учётом
    отражения от стен, в масиве В содержатся параметры квадратиков'''
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
clock = pygame.time.Clock()
finished = False

Start()
pygame.display.update()
run_game(500, 350)
print("name")
name = input()

j = 0
A = [number_circle for j in range(4)]
while j < 4:
    x, y, r , c, v_x, v_y = new_ball()
    A[j] = [x, y, r, c, v_x, v_y]
    j += 1

super_figure()

i = 0
number_super_figure = 1000
B = [number_super_figure for i in range(1000)]
while i < 100:
    x_1, y_1, v_x1, v_y1, color1 = super_figure()
    B[i] = [x_1, y_1, v_x1, v_y1, color1, height_square, height_square]
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
                    #Условие попадания в шарик через теорему пифагора
                    score += 1
                    probability = randint(0,5)
                    if probability <= 5 :
                        x, y, r, c, v_x, v_y = new_ball()
                        A[j] = [x, y, r, c, v_x, v_y]
                    if probability > 3:
                        g += 1
                        x_1, y_1, v_x1, v_y1, color1 = super_figure()
                        B[g] = [x_1, y_1, v_x1, v_y1,
                                color1, height_square, height_square]
            for h in range(g + 1):
                if a > B[h][0] and a < B[h][0] + 50 and b > B[h][1] and b < B[h][1] + 50:
                    #Условие попадания в квадратик
                    score_super += 5
                    probability = randint(0,5)
                    if probability > 3:
                        x_1, y_1, v_x1, v_y1, color1 = super_figure()
                        B[h] = [x_1, y_1, v_x1, v_y1, color1, height_square, height_square]
                    if probability <= 3:
                        B[h] = [0, 0, v_x1, v_y1, color1, 0, 0]
                    h += 1
    
    Score = str(score + score_super)
    screen.fill(BLACK)
    (x1, y1, x2, fontSize) = (10, 15, 150, 50)
    myFont = pygame.font.SysFont("None", fontSize)
    fontImage = myFont.render("Score: ", 0, "RED", "BLACK")
    fontImage_score = myFont.render(Score, 0, "RED", "BLACK")
    screen.blit(fontImage, (x1,y1))
    screen.blit(fontImage_score, (x2,y1))
    #Данный блок реализует подсчёт очков и выводит их на экран
    
    circle_speed()
    square_speed()

    pygame.display.update()

result = open('result.txt', 'a')
name = str(name)
print(name + ":" + Score + "\n", file = result)
result.close()
pygame.quit()
