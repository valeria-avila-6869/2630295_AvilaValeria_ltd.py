"""
Manejo de listas, tuplas y diccionarios en Python 
2630295
Valeria Alejandra Avila Ponce
I M1-2
"""
import math
import string

# Creates a shopping list from comma-separated input, adds one item,
# reports the number of items, and checks whether a search item exists.
# Inputs:
# - initial_items_text: comma-separated item names.
# - new_item: item to add.
# - search_item: item to search for.
# Outputs: Items list, total item count, and a Boolean search result.
# Validations:
# - The initial text, new item, and search item must not be blank.
# - Extra spaces around item names are removed.
# - An empty initial list is rejected.
# Test cases:
# 1) Normal: "apple, banana", new item "orange", search "banana".
# 2) Border: "apple", new item "pear", search "pear".
# 3) Error: blank initial text or blank new/search item.

def problem_1():
    print("\n--- Problem 1: Shopping List Basics ---")
    initial_items_text = input("Enter initial items separated by commas: ").strip()
    new_item = input("Enter a new item: ").strip()
    search_item = input("Enter an item to search for: ").strip()

    if not initial_items_text or not new_item or not search_item:
        print("Error: invalid input")
        return

    items_list = [item.strip() for item in initial_items_text.split(",") if item.strip()]
    if not items_list:
        print("Error: the initial list cannot be empty")
        return

    items_list.append(new_item)
    is_in_list = search_item in items_list

    print("Items list:", items_list)
    print("Total items:", len(items_list))
    print("Found item:", str(is_in_list).lower())

# Creates two 2D points as tuples, calculates their Euclidean distance,
# and calculates the midpoint between them.
# Inputs: x1, y1, x2, y2: numeric coordinates that can be converted to floats.
# Outputs: Point A, Point B, distance, and midpoint.
# Validations: Each coordinate must be a valid finite number.
# Test cases:
# A=(0, 0), B=(3, 4), distance=5.
# A=(2, 2), B=(2, 2), distance=0.
# Error: enter "abc" for any coordinate.

def problem_2():
    print("\n--- Problem 2: Points and Distances ---")
    try:
        x1 = float(input("Enter x1: ").strip())
        y1 = float(input("Enter y1: ").strip())
        x2 = float(input("Enter x2: ").strip())
        y2 = float(input("Enter y2: ").strip())
        coordinates = (x1, y1, x2, y2)
        if not all(math.isfinite(value) for value in coordinates):
            raise ValueError
    except ValueError:
        print("Error: invalid input")
        return

    point_a = (x1, y1)
    point_b = (x2, y2)
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", round(distance, 4))
    print("Midpoint:", midpoint)

# Stores product names and unit prices in a dictionary, then calculates
# the total cost for a requested quantity when the product exists.
# Inputs:
# - product_name: product name.
# - quantity: positive integer quantity.
# Outputs:
# - Unit price, quantity, and total, or a product-not-found error.
# Validations:
# - Product name must not be blank.
# - Quantity must be an integer greater than zero.
# - Product names are matched without regard to letter case.
# Test cases:
# "apple", quantity 2, unit price 10.0, total 20.0.
# "notebook", quantity 1.
#  Error: quantity 0, quantity "two", or unknown product.


def problem_3():
    print("\n--- Problem 3: Product Catalog ---")
    product_prices = {
        "apple": 10.0,
        "notebook": 25.5,
        "pencil": 5.0,
        "water": 12.0
    }

    product_name = input("Enter product name: ").strip().lower()
    quantity_text = input("Enter quantity: ").strip()

    if not product_name:
        print("Error: invalid input")
        return
    try:
        quantity = int(quantity_text)
    except ValueError:
        print("Error: invalid input")
        return

    if quantity <= 0:
        print("Error: quantity must be greater than zero")
        return
    if product_name not in product_prices:
        print("Error: product not found")
        return

    unit_price = product_prices[product_name]
    total_price = unit_price * quantity
    print("Unit price:", unit_price)
    print("Quantity:", quantity)
    print("Total:", round(total_price, 2))

# Stores each student's grades in a list inside a dictionary.
# Calculates the average and determines whether the student passed.
# Inputs:
# - student_name: registered student's name.
# Outputs:
# - Grades, average, and a Boolean passed result, or an error.
# Validations:
# - Student name must not be blank.
# - The student must exist in the dictionary.
# - The grade list must not be empty.
# Test cases:
# "Alice" has [90, 85, 80], average 85, passed true.
# "Charlie" has [70], passed true.
# Error: blank name or unknown student.


def problem_4():
    print("\n--- Problem 4: Student Grades ---")
    grades = {
        "alice": [90.0, 85.0, 80.0],
        "bob": [60.0, 68.0, 65.0],
        "charlie": [70.0],
        "diana": [95.0, 100.0, 92.0]
    }

    student_name = input("Enter student name: ").strip().lower()
    if not student_name:
        print("Error: invalid input")
        return
    if student_name not in grades:
        print("Error: student not found")
        return

    student_grades = grades[student_name]
    if not student_grades:
        print("Error: no grades available")
        return

    average = sum(student_grades) / len(student_grades)
    is_passed = average >= 70.0
    print("Grades:", student_grades)
    print("Average:", round(average, 2))
    print("Passed:", str(is_passed).lower())
