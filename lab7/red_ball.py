from tkinter import *

def move_up(event):
    if label.winfo_y() - 10 >= 0:
        label.place(x=label.winfo_x(), y=label.winfo_y()-10)

def move_down(event):
    if label.winfo_y() + label.winfo_height() + 10 <= window.winfo_height():
        label.place(x=label.winfo_x(), y=label.winfo_y()+10)

def move_left(event):
    if label.winfo_x() - 10 >= 0:
        label.place(x=label.winfo_x()-10, y=label.winfo_y())

def move_right(event):
    if label.winfo_x() + label.winfo_width() + 10 <= window.winfo_width():
        label.place(x=label.winfo_x()+10, y=label.winfo_y())

window = Tk()
window.geometry("50x50")

window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)

myimage = PhotoImage(file='ball.png').subsample(20, 20)
label = Label(window, image=myimage)
label.place(x=0, y=0)

window.mainloop()