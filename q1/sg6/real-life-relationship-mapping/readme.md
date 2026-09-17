# Activity: Real-Life Relationship Mapping

> **Scenario:** You are mapping out a **School Management System**.

---

## Overview
This activity guides you through modeling relationships between objects visually using UML and implementing those associations in Python code.

---

## Instructions

### Part 1: Visual Diagram (Draw.io)
1. Open [Draw.io](https://app.diagrams.net/).
2. Draw two UML class boxes: `Course` and `Student`.
3. Draw an association line connecting the two classes.
4. Add multiplicity labels to show the relationship (e.g., `1` Course can have `*` Students).
5. Export your completed diagram as an image file (`.png` or `.svg`).

### Part 2: Code Implementation (GitHub)
1. Create a Python script (e.g., `mapping.py`) inside your repository.
2. Implement the `Course` and `Student` classes.
3. Write a method inside `Course` that appends a `Student` object to a list.
4. Commit and push your code to your GitHub repository.

class Student:
    def __init__(self, student_id : str, name : str):
        self.student_id = student_id
        self.name = name
    
    def enrollInCourse(self, course):
        course.add_student(self)

class Course:
    def __init__(self, course_id : str, title : str):
        self.course_id = course_id
        self.title = title
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def get_students(self):
        return self.students
