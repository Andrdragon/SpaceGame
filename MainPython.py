from tkinter import Tk, PhotoImage, Label, Button


# root:
root = Tk()
root.title("Охота на пришельцев")
root.resizable(False, False)

# background:
img = PhotoImage(file="planet.png")
bg = Label(root, image=img)
bg.pack()

# start:
root.mainloop()
