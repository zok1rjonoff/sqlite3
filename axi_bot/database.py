import sqlite3

connection = sqlite3.connect("axi_market.db", check_same_thread=False)
query = connection.cursor()

query.execute("create table if not exists users (id integer,name text,number text,location text);")

query.execute("create table if not exists products "
              "(id integer primary key autoincrement,"
              "product_name text,"
              "product_count integer,"
              "product_description text,"
              "product_price real,"
              "product_photo text);")

query.execute("create table if not exists basket ("
              "id integer,"
              "user_product_name text,"
              "user_product_count integer);")


def check_user(user_id):
    exist = query.execute("select * from users where id = ?;", (user_id,))
    if exist.fetchone():
        return True
    else:
        return False


def get_user(user_id):
    return query.execute("select name from users where id = ?;",(user_id,)).fetchone()[0]


def registration(user_id, name, phone_number, location):
    query.execute("insert into users values(?,?,?,?);", (user_id, name, phone_number, location))
    connection.commit()


def get_product():
    return query.execute("select id, product_name,product_count from products;").fetchall()


def get_exact_product(pr_id):
    return query.execute("select product_name,product_price,product_count,product_description,product_photo from "
                         "products where id = ?;", (pr_id,)).fetchone()


def add_pr_to_basket(user_id, user_pr, user_pr_count):
    query.execute("insert into basket values(?,?,?);", (user_id, user_pr, user_pr_count))
    connection.commit()


def show_basket(user_id):
    basket = query.execute("select * from basket where is = ?;",(user_id,)).fetchone()
    if basket:
        return basket
    else:
        return False


def delete_from_basket(user_id):
    query.execute("delete from basket where id = ?;",(user_id,))
    connection.commit()


def make_order(user_id):
    name = query.execute("select user_product_name from products where id = ?;",(user_id,)).fetchone()[0]
    count = query.execute("select user_product_count from basket where id = ?;",(user_id,)).fetchone()[0]
    current_count = query.execute("select product_count from products where product_name = ?;",(name,)).fetchone()[0]
    query.execute("update products set product_count = ? where product_name = ?;",(current_count-count,name))
    info = query.execute("select * from basket where id =?;",(user_id,)).fetchone()
    address = query.execute("select location from users where id = ?;",(user_id,)).fetchone()
    query.execute("delete from basket where id = ?",(user_id,))
    connection.commit()
    return info,address


def add_product(pr_name, pr_des, pr_count, pr_price, pr_photo):
    query.execute("insert into products (product_name,product_description,product_count,product_price,"
                  "product_photo) values(?,?,?,?,?);", (pr_name, pr_des, pr_count, pr_price, pr_photo))
    connection.commit()


def delete_product(pr_id):
    query.execute("delete from products where id = ?;", (pr_id,))
    connection.commit()


def change_pr_count(pr_id, pr_count):
    current_count = query.execute("select product_count from products where id = ?;", (pr_id,)).fetchone()
    updated_count = current_count[0]
    query.execute("update products set product_count = ? where id = ?;", (updated_count + pr_count, pr_id))
    connection.commit()



def check_pr():
    check = query.execute("select * from products;").fetchone()
    if check:
        return True
    else:
        return False


connection.commit()
