# Operators
#
#             In python, Operators are used to perform operations
#             on variables and values


a = 5
b = 2

print("Operators in Python")
print()
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)

print("Assignment in Python")
print()

print("= , += , -=, *= , /= . %=")

print("Comparing in Python")
print()

number1 = input("First Number : ")
number2 = input("Second Number : ")

if number1 > number2:
    print(f"number {number1}, is greater.")
elif number1 < number2:
    print(f"number {number1}, is smaller.")
elif number1 <= number2:
    print(f"number {number1}, is smaller or equal")
elif number1 == number2:
    print(f"number {number1}, is equals")
else:
    print("Enter correct number")


print("Logical Operations")
print()

print("and or not ")
if number1 > number2 and number1 < number2:
    print(f"number {number1}, is greater.")
elif number1 <= number2 or  number1 == number2:
    print(f"number {number1}, is smaller or equal")
elif not(number2 > 10):
    print("Enter number renew")


print("is is not || in in not")
