  # AddTen(n):  Adds 10 to the parameter n and returns the result
def addTen(n):
    n = n + 10
    return n
print (addTen(10))
  # DrawRectangle(Anyturtle, l, w):  Self Explanitory
import turtle
ole = turtle.Turtle()
for i in range(2):
    l = 100
    w = 50
    ole.forward(l)
    ole.right(90)
    ole.forward(w)
    ole.right(90)

  # DrawPoly(Anyturtle, n):  Will draw a regular polygon with 'n' sides of
polly = turtle.Turtle()
polly.forward(50)
polly.left(80)
polly.forward(50)
polly.left(70)
polly.forward(50)
polly.left(70)
polly.forward(50)
polly.left(70)
polly.forward(50)
turtle.done()
