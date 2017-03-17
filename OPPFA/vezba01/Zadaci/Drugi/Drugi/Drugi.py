import sys

niz = []
n = 0
broj = 0
suma = 0

n = input("Unesite koliko brojeva zelite da se sabere: ")

for i in range (int (n)):

    broj = input("Unesite "+ n + " brojeva koje zelite da se saberu: ")
    niz.append(int (broj))
    suma += int (broj) * int(broj)
print("Brojevi koji se sabiraju: ")

for i in range (int (n)):
    print(niz[i])
print("Zbir: ", suma)