# Converts a sentence to lowercase, removes common punctuation,
# creates a list of words, and counts each word with a dictionary.
# Inputs:
# - sentence: a non-empty sentence.
# Outputs:
# - Words list, frequency dictionary, and most common word.
# Validations:
# - Sentence must not be blank.
# - Common punctuation is replaced with spaces before splitting.
# - The resulting word list must not be empty.
# Test cases:
# Normal: "red blue red" -> red: 2, blue: 1.
# Border: "Hello!" -> hello: 1.
# Error: blank text or punctuation only.


def problem_5():
    print("\n--- Problem 5: Word Frequency Counter ---")
    sentence = input("Enter a sentence: ").strip()
    if not sentence:
        print("Error: invalid input")
        return

    cleaned_sentence = sentence.lower()
    for punctuation_mark in string.punctuation:
        cleaned_sentence = cleaned_sentence.replace(punctuation_mark, " ")

    words_list = cleaned_sentence.split()
    if not words_list:
        print("Error: no words found")
        return

    freq_dict = {}
    for word in words_list:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

    most_common_word = max(freq_dict, key=freq_dict.get)
    print("Words list:", words_list)
    print("Frequencies:", freq_dict)
    print("Most common word:", most_common_word)

# Adds or updates a contact, searches for a phone number, or deletes
# a contact using a dictionary.
# Inputs:
# - action_text: ADD, SEARCH, or DELETE.
# - name: contact name.
# - phone: non-empty phone number, only for ADD.
# Outputs: A success message or a clear error message.
# Validations:
# Action is normalized to uppercase and must be supported.
# Contact name must not be blank.
# Phone number must not be blank for ADD.
# Test cases:
# ADD "Morgan" with phone "5551234567".
# SEARCH for an existing contact; DELETE the last contact.
# invalid action, blank name/phone, or unknown contact.


def problem_6():
    print("\n--- Problem 6: Simple Contact Book ---")
    contacts = {
        "Alice": "1234567890",
        "Bob": "0987654321",
        "Charlie": "5551234567"
    }

    action_text = input("Enter action (ADD, SEARCH, DELETE): ").strip().upper()
    if action_text not in ("ADD", "SEARCH", "DELETE"):
        print("Error: invalid action")
        return

    name = input("Enter contact name: ").strip()
    if not name:
        print("Error: invalid input")
        return

    if action_text == "ADD":
        phone = input("Enter phone number: ").strip()
        if not phone:
            print("Error: invalid input")
            return
        contacts[name] = phone
        print("Contact saved:", name, phone)

    elif action_text == "SEARCH":
        phone = contacts.get(name)
        if phone is None:
            print("Error: contact not found")
        else:
            print("Phone:", phone)

    elif action_text == "DELETE":
        if name in contacts:
            contacts.pop(name)
            print("Contact deleted:", name)
        else:
            print("Error: contact not found")



# MAIN MENU
# Select one problem at a time. Enter 0 to exit.

def main():
    problem_actions = {
        "1": problem_1,
        "2": problem_2,
        "3": problem_3,
        "4": problem_4,
        "5": problem_5,
        "6": problem_6
    }

    while True:
        print("\n========== PYTHON COLLECTIONS MENU ==========")
        print("1. Shopping List Basics")
        print("2. Points and Distances")
        print("3. Product Catalog")
        print("4. Student Grades")
        print("5. Word Frequency Counter")
        print("6. Simple Contact Book")
        print("0. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        if choice not in problem_actions:
            print("Error: invalid input")
            continue
        problem_actions[choice]()


if __name__ == "__main__":
    main()


# Conclusions
# Lists are appropriate when a collection needs to change over time.
# Their append, insert, remove, and pop methods support flexible updates.
# Tuples are useful for fixed data because their elements cannot be reassigned.
# Dictionaries make it convenient to retrieve values through descriptive keys.
# Combining dictionaries and lists can represent records such as students and grades.
# Input validation helps prevent common errors and makes programs more reliable.
# Separating each task into a function improves readability and testing.
#
# References
# 1) Python Software Foundation. Python Standard Library: Built-in Types.
#    https://docs.python.org/3/library/stdtypes.html
# 2) Python Software Foundation. Python Tutorial: Data Structures.
#    https://docs.python.org/3/tutorial/datastructures.html
# 3) Python Software Foundation. Built-in Functions.
#    https://docs.python.org/3/library/functions.html
# 4) Python Software Foundation. Errors and Exceptions.
#    https://docs.python.org/3/tutorial/errors.html
# 5) Python Software Foundation. String Methods.
#    https://docs.python.org/3/library/stdtypes.html#string-methods
# 6) Python Software Foundation. math — Mathematical functions.
#    https://docs.python.org/3/library/math.html