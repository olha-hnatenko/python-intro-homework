students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

leader_score = students[0]["score"]
leader_name = students[0]["name"]
for student in students:
  if student["score"]>leader_score:
    leader_score = student["score"]
    leader_name = student["name"]
print(f"{leader_name} ({leader_score})")


total = 0
for student in students:
  total += student["score"]
average = total / len(students)
print(f"Average score: {average}")


honor_roll = []
for student in students:
    if student["score"] > 75:
        honor_roll.append(student["name"])
print(honor_roll)


uniq_subject=set()
for student in students:
  uniq_subject.add(student["subject"])
print(uniq_subject)