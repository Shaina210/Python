

print("Hello World")

myname = "Shaina"

print(f"Hello {myname}! How are you?")

def hello_name(someone):
    print(f"Hello {someone}! This is a function.")




def repeat_hello(somename, n_times):
    for i in range(n_times):
        print(f"Hello there {somename}! This is a print statement number: {i+1}.")

if __name__ == "__main__":
    hello_name("Class")
    hello_name("Shaina")
    hello_name("Folks")

    repeat_hello(somename="Shaina", n_times=6)
