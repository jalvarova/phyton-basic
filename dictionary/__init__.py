# Dictionary
#
#             A dictionary is a collection which is an ordered changeable
#             and indexed by don't actually is done within college records.


person = {
    'name': 'Alvaro',
    'age': 23,
    'job': "Progeammer"
}

person['age'] = 26
print(f"Name the person is {person['name']} and your age is {person['age']}")

for x in person:
    print(x, end=",")

print()
for x in person.values():
    print(x, end=" ")

print(person.popitem())

person2 = dict(name="Diego", age=29, jon="Administrator")

print(person2)
