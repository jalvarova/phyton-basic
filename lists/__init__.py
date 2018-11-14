# Lists
#         A lists is a collection which is ordered and changeable.
#         In Python lists are written with [].

mylist = ['Alvaro', 'Diego', 13, 3.5]

mylist[1] = "Gonzalo"
print(mylist)

print()
for x in mylist:
    print(x)

# Length of the list
print()
print(f"My List : {len(mylist)}")

# Append List

mylist.append(20)
print(mylist)
# Insert List

mylist.insert(5,'G')
print(mylist)

#Remove List
mylist.pop(2)
print(mylist)

#Clear List
mylist.clear()
print(mylist)


del mylist

#Constructor
mylist2 = list(("red", "blue", "yellow"))
print(mylist2)

#Reverse
print(mylist2.reverse())
