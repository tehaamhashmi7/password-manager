import random
import tkinter
from tkinter import messagebox
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_password():
    password_entry.delete(0, tkinter.END)

    lo_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']
    up_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '/', ':', ';', '<', '=', '>', '?',
               '@', '[', ']', '^', '_', '`', '{', '|', '}']

    random_pass = []

    for i in range(3):
        sm = random.choice(lo_letters)
        random_pass.append(sm)

        cp = random.choice(up_letters)
        random_pass.append(cp)

        num = random.choice(numbers)
        random_pass.append(num)

        sym = random.choice(symbols)
        random_pass.append(sym)

    random.shuffle(random_pass)

    gen_pass = ""

    for item in random_pass:
        gen_pass += item

    password_entry.insert(0, gen_pass)


# --------------------- SEARCH FUNCTION -------------------------------------#


def search_website():
    web_site = str(web_entry.get())

    try:
        with open("saved_data.json", mode="r") as saved_file:
            data = json.load(saved_file)

            mail = data[web_site]["email"]
            passw = data[web_site]["password"]

    except KeyError:
        messagebox.showinfo(title=web_site, message=f"You have not saved any entry for {web_site}")

    except FileNotFoundError:
        messagebox.showinfo(title="No file",
                            message="No data file found in the directory, create your entries now, its simple :)")

    else:
        messagebox.showinfo(title=web_site, message=f"Username : {mail}\nPassword : {passw}")

        saved_file.close()


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_file():
    website = str(web_entry.get())
    username = str(username_entry.get())
    password = str(password_entry.get())

    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="You have left some fields empty")

    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"The details entered :-\neMail : {username}\nPassword : {password}\nProceed to save?")

        # if is_ok:
        try:
            with open("saved_data.json", mode="r") as json_file:
                data = json.load(json_file)
                data.update(new_data)

        except FileNotFoundError:
            with open("saved_data.json", mode="w") as json_file:
                json.dump(new_data, json_file, indent=4)

        else:
            with open("saved_data.json", mode="w") as json_file:
                # Saving updated data
                json.dump(data, json_file, indent=4)

        finally:
            web_entry.delete(0, tkinter.END)
            username_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200)

my_logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_logo_img)
canvas.grid(row=0, column=1)

web_label = tkinter.Label(text="Website : ", font=("Arial", 12, "bold"))
web_label.grid(row=1, column=0)

web_entry = tkinter.Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

search_button = tkinter.Button(text="Search", command=search_website, width=15)
search_button.grid(row=1, column=2)

username_label = tkinter.Label(text="eMail/Username : ", font=("Arial", 12, "bold"))
username_label.grid(row=2, column=0)

username_entry = tkinter.Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)

password_label = tkinter.Label(text="Password : ", font=("Arial", 12, "bold"))
password_label.grid(row=3, column=0)

password_entry = tkinter.Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2)

genPass_button = tkinter.Button(text="Generate Password", command=gen_password, width=15)
genPass_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=34, command=save_file)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
