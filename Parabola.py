import turtle

x, y = 0, 0
vx, vy = 20, 40
g = -9.8
k = 0.8
dt = 0.1
for i in range(0, 10):
    while y >= 0:
        x += vx * dt
        y += vy * dt
        vy += g * dt
        turtle.goto(x, y)
    vx = k * vx
    vy = -k * vy
    y = 0.1
turtle.done()
