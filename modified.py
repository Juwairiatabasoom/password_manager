from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = [choice(letters) for char in range(randint(8, 10))]

    password_list +=[choice(symbols) for char in range(randint(2, 4))]

    password_list +=[choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)

    my_password="".join(password_list)
    password_input.insert(0,my_password)
    pyperclip.copy(my_password)  #this package automatically copies the password to clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_input.get()
    email=email_input.get()
    password=password_input.get()
    new_data={website:{
                      "email":email,
                      "password":password
                        }
                        }

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="Some fields are empty")

    else:
        try:
            with open("json_file.json","r") as data_file:
                #reading old data
                data=json.load(data_file)

        except FileNotFoundError:
            with open ("json_file.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)


        else:


            # updating new data
            data.update(new_data)

            with open ("json_file.json","w") as data_file:
                #saving updated data
                json.dump(data,data_file,indent=4)
        finally:
            website_input.delete(0,END)
            password_input.delete(0,END) #delete funtion deletes the previous entry in order to enter the new entry


# ---------------------------- FIND PASSWORD ------------------------------- #


def search_the_password():
    website = website_input.get()
    try:
        with open ("json_file.json") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="Data Not Found")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}",message=f"Email: {email}\nPassword: {password}")

        else:
            if len(website)==0:
                messagebox.showinfo(title="Oops",message="Enter a valid website's name")
            else:
                messagebox.showinfo(title="Error",message=f"No details of {website} exists")



# ---------------------------- UI SETUP ------------------------------- #


window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)


canvas=Canvas(width=200,height=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

#labels

website_label=Label(text="Website:")
website_label.grid(column=0,row=1)

username_label=Label(text="Email/Username:")
username_label.grid(column=0,row=2)

password_label=Label(text="Password:")
password_label.grid(column=0,row=3)


#entry

website_input=Entry(width=35)
website_input.grid(row=1,column=1)
website_input.focus()  ##it directly focuses the cursor at the website entry

email_input=Entry(width=35)
email_input.grid(row=2,column=1)
email_input.insert(0,"juwairia@gmail.com")  # here '0' is at which char of the entry the str must be inserted

password_input=Entry(width=35)
password_input.grid(row=3,column=1)


#buttons
generate_button=Button(text="Generate Password",command=generate_password)
generate_button.grid(row=3,column=2)

search_button=Button(text="Search",width=14,command=search_the_password)
search_button.grid(row=1,column=2)

add_button=Button(text="Add",width=45,command=save)
add_button.grid(column=1,row=4,columnspan=2)


window.mainloop()



