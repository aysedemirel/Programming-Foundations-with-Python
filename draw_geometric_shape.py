import turtle

window = turtle.Screen()
window.bgcolor("black")

def draw_turtle():
    rishi = turtle.Turtle()
    rishi.shape("arrow")
    rishi.color("red")
    rishi.speed(10)
    for i in range(1,5):
        rishi.forward(100)
        rishi.right(90)

def draw_circle():
    bert = turtle.Turtle()
    bert.shape("classic")
    bert.color("white")
    bert.circle(100)

def draw_triangle():
    angie = turtle.Turtle()
    angie.shape("circle")
    angie.color("green")
    angie.speed(10)

    for i in range(1,4):
        angie.forward(100)
        angie.left(120)

draw_turtle()
draw_circle()
draw_triangle()

window.exitonclick()
