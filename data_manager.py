import csv
import datetime

from user import User
from account import Account

def load_users():
    users = []
    try:
        with open("data/users.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                users.append(User(row["username"], row["password"], row["role"], row["status"]))
    except FileNotFoundError:
        print("users.csv not found!")
    return users

def save_users(users):
    with open("data/users.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["username", "password", "role", "status"])
        for u in users:
            writer.writerow([u.username, u.password, u.role, u.status])

def load_accounts():
    accounts = []
    try:
        with open("data/accounts.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                accounts.append(Account(row["account_id"], row["username"], row["account_type"], float(row["balance"]), row["is_blocked"]))
    except FileNotFoundError:
        print("accounts.csv not found!")
    return accounts

def save_accounts(accounts):
    with open("data/accounts.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["account_id", "username", "account_type", "balance", "is_blocked"])
        for acc in accounts:
            writer.writerow([acc.account_id, acc.username, acc.account_type, acc.balance, acc.is_blocked])

def load_transactions():
    transactions = []
    try:
        with open("data/transactions.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  
                    transactions.append(row)
    except FileNotFoundError:
        pass  
    return transactions

def save_transaction(account_id, username, trans_type, amount, balance_after):
    with open("data/transactions.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([now, account_id, username, trans_type, amount, balance_after])

def show_transaction_report(username_filter=None):
    try:
        with open("data/transactions.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            rows = list(reader)
            if not rows:
                print("\nهیچ تراکنشی یافت نشد.")
                return
            print("\n" + "="*95)
            print(f"{'تاریخ و ساعت':<20} {'شماره حساب':<12} {'کاربر':<12} {'نوع':<10} {'مبلغ':<15} {'موجودی بعد':<15}")
            print("="*95)
            for row in rows:
                if username_filter is None or row[2] == username_filter:
                    try:
                        amount = int(float(row[4]))
                        balance = int(float(row[5]))
                        print(f"{row[0]:<20} {row[1]:<12} {row[2]:<12} {row[3]:<10} {amount:>12,} تومان  {balance:>12,} تومان")
                    except:
                        print(f"{row[0]:<20} {row[1]:<12} {row[2]:<12} {row[3]:<10} {row[4]:>12} {row[5]:>12}")
            print("="*95 + "\n")
    except FileNotFoundError:
        print("\nفایل تراکنش‌ها یافت نشد. هنوز تراکنشی ثبت نشده است.")
