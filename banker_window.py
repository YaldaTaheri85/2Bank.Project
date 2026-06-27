from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from gui import root
from data_manager import load_users, load_accounts, load_transactions, save_users, save_accounts
from account import Account
import random

def generate_account_id():
    return "A" + str(random.randint(1000, 9999))

def open_banker(user):
    
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Banker Dashboard")
    root.configure(bg="#EAF4FF")

    Label(
        root,
        text="🏦 Banker Dashboard",
        font=("Tahoma", 20, "bold"),
        bg="#EAF4FF",
        fg="#003366"
    ).pack(pady=15)

    Label(
        root,
        text=f"Welcome Banker {user.username} 👋",
        font=("Tahoma", 13),
        bg="#EAF4FF"
    ).pack(pady=5)

    main_frame = Frame(root, bg="#EAF4FF")
    main_frame.pack(fill=BOTH, expand=True)

    left_frame = Frame(main_frame, bg="#D6EAF8", width=220)
    left_frame.pack(side=LEFT, fill=Y, padx=5, pady=5)

    right_frame = Frame(main_frame, bg="white", relief="ridge", bd=2)
    right_frame.pack(side=RIGHT, fill=BOTH, expand=True, padx=5, pady=5)

    def show_all_accounts():
        for widget in right_frame.winfo_children():
            widget.destroy()

        Label(
            right_frame,
            text="📋 All Accounts",
            font=("Tahoma", 14, "bold"),
            bg="white",
            fg="#003366"
        ).pack(pady=10)

        tree = ttk.Treeview(
            right_frame,
            columns=("id", "username", "type", "balance", "blocked"),
            show="headings",
            height=12
        )

        tree.heading("id", text="Account ID")
        tree.heading("username", text="Username")
        tree.heading("type", text="Type")
        tree.heading("balance", text="Balance")
        tree.heading("blocked", text="Blocked")

        tree.column("id", width=100)
        tree.column("username", width=100)
        tree.column("type", width=100)
        tree.column("balance", width=120)
        tree.column("blocked", width=100)

        tree.pack(fill=BOTH, expand=True, padx=20, pady=10)

        accounts = load_accounts()
        if not accounts:
            Label(
                right_frame,
                text="❌ No accounts found!",
                font=("Tahoma", 12),
                bg="white",
                fg="red"
            ).pack(pady=20)
            return

        for acc in accounts:
            tree.insert(
                "",
                END,
                values=(
                    acc.account_id,
                    acc.username,
                    acc.account_type,
                    f"{acc.balance:,.0f}",
                    "🔒 Yes" if acc.is_blocked == "yes" else "✅ No"
                )
            )

    def open_account_window():
        window = Toplevel(root)
        window.title("➕ Open New Account")
        window.geometry("450x400")
        window.configure(bg="#EAF4FF")
        window.resizable(False, False)

        Label(
            window,
            text="➕ Open New Account",
            font=("Tahoma", 16, "bold"),
            bg="#EAF4FF",
            fg="#003366"
        ).pack(pady=15)

        frame = Frame(window, bg="white", relief="ridge", bd=2)
        frame.pack(pady=10, padx=20, fill=BOTH, expand=True)

        Label(frame, text="Username:", bg="white", font=("Tahoma", 11)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        username_entry = Entry(frame, width=25, font=("Tahoma", 11))
        username_entry.grid(row=0, column=1, padx=10, pady=10)

        Label(frame, text="Account Type:", bg="white", font=("Tahoma", 11)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        type_var = StringVar(value="current")
        Radiobutton(frame, text="Current", variable=type_var, value="current", bg="white").grid(row=1, column=1, sticky="w")
        Radiobutton(frame, text="Savings", variable=type_var, value="savings", bg="white").grid(row=2, column=1, sticky="w")

        Label(frame, text="Initial Deposit:", bg="white", font=("Tahoma", 11)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
        balance_entry = Entry(frame, width=25, font=("Tahoma", 11))
        balance_entry.grid(row=3, column=1, padx=10, pady=10)
        Label(frame, text="(Minimum: 100,000 Toman)", bg="white", font=("Tahoma", 9), fg="gray").grid(row=4, column=1, sticky="w")

        confirm_var = IntVar()
        Checkbutton(
            frame,
            text="✅ I confirm this account opening",
            variable=confirm_var,
            bg="white",
            font=("Tahoma", 10)
        ).grid(row=5, column=0, columnspan=2, pady=10)

        def create_account():
            username = username_entry.get().strip()
            account_type = type_var.get()
            try:
                balance = float(balance_entry.get().strip())
                if balance < 100000:
                    messagebox.showerror("Error", "Minimum initial deposit is 100,000 Toman!")
                    return
            except ValueError:
                messagebox.showerror("Error", "Invalid amount format!")
                return

            if not username:
                messagebox.showerror("Error", "Please enter username!")
                return

            if confirm_var.get() != 1:
                messagebox.showerror("Error", "Please confirm the account opening!")
                return

            users = load_users()
            user_exists = False
            for u in users:
                if u.username == username:
                    user_exists = True
                    break

            if not user_exists:
                messagebox.showerror("Error", f"User '{username}' does not exist!")
                return

            accounts = load_accounts()
            new_id = generate_account_id()

            existing_ids = [acc.account_id for acc in accounts]
            while new_id in existing_ids:
                new_id = generate_account_id()

            new_account = Account(new_id, username, account_type, balance, "no")
            accounts.append(new_account)
            save_accounts(accounts)

            messagebox.showinfo("Success", f"✅ Account {new_id} created successfully for {username}!")
            window.destroy()
            show_all_accounts()

        Button(
            frame,
            text="Create Account",
            command=create_account,
            bg="#4CAF50",
            fg="white",
            font=("Tahoma", 11, "bold"),
            width=15
        ).grid(row=6, column=0, columnspan=2, pady=15)

    def block_account_window():
        window = Toplevel(root)
        window.title("🔒 Block/Unblock Account")
        window.geometry("400x250")
        window.configure(bg="#EAF4FF")
        window.resizable(False, False)

        Label(
            window,
            text="🔒 Block/Unblock Account",
            font=("Tahoma", 16, "bold"),
            bg="#EAF4FF",
            fg="#003366"
        ).pack(pady=15)

        frame = Frame(window, bg="white", relief="ridge", bd=2)
        frame.pack(pady=10, padx=20, fill=BOTH, expand=True)

        Label(frame, text="Account ID:", bg="white", font=("Tahoma", 11)).grid(row=0, column=0, padx=10, pady=15, sticky="w")
        account_entry = Entry(frame, width=25, font=("Tahoma", 11))
        account_entry.grid(row=0, column=1, padx=10, pady=15)

        def toggle_block():
            account_id = account_entry.get().strip()
            if not account_id:
                messagebox.showerror("Error", "Please enter account ID!")
                return

            accounts = load_accounts()
            for acc in accounts:
                if acc.account_id == account_id:
                    if acc.is_blocked == "no":
                        acc.is_blocked = "yes"
                        save_accounts(accounts)
                        messagebox.showinfo("Success", f"🔒 Account {account_id} has been BLOCKED!")
                    else:
                        acc.is_blocked = "no"
                        save_accounts(accounts)
                        messagebox.showinfo("Success", f"✅ Account {account_id} has been UNBLOCKED!")
                    window.destroy()
                    show_all_accounts()
                    return
            messagebox.showerror("Error", "Account not found!")

        Button(
            frame,
            text="Toggle Block Status",
            command=toggle_block,
            bg="#FF9800",
            fg="white",
            font=("Tahoma", 11, "bold"),
            width=18
        ).grid(row=1, column=0, columnspan=2, pady=20)

    def transaction_report_window():
        for widget in right_frame.winfo_children():
            widget.destroy()

        Label(
            right_frame,
            text="📊 Transaction Report (All Users)",
            font=("Tahoma", 14, "bold"),
            bg="white",
            fg="#003366"
        ).pack(pady=10)

        filter_frame = Frame(right_frame, bg="white")
        filter_frame.pack(fill=X, padx=20, pady=5)

        Label(filter_frame, text="Filter by Username:", bg="white", font=("Tahoma", 10)).pack(side=LEFT, padx=5)
        username_filter = Entry(filter_frame, width=20, font=("Tahoma", 10))
        username_filter.pack(side=LEFT, padx=5)

        tree_frame = Frame(right_frame, bg="white")
        tree_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

        tree = ttk.Treeview(
            tree_frame,
            columns=("datetime", "account_id", "username", "type", "amount", "balance"),
            show="headings",
            height=15
        )

        tree.heading("datetime", text="Date & Time")
        tree.heading("account_id", text="Account ID")
        tree.heading("username", text="Username")
        tree.heading("type", text="Type")
        tree.heading("amount", text="Amount")
        tree.heading("balance", text="Balance After")

        tree.column("datetime", width=170)
        tree.column("account_id", width=90)
        tree.column("username", width=90)
        tree.column("type", width=90)
        tree.column("amount", width=110)
        tree.column("balance", width=110)

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)
        tree.pack(fill=BOTH, expand=True)

        def load_transactions_filter():
            
            for item in tree.get_children():
                tree.delete(item)

            filter_user = username_filter.get().strip()
            transactions = load_transactions()

            if not transactions:
                Label(right_frame, text="❌ No transactions found!", bg="white", fg="red", font=("Tahoma", 11)).pack(pady=10)
                return

            for trans in transactions:
                if filter_user == "" or trans[2] == filter_user:
                    try:
                        tree.insert(
                            "",
                            END,
                            values=(
                                trans[0],
                                trans[1],
                                trans[2],
                                trans[3],
                                f"{int(trans[4]):,}",
                                f"{int(trans[5]):,}"
                            )
                        )
                    except:
                        tree.insert(
                            "",
                            END,
                            values=(trans[0], trans[1], trans[2], trans[3], trans[4], trans[5])
                        )

            count = len(tree.get_children())
            Label(
                right_frame,
                text=f"📊 Total Transactions: {count}",
                bg="white",
                font=("Tahoma", 10, "bold"),
                fg="#003366"
            ).pack(pady=5)

        Button(
            filter_frame,
            text="🔍 Apply Filter",
            command=load_transactions_filter,
            bg="#2196F3",
            fg="white",
            font=("Tahoma", 9, "bold")
        ).pack(side=LEFT, padx=10)

        Button(
            filter_frame,
            text="🔄 Show All",
            command=lambda: [username_filter.delete(0, END), load_transactions_filter()],
            bg="#9E9E9E",
            fg="white",
            font=("Tahoma", 9, "bold")
        ).pack(side=LEFT, padx=5)

        load_transactions_filter()

    Button(
        left_frame,
        text="📋 All Accounts",
        width=20,
        command=show_all_accounts,
        bg="#1E88E5",
        fg="white",
        font=("Tahoma", 10, "bold")
    ).pack(pady=8)

    Button(
        left_frame,
        text="➕ Open Account",
        width=20,
        command=open_account_window,
        bg="#4CAF50",
        fg="white",
        font=("Tahoma", 10, "bold")
    ).pack(pady=8)

    Button(
        left_frame,
        text="🔒 Block/Unblock",
        width=20,
        command=block_account_window,
        bg="#FF9800",
        fg="white",
        font=("Tahoma", 10, "bold")
    ).pack(pady=8)

    Button(
        left_frame,
        text="📊 Transaction Report",
        width=20,
        command=transaction_report_window,
        bg="#9C27B0",
        fg="white",
        font=("Tahoma", 10, "bold")
    ).pack(pady=8)

    Button(
        left_frame,
        text="🚪 Logout",
        width=20,
        command=root.destroy,
        bg="#F44336",
        fg="white",
        font=("Tahoma", 10, "bold")
    ).pack(side=BOTTOM, pady=20)

    show_all_accounts()
