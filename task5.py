import turtle

color = input("Enter the color please: ")
leg_length = int(input("Enter the leg length please: "))

screen = turtle.Screen()
screen.title("turtule")
turtule = turtle.Turtle()
turtule.color(color)

for _ in range(4):
    turtule.forward(leg_length)
    turtule.left(90)

screen.mainloop()