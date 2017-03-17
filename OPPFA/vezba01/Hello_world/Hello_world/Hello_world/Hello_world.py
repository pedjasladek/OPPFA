import sys

print("__name__value:",__name__)

print("Hello World")

print("Hello World")

def main():
    print("Hello from main")
    myfoo("this is my message...")

def myfoo(arg1):
    print("Hello from foo")
    print("arg1 is: ",arg1)

if __name__ == "__main__":
    print("Hello from executable module")
    main()
else:
    print("Hello from else")