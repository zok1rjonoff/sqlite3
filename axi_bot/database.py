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


def registration(user_id, name, phone_number, location):
    query.execute("insert into users values(?,?,?,?);", (user_id, name, phone_number, location))
    connection.commit()


connection.commit()
connection.close()
