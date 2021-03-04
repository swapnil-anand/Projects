from tkinter import *


def popupmsg(msg):
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

def submit():
    message1 = entry_1.get()
    key1 = int(entry_2.get())
    message_list = message1.split(" ")
    result = ""

    if CheckVar1.get() == 1 and CheckVar2.get() == 0:
        for i in message_list:
            result_temp = ''.join(chr(ord(j) + key1) for j in i)
            result = result + " "
            result = result + result_temp
    elif CheckVar1.get() == 0 and CheckVar2.get() == 1:
        for i in message_list:
            result_temp = ''.join(chr(ord(j) - key1) for j in i)
            result = result + " "
            result = result + result_temp
    else:
        popupmsg("Please Select only 1!")
    label_message = Label(top, text=result, font=('calibre', 10, 'normal'),
                          bg="light blue")
    label_message.place(relx=0.47, rely=0.7)
    return result


top = Tk()
top.title("Message Encode Decode")
top.configure(backgroun="light blue")
top.resizable(False, False)


message = StringVar()
key = IntVar()
top.geometry("400x200")
# label for username
label_input = Label(top, text="Enter the Message to be Encrypted", bg="light blue")
entry_1 = Entry(top, textvariable=message,
                font=('calibre', 10, 'normal'))

# label for key
label_key = Label(top, text="Enter the key", bg="light blue")
entry_2 = Entry(top, textvariable=key,
                font=('calibre', 10, 'normal'))

# creating the checkbox for the Encrypt and decrypt option
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text="Encrypt", variable=CheckVar1, bg="light blue",
                 onvalue=1, offvalue=0, height=2)
C2 = Checkbutton(top, text="Decrypt", variable=CheckVar2, bg="light blue",
                 onvalue=1, offvalue=0, height=2)

# Submit Button
submit_button = Button(top, text="Submit", bg="light Green",
                       width=20, command=submit, padx=5, pady=5)

label_input.grid(row=0, column=0)
entry_1.grid(row=0, column=1)
label_key.grid(row=1, column=0)
entry_2.grid(row=1, column=1)
C1.grid(row=2, column=0)
C2.grid(row=2, column=1)
submit_button.place(relx=0.3, rely=0.4)

label_output = Label(top, text="The message after operation is ", bg="light blue")
label_output.place(relx=0.03, rely=0.7)

top.mainloop()
