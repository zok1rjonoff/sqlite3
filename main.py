import sqlite3

connection = sqlite3.connect("bank.db")
query = connection.cursor()
# query.execute("drop table clients")
query.execute("create table if not exists clients (fullname text, phone_number text,balance real); ")


# query.execute("delete from clients;")

def registration(fullname, phonenumber):
    query.execute("insert into clients (fullname, phone_number,balance) values(?,?,0);", (fullname, phonenumber))
    connection.commit()
    return f"Successfully registered \n"


def search_by_name(name):
    return query.execute("select * from clients where fullname = ?;", (name,)).fetchone()


def search_by_phone_number(phone_number):
    return query.execute("select * from clients where phone_number = ?;", (phone_number,)).fetchone()


def search_by_fullname_and_phonenumber(fullname, phonenumber):
    return query.execute("select fullname, phone_number from clients where fullname = ? , phone_number = ?;",
                         (fullname, phonenumber))


def balance_replenishment(fullanmae, balamce):
    query.execute("update clients set balance = ? where fullname = ?;", (balamce, fullanmae))
    connection.commit()
    return f"Your balance replenished \n "


def withdraw_money_from_balance(fullname, withdraw):
    real_balance = query.execute("select balance from clients where fullname = ?;", (fullname,)).fetchone()[0]
    remainder = real_balance - withdraw
    query.execute("update clients set balance = ? where fullname = ?;", (remainder, fullname))
    connection.commit()
    return f"You withdraw money \n "


def check_my_balance(fullname):
    res = query.execute("select balance from clients where fullname = ?;", (fullname,)).fetchone()[0]
    return f"You have {res} $ in your balance \n"


def calculate_deposit(fullname, month):
    deposit = query.execute("select balance from clients where fullname = ?;", (fullname,)).fetchone()[0]
    return f"Your {month} month deposit is calculated as {deposit + (deposit * 0.01 * month)} \n"


while True:
    print("1.Registration ")
    print("2.Search by fullname ")
    print("3.Search by phone number ")
    print("4.Search by fullname and phone number")
    print("5.Balance replenishment")
    print("6.Withdrawal of funds from balance ")
    print("7.Checking balance")
    print("8.Calculation deposit")
    print("9.Personal account")
    print("0.Exit")
    operation = int(input("Enter the operation "))
    if operation == 1:
        fullname = input("Enter your fullname ")
        phone_number = input("Enter your phone number ")
        res = registration(fullname, phone_number)
        print(res)
    elif operation == 2:
        fullname = input("Enter your full name ")
        res = search_by_name(fullname)
        print(f"{res}  \n")
    elif operation == 3:
        phone_number = input("Enter your phone number ")
        res = search_by_phone_number(phone_number)
        print(f"{res}  \n")
    elif operation == 4:
        fullname = input("Enter your full name: ")
        phone_number = input("Enter your phone number: ")
        res = search_by_fullname_and_phonenumber(fullname, phone_number)
        print(res)
    elif operation == 5:
        fullname = input("Who are u ? ")
        balance = input("How much money do u want to replenish ? ")
        res = balance_replenishment(fullname, balance)
        print(res)
    elif operation == 6:
        fullname = input("Who are u ? ")
        withdraw = float(input("How much money do u want to withdraw ? "))
        res = withdraw_money_from_balance(fullname, withdraw)
        print(res)
    elif operation == 7:
        fullname = input("Who are u ? ")
        res = check_my_balance(fullname)
        print(res)
    elif operation == 8:
        fullname = input("Enter your fullname ")
        month = int(input("How much monthly deposit do you want to withdraw ? "))
        res = calculate_deposit(fullname, month)
        print(res)
    elif operation == 9:
        fullname = input("Enter your fullname: ")
        res = search_by_name(fullname)
        print(f"You are {res[0]}")
        print(f"your phone number is {res[1]} ")
        print(f"Your balance is {res[2]} $ \n")
    else:
        break

connection.commit()
connection.close()

