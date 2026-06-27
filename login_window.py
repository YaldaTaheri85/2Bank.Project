from tkinter import *
from tkinter import messagebox

from gui import root
from data_manager import load_users
from user import User

from customer_window import open_customer
from banker_window import open_banker  

def open_login():

    for widget in root.winfo_children():
        widget.destroy()

    root.title("Bank Management System")

    title = Label(
        root,
        text="🏦 BANK MANAGEMENT SYSTEM",
        font=("Tahoma", 22, "bold"),
        bg="#EAF4FF",
        fg="#003366"
    )

    title.pack(pady=30)

    frame = Frame(
        root,
        bg="white",
        bd=2,
        relief="ridge"
    )

    frame.pack(pady=20)

    Label(
        frame,
        text="Username",
        bg="white",
        font=("Tahoma", 12)
    ).grid(row=0, column=0, padx=20, pady=20)

    username_entry = Entry(
        frame,
        width=30,
        font=("Tahoma", 12)
    )

    username_entry.grid(row=0, column=1, padx=20)

    Label(
        frame,
        text="Password",
        bg="white",
        font=("Tahoma", 12)
    ).grid(row=1, column=0, padx=20, pady=20)

    password_entry = Entry(
        frame,
        show="*",
        width=30,
        font=("Tahoma", 12)
    )

    password_entry.grid(row=1, column=1, padx=20)

    def login():

        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if username == "" or password == "":
            messagebox.showerror(
                "Error",
                "Please enter username and password."
            )
            return

        users = load_users()

        user = User.login(
            users,
            username,
            password
        )

        if user:

            if user.role == "customer":
                open_customer(user)
            elif user.role == "banker":  
                open_banker(user)
            else:
                messagebox.showinfo(
                    "Success",
                    "Welcome " + user.username
                )

        else:

            messagebox.showerror(
                "Error",
                "Username or Password is incorrect."
            )

    Button(
        root,
        text="🔑 Login",
        command=login,
        bg="#1E88E5",
        fg="white",
        width=20,
        height=2,
        font=("Tahoma", 12, "bold")
    ).pack(pady=25)

    Button(
        root,
        text="🚪 Exit",
        command=root.destroy,  
        bg="#F44336",
        fg="white",
        width=20,
        height=1,
        font=("Tahoma", 10, "bold")
    ).pack(pady=5)
