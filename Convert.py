import turtle
symbols = {
    '1': [(0,1), (1,2), (1,0)],
    '2': [(0,2), (1,2), (1,1), (0,0), (1,0)],
    '3': [(0,2), (1,2), (0,1), (1,1), (0,0)],
    '7': [(0,2), (1,2), (0,1), (0,0)],
    '4': [(0,2), (0,1), (1,1), (1,2), (1,0)],
    '0': [(0,0), (0,2), (1,2), (1,0), (0,0)]
}
scale = 10

x0, y0 = 0, 0
for s in '141700':
    turtle.up()
    turtle.goto(x0 + symbols[s][0][0] * scale, y0 + symbols[s][0][1] * scale)
    turtle.down()
    for x, y in symbols[s]:
        turtle.goto(x0 + x*scale, y0 + y*scale)

    x0 += 1.5*scale
turtle.done()

