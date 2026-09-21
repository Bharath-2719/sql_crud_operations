import sqlite3 as sql
conn=sql.connect("students")
cursor=conn.cursor()
cursor.execute("""
create table if not exists student(id int primary key,name text,age int,course text)""")

def insert():
  id=int(input("Enter the student id:"))
  name=input("Enter the student name:")
  age=int(input("Enter the student age:"))
  course=input("Enter the student course:")

  cursor.execute("insert into student (id,name,age,course)values(?,?,?,?)",(id,name,age,course))
  conn.commit()
def read():
  d=cursor.execute("select * from student")
  for i in d:
    print(i)
def update():
  id = int(input("Enter student id: "))
  name = input("Enter new name: ")
  cursor.execute("update student set name=? where id=?",(name,id))
  conn.commit()
def delete():
  id=int(input("Enter student id:"))
  cursor.execute("delete from student where id=?",(id,))
  conn.commit()

while True:
  print("\n===== STUDENT MANAGEMENT =====")
  print("1. Insert")
  print("2. Read")
  print("3. Update")
  print("4. Delete")
  print("5. Exit")

  choice=int(input("enter the value from 1to 5"))
  if choice==1:
    insert()
  elif choice==2:
    read()
  elif choice==3:
    update()
  elif choice==4:
    delete()
  elif choice==5:
    print("program existed")
    break
  else:
    print("Invalid choice")
conn.close()
