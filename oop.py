class Dog:
    
#declaring the object
    name = "Tom"
    age = 20


    def fun(self):
            print("My Dog is called ", self.name)
            print("It is aged",self.age)


#object instantiation
D1 = Dog()
print(D1.name) #accessing class atttributes
D1.fun()


class Person:

    def __init__(self, name, dOB, gender, career):
        self.name = name
        self.dOB = dOB
        self.gender = gender
        self.career = career

    def display(self):
        print("This is ", self.name)
        print("Am born ", self.dOB )
        print("I am ", self.gender)
        print("Am a ",self.career )

P1 = Person("Steve", "1123", "male", "SE")
P1.display()

        
            


    


