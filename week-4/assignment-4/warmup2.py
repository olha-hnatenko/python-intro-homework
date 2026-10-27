student={"name": "Karen", "grade":"A", "subjects":["Mathematics", "Psychology", "English Composition"]}
for key, value in student.items():
    print(f"{key}: {value}")
student["graduated"]=False
print(student)