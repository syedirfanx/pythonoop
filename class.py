class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 100

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_avg_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


s1 = Student("John", 23, 92)
s2 = Student("Hannah", 22, 94)
s3 = Student("Clay", 22, 90)

course1 = Course("Science", 2)
course1.add_student(s2)
course1.add_student(s3)
print(course1.get_avg_grade())
