import  turtle
import time


#setup 
clr= (0.2, 0.3, 0.4)
dark_green = (0, 0.4, 0)       # Dark green
deep_red = (0.5, 0, 0)          # Darker red
amber = (0.8, 0.7, 0.1)         # Dark yellow alternative
for i in range(100):
    turtle.forward(10)
    turtle.backward(15)
    turtle.bgcolor(*clr)
    time.sleep(0.1)
    # turtle.speed(100000000000000)
    turtle.color(*dark_green)
    turtle.circle(50)
    turtle.left(45)
    time.sleep(0.1)
    turtle.color(deep_red)
    turtle.speed(100000000)
    turtle.circle(15)
    turtle.left(45)
    turtle.position()
    time.sleep(0.1)
    # turtle.speed(10000000)
    turtle.color(amber)
    turtle.circle(100)
    turtle.left(45)
    turtle.circle(30)

# #pentagon
t = turtle.Turtle()
# for _ in range(5):
#     t.forward(100)
#     t.left(72)  # 360/5

# for _ in range(4):
#     t.forward(100)
#     t.left(90)

# t.color("red")
# t.speed(0)  # Fastest drawing

# # # Draw one petal using two arcs
# def draw_petal():
#     for _ in range(2):
#         t.circle(100, 60)  # Draw 60° arc with radius 100
#         t.left(120)        # Turn to draw the other half

# # Draw full flower
# for _ in range(6):
#     draw_petal()
#     t.right(60)  # Rotate for next petal

# t.hideturtle()
# turtle.done()

# for _ in range(30):
#     t.forward(100)
#     t.left(120)