from Student import Student
from Course import Course

s1 = Student("tim", 19, 95)
s2 = Student("bill", 19, 75)
s3 = Student("gill", 19, 65)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.students[0].name)

print(course.get_average_grade())
