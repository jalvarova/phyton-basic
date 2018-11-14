class Person:
    def __init__(self):
        self.name = ""

    def printName(self):
        self.name = input("Enter your name: ")
        print(f"Your name is : {self.name}")


c1 = Person()
c1.printName()
