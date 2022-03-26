class Dog(object):

    def __init__ (self, name, age, origin, gender):
        self.name = name
        self.age = age
        self.origin = origin
        self.gender = gender


    def display(self):
            print("My dog is called ", self.name  ,"and its ", self.age ," years old", "its from ",
                  self.origin ," Country  .Its also ", self.gender)



d = Dog('Tom', 6, 'Mexico', 'male')
d.display()

#inheritance
class Cat(Dog):
    def __init__(self, name, age, origin, gender, color):
        super().__init__(name, age,origin, gender) 
        self.color = color

    def speak(self):
        print("Meow !")

c = Cat("Nyau", 1, "England", "Female", "Gray")
c.display()
c.speak()
    
