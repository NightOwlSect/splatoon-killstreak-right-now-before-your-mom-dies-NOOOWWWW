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

def tree2(a_turtle, size):
  a_turtle.forward(size)

  a_turtle.left(25)
  tree1(a_turtle, size*0.65)
  a_turtle.right(25)
  a_turtle.right(35)
  tree1(a_turtle, size*0.85)
  a_turtle.left(35)

  a_turtle.backward(size)

tree1(turtles[0], 100)
tree2(turtles[1], 100)
#tree3(turtles[2], 100)

# Keep the window open and listening for events
window.mainloop()
