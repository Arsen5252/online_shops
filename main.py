import sqlite3

con = sqlite3.connect("shop.db")
cursor = con.cursor()
while True:
    print('1-Вивести всі товари')
    print('2-Сумарний обсяг продажів')
    
    choice = input("Оберіть дію (1-2)")
    
    if choice == "0":
        break
    elif choice == "1":
        cursor.execute('''SELECT * FROM products''')
        data = cursor.fetchall()

        print(data)