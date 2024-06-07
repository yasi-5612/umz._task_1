import sqlite3
from datetime import datetime, date


conn = sqlite3.connect('./financial_records.db')


cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        category TEXT,
        amount REAL,
        description TEXT
    )''')



def convert_to_date(input_string):
    try:
        converted_date = datetime.strptime(input_string, '%Y-%m-%d').date()
        return converted_date
    except ValueError:
        print("Invalid date format. Please enter a date in YYYY-MM-DD format.")
        return None


def add_expense(date, category, amount, description):
    cursor.execute("INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
                   (date, category, amount, description))
    conn.commit()


def remove_expense(expense_id):
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()


def update_expense(expense_id, new_amount):
    cursor.execute("UPDATE expenses SET amount = ? WHERE id = ?", (new_amount, expense_id))
    conn.commit()


def show_expenses():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    
    if rows:
        column_names = [description[0] for description in cursor.description]
        print(column_names)
        
        for row in rows:
            print(row)
    else:
        print("No expenses found.")


status = True


while status == True:

    print("Personal Expense Tracker\n") # ردیاب هزینه های شخصی
    print("1. Add Expense")           # اضافه کردن هزینه
    print("2. Show Expenses")         # مشاهده هزینه ها
    print("3. Update Expense")        # به روز رسانی هزینه
    print("4. Remove Expense")        # حذف هزینه
    print("5. Exit")                  # خارج شوید 
    
    mode = int(input("\nEnter A Number Between 1 to 5: "))
    if mode == 1:
        user_input = input("Enter A Date In YYYY-MM-DD Format: ")
        converted_date = convert_to_date(user_input)
        category = input("Category: ")
        amount = float(input("Amount: "))
        description = input("Description: ")
        add_expense(converted_date, category, amount, description)

    elif mode == 2:
        show_expenses()

    elif mode == 3:
        expense_id = input("ID: ")
        new_amount = float(input("New Amount: "))
        update_expense(expense_id, new_amount)

    elif mode == 4:
        expense_id = int(input("ID: "))
        remove_expense(expense_id)

    elif mode == 5:
        status = False



conn.close()