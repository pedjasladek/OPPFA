from Hello_world import myfoo

print("__name__is ", __name__)

if __name__ == "__main__":
    print("Hello from executable module")
    myfoo("Message from other module")