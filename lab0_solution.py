# Task 1: Variables and Output
name = "Daniel"
surname = "Szpakowski"
full_name = name + " " + surname
print(name)
print(surname)
print(full_name)
# Task 2: F-Strings
greeting = f"Hello, my name is {full_name}!"
print(greeting)
# Task 3: Arithmetic Operations
a = 17
b = 5
print(a+b, a-b, a*b, a/b, a//b, a%b, a**b)
# Task 5: Lists
my_list = ["apple", "banana", "cherry", "betroot", "cucumber"]
print(my_list[0], my_list[-1], my_list[2:5])
# Task 6: List Operations
shopping_list = []
shopping_list.append("milk")
shopping_list.append("bread")
shopping_list.append("eggs")
print(shopping_list, len(shopping_list))
shopping_list.remove("milk")
print(shopping_list, len(shopping_list))
# Task 7: Dictionary
book = {
"title:": "Pan Tadeusz",
"author:": "Adam Mickiewicz",
"year:": 1834,
"pages:": 350,
"is_available:": True,
}
for key, value in book.items():
    print(key, value)
# Task 8: Conditional Statement
score = 75
if score >= 95:
    print("Grade: 10")
elif score >= 85:
    print("Grade: 9")
elif score >= 75:
    print("Grade: 8")
elif score >= 65:
    print("Grade: 7")
elif score >= 55:
    print("Grade: 6")
elif score >= 50:
    print("Grade: 5") 
else:
    print("Grade: fail")
    # Task 9: Boolean Logic
is_sunny = True
is_warm = True
is_weekend = False
print(is_sunny and is_warm)
print(is_sunny or is_weekend)
print(not is_weekend)
print(is_sunny and is_weekend)
# Task 10: For Loop
for i in range(1, 11, 2):
    print(i)
# Task 11: While Loop
total = 0
i = 1
while i <=10:
    total += i
    i += 1
print(total)
# Task 12: Function with Return Value
def calculate_rectangle_area(width, height):
    return width*height
result = calculate_rectangle_area(7, 2)
print(result)