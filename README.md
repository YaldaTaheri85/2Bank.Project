# 📄 README 
# 🏦 2Bank.Project
> Advanced Programming Final Project - Python

# GitHub link:
https://github.com/YaldaTaheri85/2Bank.Project

---

## 📋 Project Overview

This project is a comprehensive banking management system developed in Python as the final project for the Advanced Programming course. 
The system provides a complete GUI application for managing bank accounts, transactions, and user roles.

**Two user roles are supported:**
- **Customer** - Can manage their own accounts and transactions
- **Banker** - Can manage all accounts and oversee banking operations

---

## 👥 Team Members

| Name | Student Role | Contributions |
|------|--------------|---------------|
| **Maryam Mirzaei** | Backend Developer & Customer Panel | User authentication, account management, data persistence, customer dashboard with all banking operations (deposit, withdraw with savings limits, transfer) |
| **Yalda Taheri** | GUI Developer & Banker Panel | Complete GUI design with Tkinter, login interface, banker dashboard with administrative tools (account opening confirmation, blocking/unblocking, transaction reporting) |

---

## 📂 File Ownership & Git Commits

| # | File | Owner | Commit Message |
|---|------|-------|----------------|
| 1 | `gui.py` | Yalda | `feat: implement main GUI configuration and styling - Yalda` |
| 2 | `user.py` | Maryam | `feat: implement User class with authentication system - Maryam` |
| 3 | `login_window.py` | Yalda | `feat: implement login window interface - Yalda` |
| 4 | `account.py` | Maryam | `feat: implement Account class with banking operations - Maryam` |
| 5 | `main.py` | Yalda | `feat: implement application entry point - Yalda` |
| 6 | `data_manager.py` | Maryam | `feat: implement CSV data persistence layer - Maryam` |
| 7 | `data/transactions.csv` | Yalda | `feat: create transactions data file structure - Yalda` |
| 8 | `data/users.csv` | Maryam | `feat: create users data file with sample users - Maryam` |
| 9 | `banker_window.py` | Yalda | `feat: implement complete banker dashboard with all administrative features - Yalda` |
| 10 | `data/accounts.csv` | Maryam | `feat: create accounts data file with initial data - Maryam` |
| 11 | `customer_window.py` | Maryam | `feat: implement complete customer dashboard with all banking operations - Maryam` |
| 12 | `README.md` | Both | `docs: finalize complete project documentation - Both` |

---

## 📊 Contribution Breakdown

### Maryam Mirzaei (Backend & Customer Panel)
- ✅ User class implementation with authentication system
- ✅ Account class with deposit/withdraw/transfer logic
- ✅ CSV data management (load, save, update operations)
- ✅ Comprehensive error handling and data persistence
- ✅ Savings account withdrawal restrictions (Bonus Feature)
- ✅ Complete customer dashboard with all banking operations
- ✅ Deposit, withdraw and transfer functionality

**Files Owned:** `user.py`, `account.py`, `data_manager.py`, `customer_window.py`, `data/users.csv`, `data/accounts.csv`

### Yalda Taheri (GUI & Banker Panel)
- ✅ Complete GUI design with Tkinter framework
- ✅ Login window with authentication UI
- ✅ Application entry point and window management
- ✅ Banker dashboard with administrative tools
- ✅ Account opening with banker confirmation (Bonus Feature)
- ✅ Account blocking/unblocking functionality
- ✅ Transaction report generation with filters (Bonus Feature)
- ✅ UI/UX improvements and testing

**Files Owned:** `gui.py`, `login_window.py`, `main.py`, `banker_window.py`, `data/transactions.csv`

### Both (Documentation)
- ✅ Project documentation and final review
- ✅ README preparation

**Files Owned:** `README.md`

---

## 🎯 Features

