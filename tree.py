import turtle

# Set up the screen window
window = turtle.Screen()

# Create a visible turtle object
turtles = [turtle.Turtle(), turtle.Turtle(), turtle.Turtle()]
for i in range(3):
  turtles[i].teleport(100*i - 100, -80)
  turtles[i].setheading(90)

def tree1(a_turtle, size):
  a_turtle.forward(size)
  a_turtle.backward(size)

def tree(a_turtle, level, size):
  a_turtle.forward(size)
  if level>1:

    a_turtle.left(25)
    tree(a_turtle, level-1, size*0.65)
    a_turtle.right(25)
    a_turtle.right(35)
    tree(a_turtle,level-1, size*0.85)
    a_turtle.left(35)

  a_turtle.backward(size)

tree(turtles[0], 4, 100)
tree(turtles[1],8, 100)
tree(turtles[2],12, 100)

# Keep the window open and listening for events
window.mainloop()
