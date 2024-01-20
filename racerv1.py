import random
from tkinter import *

root = Tk()
root.title("SIGN RACER")
root.geometry("400x200")

#character --> from cv
#need initialize

def start():
    WORDS = ("hackathon", "python", "sign", "language", "machine", "learning", "engineer", "computer")
    word = random.choice(WORDS)

    count = 0
    correct_ans = []
    length_word = len(word)
    lbl.config(text=word)

    while count < length_word:
        btn.pack_forget()  # Hide the "START" button when pressed
        character = input("char:")
        if character == word[count]:
            correct_ans.append(character)
            count += 1
            print(correct_ans)
            lbl.config(text=word[count:])
            if character == word[-1]:
                btn.pack()

        

# label creation
lbl = Label(root, text="")
lbl.pack()

btn = Button(root, command=start, text="START")
btn.pack()

root.mainloop()