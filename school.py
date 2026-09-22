class Person :
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def introduce(self):
        print(f"Hi, I am {self.name}")

class Student(Person):
    total_students = 0
    def __init__(self, name, email, grade):
        super().__init__(name, email)
        self.__grade = grade
        self.courses = []

        Student.total_students += 1

    #داله ال getter 
    @property
    def grade(self):
        return self.__grade

    #داله ال setter 
    @grade.setter
    def grade(self, value):
        if 0 <= value <= 100:
            self.__grade = value
        else:
            print("grade must be between 0 and 100")

    def add_course(self,course):
        self.courses.append(course)

    def introduce(self):
        print(
            f"Hi, I am {self.name} "
            f"I am a student and my grade is {self.grade}"
            )

class teacher(Person):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject
        self.courses = []

    def add_course(self,course):
        self.courses.append(course)

    def introduce(self):
        super().introduce()
        print(f"I am teaching {self.subject}")

class Course:
    total_courses = 0 
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []
        Course.total_courses += 1

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            print(f"{student.name} enrolled in {self.name}")
        else:
            print(f"{student.name} is already enrolles in {self.name}")

    def show_student(self):
        print(f"\n student in {self.name}: ")

        if len(self.students) == 0:
            print(f"No student enrolled")
            return
        for student in self.students:
            print(f"- {student.name}"
                  f"(Grade : {student.grade})")

Student.total_students = 0
Course.total_courses = 0

print("============== School System ==============")
t1 = teacher("DR Ahmed", "ahmed@gmail.com", "CS")
c1 = Course("Python", t1)
# t1.add_course(c1)
# t1.introduce()
# print(f"Total Courses Created {Course.total_courses}")

s1 = Student("Mona", "mona@gmail.com", 90)
s2 = Student("Ali", "ali@gmail.com", 80)
s1.introduce()

s1.grade = 105
s2.grade = 90
# print(f"Total students created: {Student.total_students}")
# print(s1.grade)
# print(s2.grade)

c1.add_student(s1)
c1.add_student(s2)
c1.show_student()