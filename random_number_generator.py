import tkinter as tk
from random import randrange


def main():
    WIN = tk.Tk()
    WIN.title("RANDOM NUMBER GENERATOR")
    WIN.geometry("400x600")
    WIN_BG = "#1abc9c"
    WIN.configure(bg=WIN_BG)
    FONT = "Roboto"

    prompt = tk.Label(WIN, text="Random Number Generator", font=FONT)
    prompt.place(x=80, y=10)

    label = tk.Label(WIN, text="Choose the number of digits", font=FONT)
    label.place(x=80, y=60)

    display_num = tk.Label(WIN, text="Number", font=FONT)
    display_num.place(x=165, y=300)

    num_of_digits = tk.IntVar()
    slide = tk.Scale(WIN, variable=num_of_digits, orient="horizontal", from_=1, to=7)
    slide.place(x=155, y=100)

    def randomise():
        digits = num_of_digits.get()
        random_num = None

        if digits == 1:
            random_num = randrange(1, 10)
            display_num.config(text=str(random_num))
        elif digits == 2:
            random_num = randrange(10, 100)
            display_num.config(text=str(random_num))
        elif digits == 3:
            random_num = randrange(100, 1000)
            display_num.config(text=str(random_num))
        elif digits == 4:
            random_num = randrange(1000, 10000)
            display_num.config(text=str(random_num))
        elif digits == 5:
            random_num = randrange(10000, 100000)
            display_num.config(text=str(random_num))
        elif digits == 6:
            random_num = randrange(100000, 1000000)
            display_num.config(text=str(random_num))
        elif digits == 7:
            random_num = randrange(1000000, 10000000)
            display_num.config(text=str(random_num))

    randomise_button = tk.Button(WIN, text="Randomise", font=FONT, command=randomise)
    randomise_button.place(x=150, y=500)

    WIN.mainloop()


if __name__ == "__main__":
    main()
