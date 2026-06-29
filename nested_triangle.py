import turtle

# Set up the screen window
window = turtle.Screen()

# Create a visible turtle object
my_turtle = turtle.Turtle()
my_turtle.shapesize(4)

def event_handler(x=None, y=None):
  for _ in range(3):
    my_turtle.color("red")
    my_turtle.forward(100)
    my_turtle.right(120)

  for _ in range(3):
    my_turtle.color("blue")
    my_turtle.forward(50)
    my_turtle.right(120)

  for _ in range(3):
    my_turtle.color("green")
    my_turtle.forward(25)
    my_turtle.right(120)

window.onclick(event_handler)

# Keep the window open and listening for events
window.mainloop()
