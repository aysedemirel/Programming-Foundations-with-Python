import turtle

def draw_flower(ink):
    ink.up()
    ink.home()
    for degrees in range(10, 370, 10):
        ink.down()
        ink.forward(100)
        ink.up()
        ink.home()  # resets angle to 0 degrees
        ink.left(degrees)  # so absolute angle, not relative

def draw_stem(ink):
    ink.goto(1, -400)
    ink.home()
    ink.goto(5, -400)
    ink.home()
    ink.goto(3, -400)

def draw_triangle():
    angie = turtle.Turtle()
    angie.shape("circle")
    angie.color("green")
    angie.speed("fast")
    angie.setposition(0,-200)
    for i in range(1, 4):
        angie.forward(100)
        angie.left(120)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")

    stem = turtle.Turtle()
    stem.color("green")
    stem.speed("fastest")

    draw_stem(stem)

    draw_triangle()

    flower = turtle.Turtle()
    flower.color("red")
    flower.speed("fast")

    draw_flower(flower)

draw_art()

turtle.done()
