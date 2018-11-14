# String
#
#         String is an arrays of characters or you can say
#         it is collection of characters. Character may be
#         a alphabetic, numeric or special symbol

# str[0] = {1, 2, 3}
#
# i = 10
# for i in str:
#     print(i)

print("Introduction String\n")

py = 'Python 3'
print(py[3])

ch = int(input("Enter index number: "))
print(py[ch])
print()

print("String Concatenation\n")

str1 = 'My age is'
str2 = 13

print(str1 + "\t" + str(str2))
print()

print("String Formatting\n")

a1 = 18
a2 = 19

print(f"I ma {a1} and you are {a2}")
print()

print("String Indexing and String Slicing\n")

idx = "Alvaro"

print(idx[1:4])
print(idx[-1])
print(idx[0::1])
print(idx[-1::-1])

print()

print("Imports String Method\n")

pro = "Java Python C# Ruby PHP"
bit = 'p '

print(len(idx))
print(idx.lower())
print(idx.upper())
print(idx.replace("o","a"))
print(bit.isalpha())
print(bit.isdigit())
print(bit[1].isspace())
