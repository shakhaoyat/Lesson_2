class Student:

    student_name="hello chad"
    def __init__(self,name,course):
        self.name=name
        self.course=course


    @classmethod

    def get_student_name(cls):
        return cls.student_name

print(Student.get_student_name())



