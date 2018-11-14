n1 = 1500
n2 = 2000

nl = []
for i in range(n1,n2):
    if i % 7 == 0 and i % 5 == 0:
        nl.append(str(i))
print(','.join(nl))
