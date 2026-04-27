class Student:
    def __init__(self):
        self.Name = 'Ahsan Habib Hamim'
        self.Department = 'Computer'
        self.Session = "2024 - 2025"
        self.Semester = '3d Semester'
        self.Age = 17

Student_Details = Student()

print(Student_Details.Name)
print(Student_Details.Department)
print(Student_Details.Session)
print(type(Student_Details.Semester))
print(type(Student_Details.Age))
