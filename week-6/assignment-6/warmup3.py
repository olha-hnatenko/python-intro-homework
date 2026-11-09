def set_name():
    name = "Priya"
set_name()
# print(name)
# NameError: name 'name' is not defined

def get_name():
    name = "Priya"
    return name

student_name = get_name()
print(student_name)