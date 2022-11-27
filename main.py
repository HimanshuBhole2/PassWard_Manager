from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def generate_Pass():
    passward_ent.delete(0,END)
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    passward_ent.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web = website.get()
    user = username.get()
    passw = passward_ent.get()

    new_data = {web:{'email':user,'passward':passw}}
    if len(web) == 0 or len(passw) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")

    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website.delete(0, END)
            passward_ent.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Create passward')
window.config(pady=20,padx=20)


canvas = Canvas(width=200, height= 200)
ima= PhotoImage(file= 'logo.png')
canvas.create_image(100,100,image= ima)
canvas.grid(row=0,column=1)

'''website Interfacer'''
website = Entry(width=34)
website.config(cursor='circle')
website.grid(row=1,column=1)
website.focus()
website_lable = Label(text="Website :",font=('Calibari',16,'bold'))
website_lable.grid(row=1,column=0)
'''Search Button'''
search = Button(text="Search",width=15)
search.grid(row=1,column=2)
search.config(padx=0,pady=0)



'''Username interface'''
username = Entry(width=52)
username.grid(row=2,column=1,columnspan=2)
username_lable = Label(text="Username/E-mail :",font=('Calibari',16,'bold'))
username_lable.grid(row=2,column=0)


'''passward INterface'''
passward_ent = Entry(width= 34)
passward_ent.grid(row=3,column=1)
passward_lable= Label(text="Passward :",font=('Calibari',16,'bold'))
passward_lable.grid(row=3,column=0)


'''add button interfavce'''
add_button = Button(width=45,text="Add",command=save)
add_button.grid(row=4,column=1,columnspan=2)


'''genrate passsward interface'''
gerate_passward = Button(text='Genrate Passward',command=generate_Pass)
gerate_passward.config(padx=0,pady=0)
gerate_passward.grid(row=3,column=2)







mainloop(0)