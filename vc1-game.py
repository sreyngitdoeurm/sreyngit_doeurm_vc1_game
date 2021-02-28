import tkinter as tk

# Create an empty window
root = tk.Tk()
# Set TK window size to width 600 px and height 200 px
root.geometry("600x600")
# Create a frame in the window (frame is a container, like "div" in HTML)
frame = tk.Frame()
# Set the title of the frame
frame.master.title("SREYNGIT GAME")

# HERE YOU CAN START TO DRAW
# canvas is like "svg tag" in HTML, it allows user to draw shapes


# 0 is empty, p is player, 1 is wall, d is diamond, t is life, 2 is ennemy
canvas = tk.Canvas(frame)
grid = [[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [0,"p",0,1,"t",0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [0,0,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1],
        [0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
        [1,0,0,1,0,1,0,0,0,1,0,1,2,0,"t",1,0,1,0,1],
        [1,0,0,0,0,1,1,0,1,1,0,1,1,1,1,1,0,1,0,1],
        [1,0,1,1,0,0,1,0,0,0,2,0,0,0,0,1,0,1,0,1],
        [1,1,1,0,0,2,1,0,1,1,1,1,1,"t",0,1,0,1,0,1],
        [1,0,1,0,1,"t",1,1,1,"d",0,0,1,1,0,1,0,0,0,1],
        [1,0,1,0,1,1,1,0,1,1,1,0,1,0,0,1,1,1,0,1],
        [1,0,0,0,0,0,0,0,1,0,0,2,1,0,0,1,"t",1,0,1],
        [1,0,1,1,1,1,1,1,1,0,1,1,1,0,0,1,0,1,0,1],
        [1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,1,1,1,1,0,1,0,0,1,0,1,0,1],
        [1,0,1,"t",0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
        [1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,"w"],
        [1,0,0,0,0,0,0,1,"t",0,0,0,0,2,1,2,0,0,0,"w"],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
# squareSize = #choose the appropriate size of the squares
square_size = 30

# VARIABLES
def arrayToDrawing(array, size):
    number=0
    for index in array:
        number+=1
        for i in range(len(index)):
            x0 = i*size
            y0 = 30*number
            x1 = x0 + size
            y1 = y0 + size
            if index[i] == 1:
                canvas.create_rectangle(x0, y0, x1, y1, outline="orange", fill = "blue")
            elif index[i]==2:
                canvas.create_oval(x0,y0,x1,y1, fill="yellow")
            elif index[i]=="p":
                canvas.create_oval(x0,y0,x1,y1, fill="black")
            elif index[i]=="d":
                canvas.create_oval(x0,y0,x1,y1, fill="green")
            elif index[i]=="t":
                canvas.create_oval(x0,y0,x1,y1, fill="red")
            elif index[i]=="w":
                canvas.create_rectangle(x0,y0,x1,y1, outline="pink", fill="pink")
            else:
                canvas.create_rectangle(x0, y0, x1, y1, outline="cyan", fill = "cyan")

def getPlayerPosition(grid):
    for n in range(len(grid)):
        for i in range(len(grid[n])):
            if grid[n][i]=="p":
                playerRow = n
                playerCol = i
    return ([playerRow, playerCol])


def moveLeft(event):
    global grid
    playerRow = getPlayerPosition(grid)[0]
    playerCol = getPlayerPosition(grid)[1]
    if playerCol > 0:
        if  grid[playerRow][playerCol-1] !=1:
            grid[playerRow][playerCol]=0
            grid[playerRow][playerCol-1]="p"
            arrayToDrawing(grid, square_size)

def moveRight(event):
    global grid
    playerRow = getPlayerPosition(grid)[0]
    playerCol = getPlayerPosition(grid)[1]
    if playerCol < len(grid[0])-1:
        if  grid[playerRow][playerCol+1] !=1:
            grid[playerRow][playerCol]=0
            grid[playerRow][playerCol+1]="p"
            arrayToDrawing(grid, square_size)

    
def moveUp(event):
    global grid
    playerRow = getPlayerPosition(grid)[0]
    playerCol = getPlayerPosition(grid)[1]
    if playerRow >0:
        if  grid[playerRow-1][playerCol] != 1:
            grid[playerRow][playerCol]=0
            grid[playerRow-1][playerCol]="p"
        arrayToDrawing(grid, square_size)
def moveDown(event):
    global grid
    playerRow = getPlayerPosition(grid)[0]
    playerCol = getPlayerPosition(grid)[1]
    if playerRow<len(grid)-1:
        if  grid[playerRow+1][playerCol] !=1:
            grid[playerRow][playerCol]=0
            grid[playerRow+1][playerCol]="p"
        arrayToDrawing(grid, square_size)
# pack means "draw what i put inside"
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.bind("<Left>", moveLeft)
root.bind("<Right>", moveRight)
root.bind("<Up>", moveUp)
root.bind("<Down>", moveDown)

arrayToDrawing(grid, square_size)
# Display all
root.mainloop()