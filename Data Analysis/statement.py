# A = 5
# B = 45
# if A > B:
#     print("A is greater than B")
# else:
#     print("B is greater than A")

# Marks = int(input("Enter your marks:"))
# if Marks >= 60:
#     print("you have passed")
# else:
#     print("you have failed")
    
# def table(n):
#     for i in range(1, 11):
#         print(n, "x", i, "=", n * i)
# table(5)

# odd = lambda x: "even(x)" if x % 2 == 0 else "odd(x)"
# print(odd(7))

# Q1. Check whether a number is positive, negative, or zero.
num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

# Q2. Check whether a number is even or odd.
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
    
# Q3. Find the largest of three numbers using if-elif-else.
a = 10
b = 25
c = 15

if a > b and a > c:
    print("Largest number is:", a)
elif b > c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)
    
# Q4. Print numbers from 1 to 20 using a for loop.
for i in range(1, 21):
    print(i)
    
# Q5. Print all even numbers between 1 and 50.
for i in range(2, 51, 2):
    print(i)

# Q6. Print the multiplication table of any number entered by the user.
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Q7. Find the sum of numbers from 1 to 100 using a loop.
total = 0

for i in range(1, 101):
    total += i

print("Sum =", total)

# Q8. Create a function to find the square of a number.
def square(num):
    return num ** 2

print(square(8))

# Q9. Create a function that takes two numbers and returns their sum.
def add(a, b):
    return a + b

print(add(10, 20))

# Q10. Create a function to check whether a student has passed (marks >= 40).
def check_pass(marks):
    if marks >= 40:
        return "Passed"
    else:
        return "Failed"

print(check_pass(45))