'''
name : M Drishya
date : November 5 , 2025
project title : Gradebook Analyser
'''

print("Welcome to Gradebook Analyser")
print("Enter your choice: \n1. Manual input\n2. Import CSV file")
choice = int(input())
marks = {}

if choice == 1:
    print("You chose manual input.")
    num = int(input("Enter number of students: "))
    for i in range(num):
        name = input("Enter student name: ")
        marks[name] = float(input("Enter student marks: "))

elif choice == 2:
    print("You chose to import a CSV file.")
    file_name = input("Enter CSV file name (with .csv): ")
    with open(file_name) as file:
        next(file)
        for line in file:
            name, score = line.strip().split(",")
            marks[name] = float(score)
    print("Data loaded successfully:", marks)

else:
    print("Invalid choice.")


def calculate_average(marks_dict):
    total = 0
    for value in marks_dict.values():
        total += value
    return total / len(marks_dict)


def calculate_median(marks_dict):
    values = list(marks_dict.values())
    n = len(values)
    # bubble sort
    for i in range(n):
        for j in range(0, n - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
    # find median
    if n % 2 == 0:
        median = (values[n//2 - 1] + values[n//2]) / 2
    else:
        median = values[n//2]
    return median


def find_max_score(marks_dict):
    max_value = 0
    for i in marks_dict.values():
        if i > max_value:
            max_value = i
    return max_value


def find_min_score(marks_dict):
    min_value = 100
    for i in marks_dict.values():
        if i < min_value:
            min_value = i
    return min_value
print()
print("Average marks:", calculate_average(marks))
print("Median marks:", calculate_median(marks))
print("Maximum marks:", find_max_score(marks))
print("Minimum marks:", find_min_score(marks))


grade = {}
countA = 0
countB = 0
countC = 0
countD = 0
countF = 0

for name, score in marks.items():
    if score >= 90:
        grade[name] = "A"
        countA += 1
    elif score >= 80:
        grade[name] = "B"
        countB += 1
    elif score >= 70:
        grade[name] = "C"
        countC += 1
    elif score >= 60:
        grade[name] = "D"
        countD += 1
    else:
        grade[name] = "F"
        countF += 1

print("\nGrade Distribution:")
print("A:", countA)
print("B:", countB)
print("C:", countC)
print("D:", countD)
print("F:", countF)

passed_students = []
failed_students = []

for name, score in marks.items():
    if score >= 40:
        passed_students.append(name)
    else:
        failed_students.append(name)


print()
print("Number of students passed:", len(passed_students))
print("Students who passed:", passed_students)
print("Number of students failed:", len(failed_students))
print("Students who failed:", failed_students)

print("~GRADE SUMMARY~")
print("Name\t\tMarks\tGrade")
print("-----------------------------------------------------------------------------")
for name in marks:
    print(f"{name}\t\t{marks[name]}\t{grade[name]}")
print("-----------------------------------------------------------------------------")