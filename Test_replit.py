import turtle

screensize = 600
screen = turtle.Screen()
screen.setup(screensize, screensize)
screen.screensize(sceensize * 3, screensize * 3)
screen.colormode(255)

t = turtle.Turtle()
t.speed(0)

for i in range(3):
  t.forward(50)
  t.left(120)
