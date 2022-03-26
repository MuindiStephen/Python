

numbers = [1, 2, 3, 4]

def funct(n):
    return n

#result = map(funct, numbers)
#print(list(result))
print([funct(n) for n in numbers]) #putting it in form of a list

def addition(n):
    return n+n

res = map(addition, numbers)
print(list(res))

