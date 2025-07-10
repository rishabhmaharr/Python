# Day9 HomeWork

# Q1: Ask the user to enter a key (like id, name, or salary), print "Key exists" if it is in the dictionary, otherwise print "Key not found"
dict_01 = {
    id: 192,
    "name" : "Rishabh Mahar",
    "salary" : 50000
}
key = input("Enter the key you want to search: (id, name, salary)").strip() 
if key in dict_01:
    print("Key exists")
else:
    print("Key not found")
    
# Q2: Add a new key 'Course' with value 'Python' to a dictionary having 3 prior entries, then print the updated dictionary.
dict_02 = {
    "id": 192,
    "name": "Rishabh Mahar",
    "salary": 50000
}
dict_02["Course"] = "Python"
print("Updated Dictionary:", dict_02)

# Q3: Write a Python program that does the following:
# """Creates an empty dictionary named student_marks.
# Adds the following key-value pairs to it:
# 'Alice': 85
# 'Bob': 92
# 'Charlie': 78
# Ask the user to input a student’s name.
# Print the marks of that student using the dictionary.
# If the name doesn’t exist in the dictionary, print "Student not found."""
 
student_marks = {}
student_marks['Alice'] = 85
student_marks['Bob'] = 92
student_marks['Charlie'] = 78

student_name = input("Enter the student's name:").strip()

if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found")
    