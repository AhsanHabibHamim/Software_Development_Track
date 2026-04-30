"""
We use constructor __init__ and declare a class name Student and convert it into different object , Now we can use it multiple times with passing diffrent value.
"""
class Student:
    Institute='Dhaka Polytechnic Institute'

    def __init__(self, Name, Roll, Semester, Department):
        self.Name=Name
        self.Roll=Roll
        self.Semester=Semester
        self.Department=Department

# Student Details 01
Student_01 = Student('Ahsan Habib Hamim', 242473, '3rd', 'Computer')
print(Student_01.Name, Student_01.Roll, Student_01.Semester, Student_01.Department, sep='\n')

print() #spacer

# Student Details 02
Student_02 = Student('MD Sahidul islam', 242474, '4th', 'Civil')
print(Student_02.Name, Student_02.Roll, Student_02.Semester, Student_02.Department, sep='\n')

print() #spacer

# Student Details 03
Student_03 = Student('Sabiha Akter', 242475, '5th', 'Mechanical')
print(Student_03.Name, Student_03.Roll, Student_03.Semester, Student_03.Department, sep='\n')

"""
Output:
Ahsan Habib Hamim
242473
3rd
Computer

MD Sahidul islam
242474
4th
Civil

Sabiha Akter
242475
5th
Mechanical
"""
