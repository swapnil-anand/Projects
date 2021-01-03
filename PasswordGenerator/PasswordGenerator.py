from tkinter import *
import random

def generate():
    upper_case_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                              'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lower_case_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                              'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    special_character = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', '-', '.', '/', ':', ';', '<', '=',
                              '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    str = ""
    if CheckVar1.get() == 1 and CheckVar2.get() == 0:
        while 1:
            upper_ind = random.randint(0, 25)
            lower_ind = random.randint(0, 25)
            special_ind = random.randint(0, 28)
            number_ind = random.randint(0, 9)
            str = str + upper_case_letter[upper_ind] + lower_case_letter[lower_ind] + numbers[
                number_ind] + special_character[special_ind]
            if len(str) == 4:
                break
            else:
                continue
    elif CheckVar1.get() == 0 and CheckVar2.get() == 1:
        while 1:
            upper_ind = random.randint(0, 25)
            lower_ind = random.randint(0, 25)
            special_ind = random.randint(0, 28)
            number_ind = random.randint(0, 9)
            str = str + upper_case_letter[upper_ind] + lower_case_letter[lower_ind] + numbers[
                number_ind] + special_character[special_ind]
            if len(str) == 8:
                break
            else:
                continue
    else:
        popup_window("Please choose anyone of the two message")

    string = list(str)
    random.shuffle(string)

    output = Label(top, text=''.join(string), bg="light blue")
    output.grid(row=1, column=1)

def popup_window(msg):
    popup = Tk()
    popup.title("Error 002!")
    popup.configure(background="light blue")
    popup.resizable(False, False)
    popup.geometry("400x100")
    message_label = Label(popup, text=msg, bg="light blue", )
    message_label.place(relx=0.5, rely=0.5, anchor="center")
    okay_button = Button(popup, text="Okay", command=popup.destroy, bg="light Green")
    okay_button.place(relx=0.45, rely=0.7)
    popup.mainloop()

top = Tk()
top.geometry("300x200")
top.resizable(False, False)
top.title("Password Generator")
top.configure(background="light blue")

# Creating the label for 4 character and 8 character password
messsage = Label(top, text='Choose the no of characters', bg="light blue")
# Creating the 4 bit and 8 bit checkbox
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text="4 bit", variable=CheckVar1,
                 onvalue=1, offvalue=0, bg="light blue")
C2 = Checkbutton(top, text="8 bit", variable=CheckVar2,
                 onvalue=1, offvalue=0, bg="light blue")
# Creating the Generate button
gen_butt = Button(top, text="Generate Password", command=generate, bg="light Green")

# Creating the output label for the password
display_label = Label(top, text="Password is ", bg="light blue")


messsage.grid(row=0, column=0)
C1.grid(row=0, column=1)
C2.grid(row=0, column=2)
display_label.grid(row=1, column=0)
gen_butt.place(relx=0.3, rely=0.3)

top.mainloop()
