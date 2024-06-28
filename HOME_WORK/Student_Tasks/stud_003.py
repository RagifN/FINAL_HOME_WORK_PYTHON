from stud_002 import Students

student = Students("Иван Иванов", "subjects.csv")
student.add_score("Математика", 4)
student.add_test_result("Математика", 86)
print(student.average_test_score("Математика"))
print(student.average_score())