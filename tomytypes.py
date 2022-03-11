from tkinter import *
import random

root = Tk()

current_word = 1

def clear_text():
    entry.delete(0, END)

def open_win():
    new = Toplevel(root)
    new.geometry('1000x200')
    new.title("Start typing and after your first word we will start counting your time.")
    Label(new, text = "Start typing and after your first word we will start counting your time.", font = ("arial", 25)).pack(pady=30)
    Label(new, text = "You can now close this window.", font = ("arial", 25)).pack(pady=30)
    new.lift()
    new.attributes("-topmost", True)

# Open the file in read mode
with open("validwords.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
    # print random string
    word1 = str(random.choice(words))
    word2 = random.choice(words)
    word3 = random.choice(words)
    word4 = random.choice(words)
    word5 = random.choice(words)
    word6 = random.choice(words)
    word7 = random.choice(words)
    word8 = random.choice(words)
    word9 = random.choice(words)
    word10 = random.choice(words)
    word11 = random.choice(words)
    word12 = random.choice(words)
    word13 = random.choice(words)
    word14 = random.choice(words)
    word15 = random.choice(words)
    word16 = random.choice(words)
    word17 = random.choice(words)
    word18 = random.choice(words)
    word19 = random.choice(words)
    word20 = random.choice(words)
    word21 = random.choice(words)
    word22 = random.choice(words)
    word23 = random.choice(words)
    word24 = random.choice(words)
    word25 = random.choice(words)
    word26 = random.choice(words)
    word27 = random.choice(words)
    word28 = random.choice(words)

#!cahnge it from word 1
def colorchange(user_word, filler):
    global current_word
    print(str(user_word) + " "+ str(word1))
    if user_word == word1:
        current_word = current_word + 1
        filler.configure(fg = "white")
        print("correct")
    clear_text()

def excs(event):
    user_word = str(entry.get())
    user_word = user_word.strip(" ")
    if current_word == 1:
        colorchange(user_word, lable1)
    elif current_word == 2:
        colorchange(user_word, lable2)



root.bind("<space>", excs)

lablestart = Label(root, text = "")
lablestart.grid(row=0,column=0)

entry = Entry(root, width=10)
entry.grid(row = 1, column = 0)


lable1 = Label(root, text = word1)
lable2 = Label(root, text = word2)
lable3 = Label(root, text = word3)
lable4 = Label(root, text = word4)
lable5 = Label(root, text = word5)
lable6 = Label(root, text = word6)
lable7 = Label(root, text = word7)
lable8 = Label(root, text = word8)
lable9 = Label(root, text = word9)
lable10 = Label(root, text = word10)
lable11 = Label(root, text = word11)
lable12 = Label(root, text = word12)
lable13 = Label(root, text = word13)
lable14 = Label(root, text = word14)
lable15 = Label(root, text = word15)
lable16 = Label(root, text = word16)
lable17 = Label(root, text = word17)
lable18 = Label(root, text = word18)
lable19 = Label(root, text = word19)
lable20 = Label(root, text = word20)
lable21 = Label(root, text = word21)
lable22 = Label(root, text = word22)
lable23 = Label(root, text = word23)
lable24 = Label(root, text = word24)
lable25 = Label(root, text = word25)
lable26 = Label(root, text = word26)
lable27 = Label(root, text = word27)
lable28 = Label(root, text = word28)

lable1.grid(row=1, column=1)
lable2.grid(row=1, column=2)
lable3.grid(row=1, column=3)
lable4.grid(row=1, column=4)
lable5.grid(row=1, column=5)
lable6.grid(row=1, column=6)
lable7.grid(row=1, column=7)
lable8.grid(row=1, column=8)
lable9.grid(row=1, column=9)
lable11.grid(row=1, column=10)
lable11.grid(row=3, column=0)
lable12.grid(row=3, column=1)
lable13.grid(row=3, column=2)
lable14.grid(row=3, column=3)
lable15.grid(row=3, column=4)
lable16.grid(row=3, column=5)
lable17.grid(row=3, column=6)
lable18.grid(row=3, column=7)
lable19.grid(row=3, column=8)
lable20.grid(row=3, column=9)
lable21.grid(row=4, column=0)
lable22.grid(row=4, column=1)
lable23.grid(row=4, column=2)
lable24.grid(row=4, column=3)
lable25.grid(row=4, column=4)
lable26.grid(row=4, column=5)
lable27.grid(row=4, column=6)
lable28.grid(row=4, column=7)

open_win()
root.mainloop()