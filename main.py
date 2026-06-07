import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@123",
    database="student_db"
)

cursor = conn.cursor()


def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    phone = input("Enter Phone: ")

    sql = "INSERT INTO students (name, age, course, phone) VALUES (%s, %s, %s, %s)"
    values = (name, age, course, phone)

    cursor.execute(sql, values)
    conn.commit()
    print("Student Added Successfully!")


def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    print("\n--- All Students ---")
    for row in records:
        print("ID:", row[0])
        print("Name:", row[1])
        print("Age:", row[2])
        print("Course:", row[3])
        print("Phone:", row[4])
        print("--------------------")


def search_student():
    student_id = int(input("Enter Student ID: "))

    cursor.execute("SELECT * FROM students WHERE id=%s", (student_id,))
    row = cursor.fetchone()

    if row:
        print("\nStudent Found")
        print("ID:", row[0])
        print("Name:", row[1])
        print("Age:", row[2])
        print("Course:", row[3])
        print("Phone:", row[4])
    else:
        print("Student Not Found!")


def update_student():
    student_id = int(input("Enter Student ID to Update: "))

    name = input("Enter New Name: ")
    age = int(input("Enter New Age: "))
    course = input("Enter New Course: ")
    phone = input("Enter New Phone: ")

    sql = """
    UPDATE students
    SET name=%s, age=%s, course=%s, phone=%s
    WHERE id=%s
    """

    values = (name, age, course, phone, student_id)
    cursor.execute(sql, values)
    conn.commit()

    if cursor.rowcount > 0:
        print("Student Updated Successfully!")
    else:
        print("Student Not Found!")


def delete_student():
    student_id = int(input("Enter Student ID to Delete: "))

    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print("Student Deleted Successfully!")
    else:
        print("Student Not Found!")


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Program Closed.")
        break
    else:
        print("Invalid Choice!")

cursor.close()
conn.close()