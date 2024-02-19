import sqlite3

connection = sqlite3.connect("students.db")
query = connection.cursor()

query.execute("create table if not exists students (id integer,name text,age integer, grade text);")


# query.execute("insert into students (id,name,age,grade) values(1,'Bobur',15,'A+');")
# query.execute("insert into students (id,name,age,grade) values(2,'Borya',14,'B');")
# query.execute("insert into students (id,name,age,grade) values(3,'Sasha',11,'D+');")
# query.execute("insert into students (id,name,age,grade) values(4,'Shax',10,'C+');")


def get_student_by_name(name):
    return query.execute("select name,age,grade from students where name =?;", (name,)).fetchone()


def update_student_grade(name, grade):
    query.execute("update students set grade = ? where name = ?;", (grade, name))
    connection.commit()
    return f"Updated successfully \n"


def delete_student(name):
    query.execute("delete from students where name = ?", (name,))
    connection.commit()
    return f"Successfully deleted \n"


def get_all():
    return query.execute("select * from students;").fetchall()


while True:
    print("1.Get student by name ")
    print("2.Update student grade ")
    print("3.Delete student ")
    print("4.Get all students \n ")
    operation = int(input("Enter the operation "))
    if operation == 1:
        name = input("Enter the name of the student ")
        result = get_student_by_name(name)
        print(result)
    elif operation == 2:
        name = input("Enter the name of the student ")
        grade = input("Enter new grade ")
        result = update_student_grade(name, grade)
        print(result)
    elif operation == 3:
        name = input("Enter the name of the student ")
        result = delete_student(name)
        print(result)
    elif operation == 4:
        result = get_all()
        print(result)
    else:
        break

connection.commit()
connection.close()
