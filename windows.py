from apigui import *
from tkinter import *

def main():
    root = Tk()
    top = Toplevel(root)
    window1 = Window(root, "OK2", "500x500", "Timmy")
    window2 = Window(top, "OK2", "500x500", "Tim")
    #top2 = Toplevel(root)
    window1 = Window(top)
    #window2 = Window(top2, "OK2", "500x500", "Tim")
    root.mainloop()

    return None

def main2():
    root = Toplevel()
    window2 = Window(root, "OK2", "500x500", "Tim")

    return None

main()