### 👤 Customer Features
| Feature | Description | Status | Developer |
|---------|-------------|--------|-----------|
| Authentication | Login with username and password | ✅ | Maryam |
| View Accounts | See all personal accounts with balances | ✅ | Maryam |
| Deposit Money | Add money to any account | ✅ | Maryam |
| Withdraw Money | Withdraw from accounts (with savings limits) | ✅ | Maryam |
| Transfer Money | Send money to other accounts | ✅ | Maryam |
| Transaction History | View complete transaction log | ✅ | Maryam |

### 👔 Banker Features
| Feature | Description | Status | Developer |
|---------|-------------|--------|-----------|
| View All Accounts | See all customer accounts | ✅ | Yalda |
| Open Account | Create new accounts (requires banker approval) | ✅ | Yalda |
| Block/Unblock | Suspend or restore customer accounts | ✅ | Yalda |
| Transaction Reports | Generate and filter transaction reports | ✅ | Yalda |

### ⭐ Bonus Features Implemented
| Bonus Feature | Description | Implemented By |
|---------------|-------------|----------------|
| Savings Withdrawal Limit | Restrict withdrawals from savings accounts (max 80%) | Maryam |
| Transaction Reporting | Filter transactions by username and date | Yalda |
| Account Blocking | Banker can block/unblock accounts | Yalda |
| Account Opening Confirmation | Manual banker approval for new accounts | Yalda |

---

## 📁 Project Structure
BankManagementSystem/
│
├── 📄 main.py # Application entry point (Yalda)
├── 📄 gui.py # Main GUI setup and configuration (Yalda)
├── 📄 login_window.py # Login user interface (Yalda)
├── 📄 banker_window.py # Banker dashboard UI (Yalda)
├── 📄 customer_window.py # Customer dashboard UI (Maryam)
├── 📄 user.py # User class & authentication logic (Maryam)
├── 📄 account.py # Account class & banking operations (Maryam)
├── 📄 data_manager.py # CSV file read/write operations (Maryam)
│
├── 📁 data/ # Data storage directory
│ ├── 📄 users.csv # User credentials and roles (Maryam)
│ ├── 📄 accounts.csv # Account information and balances (Maryam)
│ └── 📄 transactions.csv # Transaction history log (Yalda)
│
├── 📄 README.md # This documentation file (Both)
└── 📄 .gitignore # Git ignore rules

text

---

## 🗂️ Data Files Format

### users.csv
username,password,role,status
maryam,1381,banker,active
yalda,1385,banker,active
zayn,1371,customer,active
amir,1373,customer,active

text

### accounts.csv
account_id,username,account_type,balance,is_blocked
A1001,zayn,current,500000,no
A1002,zayn,savings,300000,no
A1003,amir,current,1000000,no
A1004,amir,savings,500000,no

text

### transactions.csv
from_account,to_account,amount,type,date
A1001,A1002,100000,transfer,2025-06-27
A1001,,50000,deposit,2025-06-27
A1002,,20000,withdraw,2025-06-27

text

---

## 🚀 How to Run

### Prerequisites
- Python 3.8 or higher installed on your system
- Tkinter (comes pre-installed with Python)

### Installation & Execution

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mrymirzaeii/2bankproject.git
   cd 2bankproject
Verify Python installation:

bash
python --version
Run the application:

bash
python main.py
👥 Sample Users for Testing
Username	Password	Role	Status
maryam	1381	Banker	Active
yalda	1385	Banker	Active
zayn	1371	Customer	Active
amir	1373	Customer	Active
💡 Note: Use these credentials to log in and test the application.

📚 Course Information
Detail	Information
Course	Advanced Programming
Instructor	Zahra Rezvani
Term	Spring 1404
Project Type	Final Project
Programming Language	Python
Team number	2

🏆 Bonus Features Summary
✅ Savings Account Withdrawal Limits - Prevents overspending from savings accounts (max 80% of balance) (Maryam)

✅ Transaction Reporting System - Filter transactions by username and date (Yalda)

✅ Account Blocking/Unblocking - Banker can control account access (Yalda)

✅ Manual Account Opening Confirmation - Banker approval required for new accounts (Yalda)

Thank you for reviewing our project! 🙏
