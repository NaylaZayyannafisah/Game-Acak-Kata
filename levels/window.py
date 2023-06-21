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

background_img = PhotoImage(file = f"C:\coding\python_programs\semester 2\Game Acak Kata\levels/background.png")
background = canvas.create_image(
    286.5, 400.0,
    image=background_img)

img0 = PhotoImage(file = f"C:\coding\python_programs\semester 2\Game Acak Kata\levels\img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 225, y = 111,
    width = 150,
    height = 40)

img1 = PhotoImage(file = f"C:\coding\python_programs\semester 2\Game Acak Kata\levels\img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 225, y = 173,
    width = 150,
    height = 40)

img2 = PhotoImage(file = f"C:\coding\python_programs\semester 2\Game Acak Kata\levels\img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 225, y = 235,
    width = 150,
    height = 40)

img3 = PhotoImage(file = f"C:\coding\python_programs\semester 2\Game Acak Kata\levels\img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 225, y = 297,
    width = 150,
    height = 40)

img4 = PhotoImage(file = f"C:\coding\python_programs\semester 2\Game Acak Kata\levels\img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 225, y = 359,
    width = 150,
    height = 40)

img5 = PhotoImage(file = f"C:\coding\python_programs\semester 2\Game Acak Kata\levels\img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b5.place(
    x = 225, y = 421,
    width = 150,
    height = 40)

img6 = PhotoImage(file = f"C:\coding\python_programs\semester 2\Game Acak Kata\levels\img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b6.place(
    x = 225, y = 483,
    width = 150,
    height = 40)

canvas.create_text(
    89.5, 62.5,
    text = "Pilih Tipe",
    fill = "#000000",
    font = ("Winkle-Regular", int(24.0)))

window.resizable(False, False)
window.mainloop()
