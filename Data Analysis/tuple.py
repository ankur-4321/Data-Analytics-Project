# employee = (2, "rohan", "IT", 8000)
# print("employee_id", employee[0] )
# print("employee_name", employee[1])
# print("employee_department", employee[2])
# print("employee_salary", employee[3])

# Q1. Create a list of 5 fruits and print the complete list.

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print(fruits)

# Q2. Create a list of 5 numbers. Add a new number, remove one number, and print the updated list.
numbers = [10, 20, 30, 40, 50]

numbers.append(60)   # Add a new number
numbers.remove(20)   # Remove a number

print(numbers)

# Q3. Create a list of your favorite movies and print the first and last movie.movies = ["3 Idiots", "Dangal", "PK", "Bahubali", "KGF"]

movies = ["3 Idiots", "Dangal", "PK", "Bahubali", "KGF"]

print(movies[0])
print(movies[-1])

# Q4. Create a tuple containing 5 colors and print the third color.

colors = ("Red", "Blue", "Green", "Black", "White")

print(colors[2])

# Q5. Find how many times 20 appears and the index position of 40.

numbers = (10, 20, 30, 20, 40, 20)

print(numbers.count(20))
print(numbers.index(40))

# Q6. Create a set of 5 city names. Add a new city, remove one city, and print the final set.

cities = {"Lucknow", "Delhi", "Mumbai", "Kanpur", "Agra"}

cities.add("Jaipur")
cities.remove("Agra")

print(cities)

# Q7.Create a set numbers = {1, 2, 2, 3, 4, 4, 5}. Print the set and write your observation about duplicates.

numbers = {1, 2, 2, 3, 4, 4, 5}

print(numbers)

# Q8. Create a dictionary for a student containing Name, Age, and Course. Print all details.

student = {
    "Name": "Ankur",
    "Age": 21,
    "Course": "BCA"
}

print(student)

# Q9. Using the student dictionary: Update Age, Add City, Remove Course, and print the final dictionary.

student = {
    "Name": "Ankur",
    "Age": 21,
    "Course": "BCA"
}

student["Age"] = 22
student["City"] = "Lucknow"
student.pop("Course")

print(student)

# Q10. Create a list of dictionaries for students and print all student names, marks of Priya, and total number of students.
students = [
    {"Name": "Ankur", "Marks": 85},
    {"Name": "Priya", "Marks": 90},
    {"Name": "Rohit", "Marks": 78}
]
for student in students:
    print(student["Name"])
print(student["Name"])

print("Priya's Marks:", students[1]["Marks"])

print("Total Students:", len(students))
