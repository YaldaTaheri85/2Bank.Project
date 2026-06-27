from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from gui import root
from data_manager import load_accounts, load_transactions, save_accounts, save_transaction

def open_customer(user):
    
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Customer Dashboard")
    root.configure(bg="#EAF4FF")

    Label(
        root,
        text="🏦 Customer Dashboard",
        font=("Tahoma", 20, "bold"),
        bg="#EAF4FF",
        fg="#003366"
    ).pack(pady=15)

    Label(
        root,
        text=f"Welcome {user.username} 👋",
        font=("Tahoma", 13),
        bg="#EAF4FF"
    ).pack(pady=5)

    main_frame = Frame(root, bg="#EAF4FF")
    main_frame.pack(fill=BOTH, expand=True)

    left_frame = Frame(main_frame, bg="#D6EAF8", width=220)
    left_frame.pack(side=LEFT, fill=Y, padx=5, pady=5)

    right_frame = Frame(main_frame, bg="white", relief="ridge", bd=2)
    right_frame.pack(side=RIGHT, fill=BOTH, expand=True, padx=5, pady=5)

    current_account = None

    def show_accounts():
        for widget in right_frame.winfo_children():
            widget.destroy()

        Label(
            right_frame,
            text="📋 My Accounts",
            font=("Tahoma", 14, "bold"),
            bg="white",
            fg="#003366"
        ).pack(pady=10)

        tree = ttk.Treeview(
            right_frame,
            columns=("id", "type", "balance", "blocked"),
            show="headings",
            height=10
        )

        tree.heading("id", text="Account ID")
        tree.heading("type", text="Type")
        tree.heading("balance", text="Balance (Toman)")
        tree.heading("blocked", text="Blocked")

        tree.column("id", width=120)
        tree.column("type", width=120)
        tree.column("balance", width=150)
        tree.column("blocked", width=100)

        tree.pack(fill=BOTH, expand=True, padx=20, pady=10)

        accounts = load_accounts()
        user_accounts = [acc for acc in accounts if acc.username == user.username]

        if not user_accounts:
            Label(
                right_frame,
                text="❌ No accounts found!",
                font=("Tahoma", 12),
                bg="white",
                fg="red"
            ).pack(pady=20)
            return

        for acc in user_accounts:
            tree.insert(
                "",
                END,
                values=(
                    acc.account_id,
                    acc.account_type,
                    f"{acc.balance:,.0f}",
                    "🔒 Yes" if acc.is_blocked == "yes" else "✅ No"
                )
            )

    def deposit_window():
        window = Toplevel(root)
        window.title("💰 Deposit")
        window.geometry("400x300")
        window.configure(bg="#EAF4FF")
        window.resizable(False, False)

        Label(
            window,
            text="💰 Deposit Money",
            font=("Tahoma", 16, "bold"),
            bg="#EAF4FF",
            fg="#003366"
        ).pack(pady=15)

        frame = Frame(window, bg="white", relief="ridge", bd=2)
        frame.pack(pady=10, padx=20, fill=BOTH, expand=True)

        Label(frame, text="Account ID:", bg="white", font=("Tahoma", 11)).grid(row=0, column=0, padx=10, pady=15, sticky="w")
        account_entry = Entry(frame, width=25, font=("Tahoma", 11))
        account_entry.grid(row=0, column=1, padx=10, pady=15)

        Label(frame, text="Amount (Toman):", bg="white", font=("Tahoma", 11)).grid(row=1, column=0, padx=10, pady=15, sticky="w")
        amount_entry = Entry(frame, width=25, font=("Tahoma", 11))
        amount_entry.grid(row=1, column=1, padx=10, pady=15)

        def deposit():
            account_id = account_entry.get().strip()
            try:
                amount = float(amount_entry.get().strip())
                if amount <= 0:
                    messagebox.showerror("Error", "Amount must be positive!")
                    return
            except ValueError:
                messagebox.showerror("Error", "Invalid amount format!")
                return

            accounts = load_accounts()
            for acc in accounts:
                if acc.account_id == account_id and acc.username == user.username:
                    if acc.is_blocked == "yes":
                        messagebox.showerror("Error", "This account is blocked!")
                        return
                    acc.deposit(amount, save_transaction)
                    save_accounts(accounts)
                    messagebox.showinfo("Success", f"💰 {amount:,.0f} Toman deposited successfully!")
                    window.destroy()
                    show_accounts()
                    return
            messagebox.showerror("Error", "Account not found or does not belong to you!")

        Button(
            frame,
            text="Deposit",
            command=deposit,
            bg="#4CAF50",
            fg="white",
            font=("Tahoma", 11, "bold"),
            width=15
        ).grid(row=2, column=0, columnspan=2, pady=20)

    def withdraw_window():
        window = Toplevel(root)
        window.title("🏦 Withdraw")
        window.geometry("400x300")
        window.configure(bg="#EAF4FF")
        window.resizable(False, False)

        Label(
            window,
            text="🏦 Withdraw Money",
            font=("Tahoma", 16, "bold"),
            bg="#EAF4FF",
            fg="#003366"
        ).pack(pady=15)

        frame = Frame(window, bg="white", relief="ridge", bd=2)
        frame.pack(pady=10, padx=20, fill=BOTH, expand=True)

        Label(frame, text="Account ID:", bg="white", font=("Tahoma", 11)).grid(row=0, column=0, padx=10, pady=15, sticky="w")
        account_entry = Entry(frame, width=25, font=("Tahoma", 11))
        account_entry.grid(row=0, column=1, padx=10, pady=15)

        Label(frame, text="Amount (Toman):", bg="white", font=("Tahoma", 11)).grid(row=1, column=0, padx=10, pady=15, sticky="w")
        amount_entry = Entry(frame, width=25, font=("Tahoma", 11))
        amount_entry.grid(row=1, column=1, padx=10, pady=15)

        def withdraw():
            account_id = account_entry.get().strip()
            try:
                amount = float(amount_entry.get().strip())
                if amount <= 0:
                    messagebox.showerror("Error", "Amount must be positive!")
                    return
            except ValueError:
                messagebox.showerror("Error", "Invalid amount format!")
                return

            accounts = load_accounts()
            for acc in accounts:
                if acc.account_id == account_id and acc.username == user.username:
                    if acc.is_blocked == "yes":
                        messagebox.showerror("Error", "This account is blocked!")
                        return
                    if acc.withdraw(amount, save_transaction):
                        save_accounts(accounts)
                        messagebox.showinfo("Success", f"🏦 {amount:,.0f} Toman withdrawn successfully!")
                        window.destroy()
                        show_accounts()
                        return
                    else:
                        return
            messagebox.showerror("Error", "Account not found or does not belong to you!")

        Button(
            frame,
            text="Withdraw",
            command=withdraw,
            bg="#FF5722",
            fg="white",
            font=("Tahoma", 11, "bold"),
            width=15
        ).grid(row=2, column=0, columnspan=2, pady=20)

    def transfer_window():
        window = Toplevel(root)
        window.title("🔄 Transfer")
        window.geometry("450x350")
        window.configure(bg="#EAF4FF")
        window.resizable(False, False)

        Label(
            window,
            text="🔄 Transfer Money",
            font=("Tahoma", 16, "bold"),
            bg="#EAF4FF",
            fg="#003366"
        ).pack(pady=15)

        frame = Frame(window, bg="white", relief="ridge", bd=2)
        frame.pack(pady=10, padx=20, fill=BOTH, expand=True)

        Label(frame, text="From Account:", bg="white", font=("Tahoma", 11)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        from_entry = Entry(frame, width=25, font=("Tahoma", 11))
        from_entry.grid(row=0, column=1, padx=10, pady=10)

        Label(frame, text="To Account:", bg="white", font=("Tahoma", 11)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        to_entry = Entry(frame, width=25, font=("Tahoma", 11))
        to_entry.grid(row=1, column=1, padx=10, pady=10)

        Label(frame, text="Amount (Toman):", bg="white", font=("Tahoma", 11)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        amount_entry = Entry(frame, width=25, font=("Tahoma", 11))
        amount_entry.grid(row=2, column=1, padx=10, pady=10)

        def transfer():
            from_id = from_entry.get().strip()
            to_id = to_entry.get().strip()
            try:
                amount = float(amount_entry.get().strip())
                if amount <= 0:
                    messagebox.showerror("Error", "Amount must be positive!")
                    return
            except ValueError:
                messagebox.showerror("Error", "Invalid amount format!")
                return

            if from_id == to_id:
                messagebox.showerror("Error", "Cannot transfer to same account!")
                return

            accounts = load_accounts()
            from_acc = None
            to_acc = None

            for acc in accounts:
                if acc.account_id == from_id and acc.username == user.username:
                    from_acc = acc
                if acc.account_id == to_id:
                    to_acc = acc

            if not from_acc:
                messagebox.showerror("Error", "Source account not found or does not belong to you!")
                return
            if not to_acc:
                messagebox.showerror("Error", "Destination account not found!")
                return
            if from_acc.is_blocked == "yes":
                messagebox.showerror("Error", "Your account is blocked!")
                return
            if to_acc.is_blocked == "yes":
                messagebox.showerror("Error", "Destination account is blocked!")
                return

            if from_acc.balance < amount:
                messagebox.showerror("Error", "Insufficient balance!")
                return

            from_acc.balance -= amount
            to_acc.balance += amount
            save_accounts(accounts)

            save_transaction(from_id, user.username, "transfer", -amount, from_acc.balance)
            save_transaction(to_id, to_acc.username, "transfer", amount, to_acc.balance)

            messagebox.showinfo("Success", f"🔄 {amount:,.0f} Toman transferred successfully!")
            window.destroy()
            show_accounts()

        Button(
            frame,
            text="Transfer",
            command=transfer,
            bg="#2196F3",
            fg="white",
            font=("Tahoma", 11, "bold"),
            width=15
        ).grid(row=3, column=0, columnspan=2, pady=20)

    def show_transactions():
        
        for widget in right_frame.winfo_children():
            if widget != Label:
                widget.destroy()

        Label(
            right_frame,
            text="📊 Transactions History",
            font=("Tahoma", 14, "bold"),
            bg="white",
            fg="#003366"
        ).pack(pady=(10, 5), anchor="w", padx=20)

        frame_container = Frame(right_frame, bg="white")
        frame_container.pack(fill=BOTH, expand=True, padx=20, pady=10)

        tree = ttk.Treeview(
            frame_container,
            columns=("datetime", "account_id", "type", "amount", "balance"),
            show="headings",
            height=12
        )

        tree.heading("datetime", text="Date & Time")
        tree.heading("account_id", text="Account ID")
        tree.heading("type", text="Type")
        tree.heading("amount", text="Amount")
        tree.heading("balance", text="Balance After")

        tree.column("datetime", width=180)
        tree.column("account_id", width=100)
        tree.column("type", width=100)
        tree.column("amount", width=120)
        tree.column("balance", width=120)

        scrollbar = ttk.Scrollbar(frame_container, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)
        tree.pack(fill=BOTH, expand=True)

        transactions = load_transactions()
        
        user_trans = []
        for t in transactions:
            if len(t) >= 3 and t[2] == user.username:
                user_trans.append(t)

        if not user_trans:
            Label(
                right_frame,
                text="❌ No transactions found!",
                font=("Tahoma", 12),
                bg="white",
                fg="red"
            ).pack(pady=20)
            return

        for trans in user_trans:
            try:
                tree.insert(
                    "",
                    END,
                    values=(
                        trans[0],
                        trans[1],
                        trans[3],
                        f"{int(float(trans[4])):,}",
                        f"{int(float(trans[5])):,}"
                    )
                )
            except:
                tree.insert(
                    "",
                    END,
                    values=(
                        trans[0] if len(trans) > 0 else "",
                        trans[1] if len(trans) > 1 else "",
                        trans[3] if len(trans) > 3 else "",
                        trans[4] if len(trans) > 4 else "",
                        trans[5] if len(trans) > 5 else ""
                    )
                )
                
    Button(
        left_frame,
        text="📋 My Accounts",
        width=20,
        command=show_accounts,
        bg="#1E88E5",
        fg="white",
        font=("Tahoma", 10, "bold")
    ).pack(pady=8)

    Button(
        left_frame,
        text="💰 Deposit",
        width=20,
        command=deposit_window,
        bg="#4CAF50",
        fg="white",
        font=("Tahoma", 10, "bold")
    ).pack(pady=8)

    Button(
        left_frame,
        text="🏦 Withdraw",
        width=20,
        command=withdraw_window,
        bg="#FF5722",
        fg="white",
        font=("Tahoma", 10, "bold")
    ).pack(pady=8)

    Button(
        left_frame,
        text="🔄 Transfer",
        width=20,
        command=transfer_window,
        bg="#2196F3",
        fg="white",
        font=("Tahoma", 10, "bold")
    ).pack(pady=8)

    Button(
        left_frame,
        text="📊 Transactions",
        width=20,
        command=show_transactions,
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

    show_accounts()
