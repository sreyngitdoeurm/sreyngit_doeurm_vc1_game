import tkinter as tk
from tkinter import messagebox
import winsound

# Create an empty window
root = tk.Tk()
# Set TK window size to width 600 px and height 200 px
root.geometry("700x700")
# Create a frame in the window (frame is a container, like "div" in HTML)
frame = tk.Frame()
# Set the title of the frame
frame.master.title("SREYNGIT GAME")

# HERE YOU CAN START TO DRAW
# canvas is like "svg tag" in HTML, it allows user to draw shapes
# set image ennemies(2), player("p"), diamond("d") and time ("t")
player=tk.PhotoImage(file="player1.png")
ennemies=tk.PhotoImage(file="cov.png")
diamond=tk.PhotoImage(file="diamond.png")
signExit=tk.PhotoImage(file="signExit.png")
life=tk.PhotoImage(file="life.png")
bg=tk.PhotoImage(file="bg.png")
#display image


# 0 is empty, p is player, 1 is wall, d is diamond, t is life, 2 is ennemy, w is way
canvas = tk.Canvas(frame)
grid = [[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [0,1,0,1,"l",0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        ["p",0,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1],
        [1,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
        [1,0,0,1,0,1,0,0,0,1,0,1,2,0,"l",1,0,1,0,1],
        [1,0,0,0,0,1,1,0,1,1,0,1,1,1,1,1,0,1,0,1],
        [1,0,1,1,0,0,1,0,0,0,2,0,0,0,0,1,0,1,0,1],
        [1,1,1,0,0,2,1,0,1,1,1,1,1,"l",0,1,0,1,0,1],
        [1,0,1,0,1,"l",1,1,1,"d",0,0,1,1,0,1,0,0,0,1],
        [1,0,1,0,1,1,1,0,1,1,1,0,1,0,0,1,1,1,0,1],
        [1,0,0,0,0,0,0,0,1,0,0,2,1,0,0,1,"l",1,0,1],
        [1,0,1,1,1,1,1,1,1,0,1,1,1,0,0,1,2,1,0,1],
        [1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,1,1,1,1,0,1,0,0,1,0,1,0,1],
        [1,0,1,"l",0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
        [1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1],
        [1,0,2,0,0,0,0,1,"l",0,0,0,0,2,1,2,0,0,0,"w"],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3]]
# variables
size = 30
numberOfLife = 2
hasDiamond = False
numberOfDiamond=0
# drawing
def arrayToDrawing(array, size):
    global player, ennemies, dimond, forest, bg,numberOfLife, numberOfDiamond
    canvas.delete("all")
    canvas.create_image(0,0, anchor="nw", image=bg)
    number=0
    for index in array:
        number+=1
        for i in range(len(index)):
            x0 = i*size
            y0 = 30*number
            x1 = x0 + size
            y1 = y0 + size
            if index[i] == 1:
                canvas.create_rectangle(x0, y0, x1, y1, fill="white")
            elif index[i]==2:
                canvas.create_image(x0+15, y0+10, image=ennemies)
            elif index[i]=="p":
                canvas.create_image(x0+15, y0+10, image=player)
            elif index[i]=="d":
                canvas.create_image(x0+15, y0+15, image=diamond)
            elif index[i]=="l":
                canvas.create_image(x0+15,y0+15, image=life)
            elif index[i]=="w":
                canvas.create_rectangle(x0,y0,x1,y1, outline="cyan", fill=None)
            elif index[i]==3:
                canvas.create_image(x0-15,y0-15, image=signExit)
            else:
                canvas.create_rectangle(x0, y0, x1, y1, outline="cyan", fill=None)
    canvas.create_image(300, 10, image=life)
    canvas.create_image(500, 10, image=diamond)
    canvas.create_text(330, 10, text=str(numberOfLife))
    canvas.create_text(530, 10, text=str(numberOfDiamond))
    canvas.create_text(40,10, text="level: easy")
# move player
def getPlayerPosition(grid):
    canvas.delete("all")
    for n in range(len(grid)):
        for i in range(len(grid[n])):
            if grid[n][i]=="p":
                playerRow = n
                playerCol = i
    return ([playerRow, playerCol])

def moveLeft(event):
    global grid, numberOfLife, hasDiamond, numberOfDiamond
    playerRow = getPlayerPosition(grid)[0]
    playerCol = getPlayerPosition(grid)[1]
    if playerCol > 0:
        if  grid[playerRow][playerCol-1] ==0:
            grid[playerRow][playerCol]=0
            grid[playerRow][playerCol-1]="p"
        elif grid[playerRow][playerCol-1]=="l":
            grid[playerRow][playerCol]=0
            grid[playerRow][playerCol-1]="p"
            numberOfLife += 1
        elif grid[playerRow][playerCol-1]==2:
            grid[playerRow][playerCol]=0
            grid[playerRow][playerCol-1]="p"
            winsound.PlaySound("fall3.wav", winsound.SND_FILENAME)
            numberOfLife -= 1
        elif grid[playerRow][playerCol-1]=="d":
            grid[playerRow][playerCol]=0
            grid[playerRow][playerCol-1]="p"
            winsound.PlaySound("getlife.wav", winsound.SND_FILENAME)
            numberOfDiamond+=1
            hasDiamond = True
        elif grid[playerRow][playerCol-1]=="w" and hasDiamond:
            grid[playerRow][playerCol]=0
            grid[playerRow][playerCol-1]="p"
            winsound.PlaySound("win.wav", winsound.SND_FILENAME)
            messagebox.showinfo(message="you win")
    if numberOfLife<1:
        winsound.PlaySound("gameover.wav", winsound.SND_FILENAME)
        messagebox.showinfo(message="Game Over")
            
    winsound.PlaySound("walk.wav", winsound.SND_FILENAME)
    arrayToDrawing(grid,size)

def moveRight(event):
    global grid, numberOfLife,hasDiamond, numberOfDiamond
    playerRow = getPlayerPosition(grid)[0]
    playerCol = getPlayerPosition(grid)[1]
    if playerCol < len(grid[0])-1:
        if  grid[playerRow][playerCol+1] ==0:
            grid[playerRow][playerCol]=0
            grid[playerRow][playerCol+1]="p"
        elif grid[playerRow][playerCol+1]=="l":
            grid[playerRow][playerCol]=0
            grid[playerRow][playerCol+1]="p"
            numberOfLife += 1
        elif grid[playerRow][playerCol+1]==2:
            grid[playerRow][playerCol]=0
            grid[playerRow][playerCol+1]="p"
            winsound.PlaySound("fall3.wav", winsound.SND_FILENAME)
            numberOfLife -= 1
        elif grid[playerRow][playerCol+1]=="d":
            grid[playerRow][playerCol]=0
            grid[playerRow][playerCol+1]="p"
            winsound.PlaySound("getlife.wav", winsound.SND_FILENAME)
            numberOfDiamond+=1
            hasDiamond = True
        elif grid[playerRow][playerCol+1]=="w" and hasDiamond:
            grid[playerRow][playerCol]=0
            grid[playerRow][playerCol+1]="p"
            winsound.PlaySound("win.wav", winsound.SND_FILENAME)
            messagebox.showinfo(message="you win")
    if numberOfLife<1:
        winsound.PlaySound("gameover.wav", winsound.SND_FILENAME)
        messagebox.showinfo(message="Game Over")
    winsound.PlaySound("walk.wav", winsound.SND_FILENAME)
    arrayToDrawing(grid,size)
def moveUp(event):
    global grid, numberOfLife,hasDiamond,numberOfDiamond
    playerRow = getPlayerPosition(grid)[0]
    playerCol = getPlayerPosition(grid)[1]
    if playerRow >0:
        if  grid[playerRow-1][playerCol] ==0:
            grid[playerRow][playerCol]=0
            grid[playerRow-1][playerCol]="p"
        elif grid[playerRow-1][playerCol]=="l":
            grid[playerRow][playerCol]=0
            grid[playerRow-1][playerCol]="p"
            numberOfLife += 1
        elif grid[playerRow-1][playerCol]==2:
            grid[playerRow][playerCol]=0
            grid[playerRow-1][playerCol]="p"
            winsound.PlaySound("fall3.wav", winsound.SND_FILENAME)
            numberOfLife -= 1
        elif grid[playerRow-1][playerCol]=="d":
            grid[playerRow][playerCol]=0
            grid[playerRow-1][playerCol]="p"
            winsound.PlaySound("getlife.wav", winsound.SND_FILENAME)
            numberOfDiamond+=1
            hasDiamond = True
        elif grid[playerRow-1][playerCol]=="w" and hasDiamond:
            grid[playerRow][playerCol]=0
            grid[playerRow-1][playerCol]="p"
            winsound.PlaySound("win.wav", winsound.SND_FILENAME)
            messagebox.showinfo(message="you win")
    if numberOfLife<1:
        winsound.PlaySound("gameover.wav", winsound.SND_FILENAME)
        messagebox.showinfo(message="Game Over")
    winsound.PlaySound("walk.wav", winsound.SND_FILENAME)
    arrayToDrawing(grid,size)
def moveDown(event):
    global grid, numberOfLife,hasDiamond, numberOfDiamond
    playerRow = getPlayerPosition(grid)[0]
    playerCol = getPlayerPosition(grid)[1]
    if playerRow <len(grid)-1:
        if  grid[playerRow+1][playerCol] ==0:
            grid[playerRow][playerCol]=0
            grid[playerRow+1][playerCol]="p"
        elif grid[playerRow+1][playerCol]=="l":
            grid[playerRow][playerCol]=0
            grid[playerRow+1][playerCol]="p"
            numberOfLife += 1
        elif grid[playerRow+1][playerCol]==2:
            grid[playerRow][playerCol]=0
            grid[playerRow+1][playerCol]="p"
            winsound.PlaySound("fall3.wav", winsound.SND_FILENAME)
            numberOfLife -= 1
        elif grid[playerRow+1][playerCol]=="d":
            grid[playerRow][playerCol]=0
            grid[playerRow+1][playerCol]="p"
            winsound.PlaySound("getlife.wav", winsound.SND_FILENAME)
            numberOfDiamond+=1
            hasDiamond = True
        elif grid[playerRow+1][playerCol]=="w" and hasDiamond:
            grid[playerRow][playerCol]=0
            grid[playerRow+1][playerCol]="p"
            winsound.PlaySound("win.wav", winsound.SND_FILENAME)
            messagebox.showinfo(message="you win")
    if numberOfLife<1:
        winsound.PlaySound("gameover.wav", winsound.SND_FILENAME)
        messagebox.showinfo(message="Game Over")
    winsound.PlaySound("walk.wav", winsound.SND_FILENAME)
    arrayToDrawing(grid,size)
# move enemies
def getEnemyPosition(grid):
    enemiesPosition=[]
    for n in range(len(grid)):
        for i in range(len(grid[n])):
            if grid[n][i]==2:
                enemyRow=n
                enemyCol=i
        enemiesPosition.append([enemyRow,enemyCol])
    return (enemiesPosition)
# move enemies
def moveEnemies():
    global grid
    enemyRow=getEnemyPosition(grid)[0]
    enemyCol=getEnemyPosition(grid)[1]
    if grid[enemyRow][enemyCol+1]!=1:
        canvas.move()
# pack means "draw what i put inside"
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.bind("<Left>", moveLeft)
root.bind("<Right>", moveRight)
root.bind("<Up>", moveUp)
root.bind("<Down>", moveDown)
# displayWin()
arrayToDrawing(grid,size)

# Display all
root.mainloop()