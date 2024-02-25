# Example program for decorartor in python
def mynewdecor(func):
    def inner(name):
        if name == "vinodh":
            print("hi, its good morning.")
        elif name == "abc":
            print("its characters only...")
        elif name == "cow":
            print("its animal.")
        else:
            print(func(name))
    return inner


@mynewdecor
def take(name):
    print("hi", name, 'good morning ...')


take("vinodh")
take("abc")
take("cow")
print("---------------------------------------------------")
