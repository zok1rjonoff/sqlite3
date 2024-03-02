import sqlite3

# Подключение к БД
connection = sqlite3.connect('shop.db', check_same_thread=False)
# Связь между Python и SQL
sql = connection.cursor()

# Создание таблицы пользователей
sql.execute('CREATE TABLE IF NOT EXISTS users ('
            'id INTEGER, '
            'name TEXT, '
            'number TEXT, '
            'location TEXT'
            ');')
# Создание таблицы продуктов
sql.execute('CREATE TABLE IF NOT EXISTS products ('
            'pr_id INTEGER PRIMARY KEY AUTOINCREMENT, '
            'pr_name TEXT, '
            'pr_count INTEGER, '
            'pr_description TEXT, '
            'pr_price REAL, '
            'pr_photo TEXT'
            ');')
# Создание таблицы корзины
sql.execute('CREATE TABLE IF NOT EXISTS cart ('
            'id INTEGER, '
            'user_pr_name TEXT, '
            'user_pr_count INTEGER, '
            'total REAL'
            ');')


## Методы для пользователя ##
# Проверка на наличие юзера в БД
def check_user(id):
    check = sql.execute('SELECT * FROM users WHERE id=?;', (id,))
    if check.fetchone():
        return True
    else:
        return False


# Регистрация пользователя
def register(id, name, number, location):
    sql.execute('INSERT INTO users VALUES(?, ?, ?, ?);', (id, name, number, location))
    # Фиксируем изменения
    connection.commit()


## Методы для продуктов ##
# Сторона пользователя
# Вывод всех товаров
def get_pr():
    p = sql.execute('SELECT pr_id, pr_name, pr_count FROM products;').fetchall()
    return p


def get_product_count_by_id(product_id):
    product = sql.execute("select pr_count from products where pr_id = ?;", (product_id,)).fetchone()
    return product


# Вывод информации о конкретном продукте
def get_exact_pr(pr_id):
    a = sql.execute('SELECT pr_name, pr_description, pr_count, pr_price, pr_photo '
                    'FROM products WHERE pr_id=?;', (pr_id,)).fetchone()
    return a


# Добавление товара в корзину
def add_pr_to_cart(user_id, user_pr, user_pr_count, total):
    sql.execute('insert into cart (id,user_pr_name,user_pr_count,total) VALUES(?, ?, ?, ?);', (user_id, user_pr, user_pr_count, total))
    connection.commit()


# Сторона админа
# Добавление продукта
def add_pr(pr_name, pr_description, pr_count, pr_price, pr_photo):
    sql.execute('INSERT INTO products(pr_name, pr_description, pr_count, pr_price, pr_photo) '
                'VALUES(?, ?, ?, ?, ?);', (pr_name, pr_description, pr_count, pr_price, pr_photo))
    # Фиксируем изменения
    connection.commit()


# Удаление продукта
def del_pr(pr_id):
    sql.execute('DELETE FROM products WHERE pr_id=?;', (pr_id,))
    # Фиксируем изменения
    connection.commit()


# Изменение количество (можно что-то своё)
def change_pr_count(pr_id, new_count):
    current_count = sql.execute('SELECT pr_count FROM products WHERE pr_id=?;', (pr_id,)).fetchone()
    sql.execute('UPDATE products SET pr_count=? WHERE pr_id=?;',
                (current_count[0] + new_count, pr_id))
    # Фиксируем изменения
    connection.commit()


# Проверка на наличие товаров в БД
def check_pr():
    pr_check = sql.execute('SELECT * FROM products;')
    if pr_check.fetchone():
        return True
    else:
        return False


## Методы для корзины ##
# Отображение корзины
def show_cart(user_id):
    cart_check = sql.execute('SELECT * FROM cart WHERE id=?;', (user_id,)).fetchone()
    return cart_check


# Очистка корзины
def clear_cart(user_id):
    sql.execute('DELETE FROM cart WHERE id=?;', (user_id,))
    # Фиксируем изменения
    connection.commit()


# Оформление заказа
def make_order(user_id):
    print(user_id)
    pr_name = sql.execute('SELECT user_pr_name FROM cart WHERE id=?;', (user_id,)).fetchone()[0]

    user_pr_count = sql.execute('SELECT user_pr_count FROM cart WHERE id=?;',
                                (user_id,)).fetchone()[0]

    current_count = sql.execute('select pr_count from products where pr_id=?;',
                                (pr_name,)).fetchone()[0]
    sql.execute('UPDATE products SET pr_count=? WHERE pr_name=?;',
                (current_count - user_pr_count, pr_name))
    info = sql.execute("select * from cart where id = ?;", (855574466,)).fetchone()
    address = sql.execute('SELECT location FROM users WHERE id=?;', (user_id,)).fetchone()[0]
    # sql.execute('DELETE FROM cart WHERE id=?;', (user_id,))
    connection.commit()
    return info, address


# s = sql.execute("select * from cart where id = ?;",(855574466,)).fetchone()[0]
# print(s)
