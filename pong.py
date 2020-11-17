import turtle

# create a window
wn = turtle.Screen()
wn.title("Pong game by Sunil")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)    #stops the window from updating

# Main game loop
while True:
    wn.update()