#iterativeness of items in lists
fruits = ['mango', 'orange', 'guavas']

for fruit in fruits:
     if fruit=='mango':
        print("Yes")
     else:
        print("No Mangoes")
    
for x in range(1,20):
    
        print(x)

#string methods
        #split
y = input("Enter sth ")
print(y.split()) 
print(y.split('a'))

    #slice operator
students = ['Steve', 'Michael', 'jack', 'Kim']
print(students[3:3])

students.append('Dancan')
print(students)

#functions

def addTwo(x):
    return x + 2

sum = addTwo(7)
print(sum)

def printString(string):
    print(string)
print(printString("Hello World"))


def rectangleArea(length, width):
    return length*width

print(rectangleArea(10, 20))

def AreaOfCircle(r):
    return (22/7 *r * r)

print("Area of a circle of radius ",{r} , AreaOfCircle(7))



  
