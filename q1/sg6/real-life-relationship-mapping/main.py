# Write a short Python code snippet showing a Course adding a Student object to a list. 


student1 = Student("S001", "Kyren")
course1 = Course("C001", "Introduction to Nuclear Science")

course1.add_student(student1)

for student in course1.get_students():
    print(f"Student ID: {student.student_id}, Name: {student.name}")
