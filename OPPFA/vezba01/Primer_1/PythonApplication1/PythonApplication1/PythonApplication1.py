import sys

if len(sys.argv) > 1:
    print("Parametar prosledjen")
    print("arg is: ", sys.argv[1])
    name = sys.argv[1]
else:
    print("Nije prosledjen parametar")
    sys.exit()

x = [(1,2), (3,4), (5,6), (7,8), (9,10)]
#print(x)

dictionary = {name:x}

dictionary["asdf"] = 5

for key, value in dictionary.items():
    print("key: ", key, "value: ", value) 
