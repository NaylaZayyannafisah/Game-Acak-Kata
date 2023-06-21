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

background_img = PhotoImage(file = f"C:\coding\python_programs\semester 2\Game Acak Kata\gameplay/background.png")
background = canvas.create_image(
    286.5, 400.0,
    image=background_img)

img0 = PhotoImage(file = f"C:\coding\python_programs\semester 2\Game Acak Kata\gameplay\img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 30, y = 35,
    width = 129,
    height = 35)

img1 = PhotoImage(file = f"C:\coding\python_programs\semester 2\Game Acak Kata\gameplay\img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 224, y = 387,
    width = 150,
    height = 40)

img2 = PhotoImage(file = f"C:\coding\python_programs\semester 2\Game Acak Kata\gameplay\img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 224, y = 451,
    width = 150,
    height = 40)

img3 = PhotoImage(file = f"C:\coding\python_programs\semester 2\Game Acak Kata\gameplay\img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 224, y = 513,
    width = 150,
    height = 40)

entry0_img = PhotoImage(file = f"C:\coding\python_programs\semester 2\Game Acak Kata\gameplay\img_textBox0.png")
entry0_bg = canvas.create_image(
    300.0, 313.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry0.place(
    x = 120, y = 281,
    width = 360,
    height = 62)

window.resizable(False, False)
window.mainloop()
