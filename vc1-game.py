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
canvas = tk.Canvas(frame)
grid = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1],
        [1,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
        [1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1],
        [1,0,0,0,0,1,1,0,1,1,0,1,1,1,1,1,0,1,0,1],
        [1,0,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,1],
        [1,1,1,0,0,0,1,0,1,1,1,1,1,0,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,1,1,0,0,0,1,1,0,1,0,0,0,1],
        [1,0,1,0,1,1,1,0,1,1,1,0,1,0,0,1,1,1,0,1],
        [1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,1,0,1],
        [1,0,1,1,1,1,1,1,1,0,1,1,1,0,0,1,0,1,0,1],
        [1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,1,1,1,1,0,1,0,0,1,0,1,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
        [1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1],
        [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1],
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
                canvas.create_rectangle(x0, y0, x1, y1, outline="blue", fill = "blue")
            else:
                canvas.create_rectangle(x0, y0, x1, y1, fill = "white")

# pack means "draw what i put inside"
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
arrayToDrawing(grid, square_size)
# Display all
root.mainloop()