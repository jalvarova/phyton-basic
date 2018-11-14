# File Handling
def readFile():
    f = open("Python.txt", "r")
    texto = f.read()
    print(texto)
    f.close()



f = open('Python.txt', 'w')
f.write('hola mundo')
f.close()

readFile()

f = open("Python.txt", "a")
f.write('\t' + "Alvaro")
f.close()

readFile()


