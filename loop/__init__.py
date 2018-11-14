# For Loop
#
#             A "for loop" is written by using for keyword
#             A for loop is used for iterating over a sequence

ch = int(input("Enter Number : "))
n1 = 0
n2 = 1
next = 0

for i in range(1, ch):
    if i == 1:
        print(n1, end=",")
    if i == 2:
        print(n2, end=",")

    next = n1 + n2
    n1 = n2
    n2 = next

    print(next, end=",")

i = 1
sum = 0
print()
while i <= ch:
    sum = sum + i
    i += 1
print(f"Sum: {sum} ")

x = int(input("Enter x Number : "))
y = int(input("Enter y Number : "))

for i in range(x):
    for j in range(y):
        if j == 10:
            break
        elif j == 2:
            continue
        else:
            print("*", end='')
    if i == 2:
        pass
    else:
        print("\n")
