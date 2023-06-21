from tkinter import *
from random import *
from tkinter import messagebox
import time

COLOUR_WORD = ['EARMH', 'UNKING', 'UIBR', 'UIJHA', 'AENYOR', 'NGUU', 'OORNAM', 'ATKLOC', 'NYVA', 'REMAH UDMA', 'SAME', 'AERPK',
               'AITHM', 'UTPIH', ]

COLOUR_ANSWER = ['MERAH', 'KUNING', 'BIRU', 'HIJAU', 'ORANYE', 'UNGU', 'MAROON', 'COKLAT', 'NAVY', 'MERAH MUDA', 'EMAS',
                 'PERAK', 'HITAM', 'PUTIH', ]


ran_num = randrange(0, (len(COLOUR_WORD)))
jumbled_rand_word = COLOUR_WORD[ran_num]

points = 0


def main():
    def back():
        my_window.destroy()
        import index
        index.start_main_page()

    def change():
        global ran_num
        ran_num = randrange(0, (len(COLOUR_WORD)))
        word.configure(text=COLOUR_WORD[ran_num])
        get_input.delete(0, END)
        ans_lab.configure(text="")

    def cheak():
        global points, ran_num
        user_word = get_input.get().upper()
        if user_word == COLOUR_ANSWER[ran_num]:
            points += 5
            score.configure(text="Poin: " + str(points))
            messagebox.showinfo('Benar', "Jawaban Benar.. Pertahankan!")
            ran_num = randrange(0, (len(COLOUR_WORD)))
            word.configure(text=COLOUR_WORD[ran_num])
            get_input.delete(0, END)
            ans_lab.configure(text="")
        else:
            messagebox.showerror("Error", "Jawaban Salah..Coba lagi!")
            get_input.delete(0, END)

    def show_answer():
        global points
        if points > 4:
            points -= 5
            score.configure(text="Poin: " + str(points))
            time.sleep(0.5)
            ans_lab.configure(text=COLOUR_ANSWER[ran_num])
        else:
            ans_lab.configure(text='Poin tidak cukup', font="Winkle")

    my_window = Tk()
    my_window.geometry("500x500+500+150")
    my_window.resizable(0, 0)
    my_window.title("Tebak Kata")
    my_window.configure(background="#e6fff5")
    #img1 = PhotoImage(file="back.png")

    lab_img1 = Button(
        my_window,
        #image=img1,
        text="Kembali",
        bg='#e6fff5',
        font="Winkle",
        border=0,
        justify='center',
        command=back,
    )
    lab_img1.pack(anchor='nw', pady=10, padx=10)

    score = Label(
        text="Poin:- 0",
        pady=10,
        bg="#e6fff5",
        fg="#000000",
        font="Arial  14 bold"
    )
    score.pack(anchor="n")

    word = Label(
        text=jumbled_rand_word,
        pady=10,
        bg="#e6fff5",
        fg="#000000",
        font="Winkle  30 bold"
    )
    word.pack()

    get_input = Entry(
        font="Winkle 26 bold",
        borderwidth=10,
        justify='center',
    )
    get_input.pack()

    submit = Button(
        text="Cek",
        width=18,
        borderwidth=8,
        font=("Winkle", 13),
        fg="#000000",
        bg="#99ffd6",
        command=cheak,
    )
    submit.pack(pady=(10, 20))

    change = Button(
        text="Ganti Kata",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("Winkle", 13),
        command=change,
    )
    change.pack()

    ans = Button(
        text="Jawaban",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("Winkle", 13),
        command=show_answer,
    )
    ans.pack(pady=(20, 10))

    ans_lab = Label(
        text="",
        bg="#e6fff5",
        fg="#000000",
        font="Winkle 15 bold",
    )
    ans_lab.pack()

    my_window.mainloop()
