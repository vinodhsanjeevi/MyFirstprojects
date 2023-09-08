def mydecor(func):
    def innerfunc(name):
        if name == "vinodh":
            print("yes,good mrng it is..")
        else:
            print("yes,ram is god..")
    return innerfunc
@mydecor
def decor(name):
    print("hi", name ,"good moring")
    
decor("vinodh")
decor("ram")
# this is the way of doing and working decorator 
# thank you
print("for testing only ------------- nothing is changed here")
print("it is final line -----------------------------------------------------------------------------")