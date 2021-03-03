import tkinter as tk
import random

# CONSTANTS
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

colors=["red","blue","pink","black","green","brown"]


# GAME VARIABLE

# FUNCTIONS
def createOval1():
    global colors
    randCol=random.choice(colors)
    canvas.create_oval(300,100,400,200, fill=randCol)
def Ractangle():
    global colors
    randCol=random.choice(colors)
    canvas.create_rectangle(300,250,400,500, fill=randCol)

def clickOnC(event):
    canvas.after(20, lambda:createOval1())
def clickOnSpace(event):
    canvas.create_text(100,100, text="Hello my beloved friend and teacher")
    canvas.after(5000, lambda:createOval1())
    canvas.after(3000, lambda:Ractangle())
# CREATE GRAPHIC
windows = tk.Tk()
windows.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
canvas = tk.Canvas(windows)
canvas.pack(expand=True, fill="both")

#DRAW GRAPHIC

windows.bind("<c>", clickOnC)
windows.bind("<space>", clickOnSpace)


# Save the return value of the create


windows.mainloop()



# import tkinter as tk
# import random

# colors = ["red", "blue", "black", "yellow"]
# # function that displays hello world, but returns nothing
# def moveBalls():
#     global balls, directions
#     for i in range(len(balls)):
#         ball = balls[i]
#         position = canvas.coords(ball) # [x0, y0, x1, y1]
#         if position[2] > 600 or position[0]<0:
#             directions[i][0] = -directions[i][0]
#         if position[3] > 600 or position[1]<0:
#             directions[i][1] = -directions[i][1]
#         canvas.move(ball, directions[i][0], directions[i][1])
#     canvas.after(50, lambda:moveBalls())

# # Create an empty window
# root = tk.Tk()
# # Set TK window size to width 600 px and height 200 px
# root.geometry("600x600")
# # Create a frame in the window (frame is a container, like "div" in HTML)
# frame = tk.Frame()
# # Set the title of the frame
# frame.master.title("Hello PNC")
# canvas = tk.Canvas(frame)

# ball0 = canvas.create_oval(0,0,50,50,fill="red") #top left
# dx0 = random.randrange(1,15)
# dy0 = random.randrange(1,15)

# ball1 = canvas.create_oval(0, 550, 50, 600, fill = "blue") #bottom left
# dx1 = random.randrange(1,15)
# dy1 = random.randrange(-15,-1)

# ball2 = canvas.create_oval(550, 0, 600, 50, fill = "yellow") #top right
# dx2 = random.randrange(-15,-1)
# dy2 = random.randrange(1,15)

# ball3 = canvas.create_oval(550, 550, 600, 600, fill = "yellow") #bottom right
# dx3 = random.randrange(-15,-1)
# dy3 = random.randrange(-15,-1)


# balls = [ball0, ball1, ball2, ball3]
# directions = [[dx0,dy0],[dx1,dy1],[dx2,dy2],[dx3,dy3]]






# moveBalls()
# # pack means "draw what i put inside"
# canvas.pack(expand=True, fill='both')
# frame.pack(expand=True, fill='both')

# # Display all
# root.mainloop()