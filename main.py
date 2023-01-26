from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
               'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
               'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    input_password.insert(0, password)
    pyperclip.copy(password)





# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
def save():
    website = input_website.get()
    email = input_email.get()
    password = input_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message=f"Please make sure you haven't left any fields empty.")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                      f" \nPassword: {password} \nIs it ok save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                input_website.delete(0, END)
                input_password.delete(0, END)




window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=logo_img)
canvas.grid(column=1, row=0)

# label
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# Entry
input_website = Entry(width=36)
print(input_website.get())
input_website.grid(column=1, row=1, columnspan=2)
input_website.focus()

input_email = Entry(width=36)
print(input_email.get())
input_email.grid(column=1, row=2, columnspan=2)
input_email.insert(0, "natalya@gmail.com")


input_password = Entry(width=19)
print(input_website.get())
input_password.grid(column=1, row=3)

# Button
button = Button(text="General Password", command=generate_password)
button.grid(column=2, row=3)

button = Button(text="Add", width=34, command=save)
button.grid(column=1, row=4, columnspan=2)


window.mainloop()
