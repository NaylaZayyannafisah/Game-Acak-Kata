from tkinter import *
from tkinter import messagebox
import tkinter
from PIL import ImageTk, Image

wts=open("C:\coding\python_programs\semester 2\Projek UAS Game Acak Kata\Projek UAS Game Acak Kata\settings.txt","r")
global fs
fs=int(wts.read())
print(fs)
wts.close()

def start_main_page():
    def start_game(args):
        main_window.destroy()
        if args == 1:
            from Options import Animals
            Animals.main()
        elif args == 2:
            from Options import Body_parts
            Body_parts.main()
        elif args == 3:
            from Options import Colour
            Colour.main()
        elif args == 4:
            from Options import Fruit
            Fruit.main()
        elif args == 5:
            from Options import Shapes
            Shapes.main()
        elif args == 6:
            from Options import Vegetable
            Vegetable.main()
        elif args == 7:
            from Options import Vehicles
            Vehicles.main()

    def option():

        lab_img1 = Button(
            main_window,
            text="Pilih Tipe",
            bg='#e6fff5',
            border=0,
            justify='center',
            font=("Winkle", 12)
        )

        sel_btn1 = Button(
            text="Hewan",
            width=18,
            borderwidth=8,
            font=("Winkle", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(1),
        )

        sel_btn2 = Button(
            text="Bagian Tubuh",
            width=18,
            borderwidth=8,
            font=("Winkle", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(2),
        )

        sel_btn3 = Button(
            text="Warna",
            width=18,
            borderwidth=8,
            font=("Winkle", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(3),
        )

        sel_btn4 = Button(
            text="Buah-buahan",
            width=18,
            borderwidth=8,
            font=("Winkle", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(4),
        )

        sel_btn5 = Button(
            text="Bangun Datar",
            width=18,
            borderwidth=8,
            font=("Winkle", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(5),
        )

        sel_btn6 = Button(
            text="Sayur-sayuran",
            width=18,
            borderwidth=8,
            font=("Winkle", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(6),
        )

        sel_btn7 = Button(
            text="Kendaraan",
            width=18,
            borderwidth=8,
            font=("Winkle", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(7),
        )
        lab_img1.grid(row=0, column=0, padx=20)
        sel_btn1.grid(row=0, column=4, pady=(10, 0), padx=50, )
        sel_btn2.grid(row=1, column=4, pady=(10, 0), padx=50, )
        sel_btn3.grid(row=2, column=4, pady=(10, 0), padx=50, )
        sel_btn4.grid(row=3, column=4, pady=(10, 0), padx=50, )
        sel_btn5.grid(row=4, column=4, pady=(10, 0), padx=50, )
        sel_btn6.grid(row=5, column=4, pady=(10, 0), padx=50, )
        sel_btn7.grid(row=6, column=4, pady=(10, 0), padx=50, )

    def show_option():
        start_btn.destroy()

        about_btn.destroy()

        exit_btn.destroy()

        label3.destroy()

        tombol_fullscreen.destroy()

        lab_img.destroy()
        option()

    main_window = Tk()

    main_window.geometry("500x500+500+150")
    main_window.resizable(0, 0)
    main_window.title("Tebak Kata")
    main_window.configure(background="#e6fff5")

    def message():
        tkinter.messagebox.showinfo('About','2110511045_Nayla Zayyannafisah Abida\n2110511052_Azriel Dwi Mahendra\n2110511060_Saripah\n')

    def togglefullscreen():
        global fs
        if fs==1:
            fs-=1
            tombol_fullscreen.configure(text="Aktifkan", font="Winkle")
            main_window.attributes("-fullscreen",False)
            print("Layar Penuh Dinonaktifkan")
            wts=open("settings.txt","w")
            wts.write("0")
            wts.close()
            
        elif fs==0:
            fs+=1
            tombol_fullscreen.configure(text="Nonaktifkan", font="Winkle")
            main_window.attributes("-fullscreen",True)
            print("Layar Penuh Diaktifkan")
            wts=open("settings.txt","w")
            wts.write("1")
            wts.close()
    

    # img1 = PhotoImage(file="back.png")

    lab_img = Label(
        main_window,
        text="-ˏ͛⑅ TEBAK KATA ⑅ˏ͛-",
        bg='#e6fff5',
        fg='#FF00FF',
        font=("Winkle", 40, "bold")
    )

    start_btn = Button(
        main_window,
        text="Mulai",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("Winkle", 13),
        cursor="hand2",
        command=show_option,
    )

    about_btn = Button(
        main_window,
        text="Info",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("Winkle", 13),
        cursor="hand2",
        command=message
    )

    exit_btn = Button(
        main_window,
        text="Keluar",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("Winkle", 13),
        cursor="hand2",
        command=main_window.quit
    )
    
    label3 = Label(
        main_window, 
        text="\n\nPengaturan Layar Penuh", 
        width=20,
        borderwidth=10,
        fg="#2e5746",
        bg='#e6fff5',
        font=("Winkle", 13, "bold"),
        cursor="hand2",
    )
    
    tombol_fullscreen = Button(
        main_window, 
        text="",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg='#99ffd6',
        font=("Winkle", 13),
        cursor="hand2", 
        command=togglefullscreen
    )
    if fs==0:
        main_window.attributes("-fullscreen",False)
        tombol_fullscreen.configure(text="Aktifkan", font="Winkle")
    elif fs==1:
        main_window.attributes("-fullscreen",True)
        tombol_fullscreen.configure(text="Nonaktifkan", font="Winkle")
    
    lab_img.pack(pady=(50, 0))
    start_btn.pack(pady=(30, 20))
    about_btn.pack(pady=(10, 20))
    exit_btn.pack(pady=(10, 20))
    label3.pack()
    tombol_fullscreen.pack(padx=(50))

    main_window.mainloop()


start_main_page()
