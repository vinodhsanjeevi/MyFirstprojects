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
print( " --- ")
print("its final line --------- ")


@mynewdecor
def take(name):
    print("hi", name, 'good morning ...')


take("vinodh")
take("abc")
take("cow")
print("----------------------------------------------------")
print(" 9 9 9 9 9 9 9")
c = a + b
print("lkchkjdwckhdk")
