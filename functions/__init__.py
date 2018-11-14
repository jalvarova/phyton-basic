# Functions
#
#             A function is a block of code which only runs
#             when it is called

# Print function
def myfunc():
    print("My world")


myfunc()
myfunc()


# Parameter Function
def myfunc2(a, b):
    sum = a + b
    print(sum)


myfunc2(2, 3)


# Return function
def myfunreturn(a, b):
    return a * b


multi = myfunreturn(2, 3)
print(multi)


# Default parameter

def mydefault(a=13):
    print(a)


print(mydefault(35))

# Zip

list1 = ["Alvaro", "Diego", "Susan"]
list2 = ["Gonza", "Luciana", "Maru"]

print(dict(zip(list1, list2)))
