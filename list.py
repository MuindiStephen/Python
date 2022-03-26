team = ["steve", "jack", "alice", "gorge", "alice"];
print(team);
print(len(team))
print(team.count(2))

grade = [] #grade list
num = float(input("Enter first grade: "))
grade.append(num) #insert num to the list
num = float(input("Enter second grade: "))
grade.append(num)
num = float(input("Enter third grade: "))
grade.append(num)
num = float(input("Enter forth grade: "))
grade.append(num)
num = float(input("Enter fifth grade: "))
grade.append(num)

#summing up the grades
print("-------------------------------------------")
print(" Grades :  " ,grade)
sum(grade)

print(" Total Grade : ", sum(grade))


#computing the average
print(" ------------------------------------------- ")

average = sum(grade)/len(grade)
print("Average Grade : ",average)



#if statement

if (average >=70 and average <=100 ):
    print("First Class")

if (average >=60 and average <=69.9 ):
    print("First Class")
if (average >=50 and average <=59.9 ):
    print("First Class")
else:
    print("Pass")



#swapping
x = 10
y = 20

x, y = y,x
print(x, y)

#nested list
list1 = ['a', 'b', 'c', ['x', 'y', 'z']]
print(list1[3][2])

#mutable - when changed,takes change in a list

list2 = list1

list2[3] = 'f'

print(list2)
print(list1)


#True or false questions

x = "Dog"<"dog"
y = "fun" in "refunded"
n = 4
answ = "Y"
a = 1
b = 1
z = (a+b)<(2*a)
print(x)
print(y)
print(answ =="Y" or answ == "y")
print(answ =="Y" and answ == "y")


      




