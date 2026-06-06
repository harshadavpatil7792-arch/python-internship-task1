#Task 1: Sum of Two Numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2

print("Sum =", sum)



# Task 2: Odd or Even Checker
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# Task 3: Factorial Calculator
num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial =", factorial)



# Task 4: Fibonacci Sequence Generator
n = int(input("How many terms? "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c



# Task 5: Reverse a String
text = input("Enter a string: ")

reverse = text[::-1]

print("Reversed String:", reverse)



# Task 6: Palindrome Checker
text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")



# Task 7:Leap Year Check
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")



# Task 8: Armstrong Number Check
num = int(input("Enter a number: "))

digits = str(num)
power = len(digits)

sum_of_powers = 0

for digit in digits:
    sum_of_powers += int(digit) ** power

if sum_of_powers == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")