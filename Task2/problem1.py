n = int(input())

students = []

for i in range(n):
    name = str(input())
    grade = float(input())
    students.append([name , grade])

grades = set (grade for i  , grade in students)
sortedGrades = sorted(grades)    

secondLowest = sortedGrades[1]
names = sorted (set (name for name , grade in students if grade == secondLowest) )

for name in names:
    print(name)
