#  generatore progam for testing
# generate a sequence of numbers

def gen(number):
    for i in range(1, number+1):
        yield ( f'{number} x {i} = {number}*{i}')
p = gen(10)
for i in p:
    print(i)