# This program prints a student introduction using variables and dictionaries.

name = "Govind Patel"
age = 20
city = "Jodhpur"
favorite_subject = "Python"
target_role = "AI Developer"

student = {
    "name": name,
    "age": age,
    "city": city,
    "favorite_subject": favorite_subject,
    "target_role": target_role
}

print(f"My name is {student['name'].title()}.")
print(f"I am {student['age']} years old.")
print(f"I live in {student['city'].upper()}.")
print(f"My favorite subject is {student['favorite_subject']} and I want to become an {student['target_role']}.")