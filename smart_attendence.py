import mysql.connector
from datetime import date
from mysql.connector import cursor

mydb = mysql.connector.connect(host="localhost",user="root",passwd="Srushti@19",database="Attendance")

mycursor = mydb.cursor()
mycursor.execute("SELECT Emp_id,Emp_Full_Name FROM Employees;")
employees= mycursor.fetchall()
print("Employee List")
for employee in employees:
    print(employee[0], "-", employee[1])

try:
    Emp_id = int(input("Enter Employee_id:"))
except ValueError:
    print("Invalid input. Please enter numeric employee id.")
    mycursor.close()
    mydb.close()
    exit()

today = date.today()

mycursor.execute("SELECT * From Employees WHERE Emp_id=%s", (Emp_id,))
emp = mycursor.fetchone()

if emp is None:
    print("This emp id is not valid")
else:
    Status = input("Enter Status(Yes/No): ")
    if Status != "Yes" and Status != "No":
        print("Invalid input. Please enter either Yes or No.")
        mycursor.close()
        mydb.close()
        exit()

    mycursor.execute("SELECT * From Emp_Attendance WHERE Emp_id=%s AND Attendance_date=%s", (Emp_id,today))
    record = mycursor.fetchall()

    if record:
        print("Attendance has already been marked!")
    else:
         mycursor.execute("INSERT INTO Emp_Attendance (Emp_id,Attendance_date, Status) VALUES (%s,%s,%s)",(Emp_id,today,Status))
         mydb.commit()
         print("Attendance marked successfully!")

print("\nAttendance Records:")
mycursor.execute("SELECT Emp_id, Attendance_date, Status From Emp_Attendance")
records = mycursor.fetchall()

for record in records:
    print(record)

mycursor.close()
mydb.close()