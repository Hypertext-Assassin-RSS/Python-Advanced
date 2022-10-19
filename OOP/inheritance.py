class Person:
    name = ''
    age = 0

    def __init__(self,personName,personAge):
        self.name = personName
        self.age = personAge
        
    def showName(self):
        print(self.name)
    def showAge(self):
        print(self.age)

class Student(Person):
    StudentId = ''

    def __init__(self,studentName,studentAge,studentId):
        Person.__init__(self,studentName,studentAge)

        self.StudentId = studentId

    def getId(self):
        return self.StudentId
    

person1 = Person('Rajith',22)
person1.showAge()

student1 = Student('sanjaya',22,'S001')
student1.showName()
print(student1.getId())

