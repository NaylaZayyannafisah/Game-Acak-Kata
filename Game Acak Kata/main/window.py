from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("600x600")
window.configure(bg = "#e2dad7")
canvas = Canvas(
    window,
    bg = "#e2dad7",
    height = 600,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    286.5, 400.0,
    image=background_img)

canvas.create_text(
    305.0, 108.0,
    text = "ACAK KATA",
    fill = "#fffadd",
    font = ("Winkle-Regular", int(48.0)))

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 214, y = 338,
    width = 160,
    height = 48)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 214, y = 421,
    width = 160,
    height = 48)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 212, y = 253,
    width = 160,
    height = 48)

window.resizable(False, False)
window.mainloop()
