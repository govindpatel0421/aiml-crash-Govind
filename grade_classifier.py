students = [
    {"name": "Rahul", "score": 92},
    {"name": "Priya", "score": 81},
    {"name": "Aman", "score": 67},
    {"name": "Sneha", "score": 74},
    {"name": "Karan", "score": 45}
]

def classify(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

sorted_students = sorted(
    students,
    key=lambda student: student["score"],
    reverse=True
)

for student in sorted_students:
    grade = classify(student["score"])
    print(f"{student['name']} - Score: {student['score']} - Grade: {grade}")