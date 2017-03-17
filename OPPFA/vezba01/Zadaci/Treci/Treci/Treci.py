import sys

niz = []
n = 0
broj = 0
suma = 0

for i in range (2):
    n = input("Unesite string: ")
    niz.append(n)
    
print("Uneti stringovi su : ")

for i in range (2):
    print(niz[i])
niz[2] = niz[0] + niz[1]
print(niz[2])

