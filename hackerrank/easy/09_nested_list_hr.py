"""
Given the names and grades for each student in a class of N students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note:
If there are multiple students with the second lowest grade,
order their names alphabetically and print each name on a new line.
"""

# Collect student names and scores
students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

# Find the second lowest score (remove duplicates, then sort)
second_lowest = sorted({s[1] for s in students})[1]

# Get names of students who have the second lowest score, sorted alphabetically
names = sorted([s[0] for s in students if s[1] == second_lowest])

for name in names:
    print(name)
