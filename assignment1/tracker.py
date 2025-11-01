'''
name : M Drishya 
date : November 1 , 2025 
project title : Daily Calorie Tracker
'''

print("Welcome to Daily Calorie Tracker")
print("Enter the number of items you have eaten today:")
num_items = int(input())

total = 0
avg = 0
meal_names = []
calories_list = []   # <--- Added this line

for i in range(num_items):
    print("Enter the meal name for item no.", i + 1, ":")
    meal_name = input()
    meal_names.append(meal_name)
    
    print("Enter the calories for item no.", i + 1, ":")
    calories = int(input())
    calories_list.append(calories)  # <--- Added this line
    total += calories

avg = total / num_items if num_items > 0 else 0

print("Total calories consumed today:->", total)
print("Average calories consumed per item:->", avg)

print("Enter your daily calorie limit:")
limit = int(input())

if total > limit:
    print("You have exceeded your daily calorie limit.!!!!")
else:
    print("You are within your daily calorie limit.")

print()
print("~SUMMARY~")
print("Item\t\tCalories")

for i in range(num_items):
    print(f"{meal_names[i]}--->\t{calories_list[i]}")

print("-----------------------------")
print("Total calories consumed today:\t", total)
print("Average calories per item:\t", avg)
print("Daily calorie limit:\t\t", limit)
