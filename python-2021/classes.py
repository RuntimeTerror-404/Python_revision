
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHello(self, place):
        self.place = place
        print(f"my name is {self.name} and my age is {self.age}")
        print(f"i am from {place}")

    def p(self, passion):
        self.passion = passion
        print(f"my passion is {passion}")


# obj = User("Mohit", 19)
# obj.sayHello("Noida")
# obj.p("Coding")

# print(obj.age)

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} can bark because he is a dog")

    def body(self, color):
        self.color = color
        print(f"{self.breed}'s color is {color}")

    def life(self, age):
        self.age = age
        if(self.breed == "German Sepherd"):
            print(f"{self.name} can live more than {age} years")
        else:
            print(f"{self.name} can not live more than {age} years")


dog = Dog("Sipi", "German Sepherd")

dog.life(13)
dog.body('white')
dog.bark()
print(dog.name)
