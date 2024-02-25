#  generatore progam for testing
# generate a sequence of numbers
def gen(number):
    for i in range(1, number+1):
        print( f'{number} x {i} = {number}*{i}')
gen(10)