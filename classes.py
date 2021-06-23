# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def bio(self, place):
#         return f'my name is {self.name} i am {self.age} and i am from {place}'
#     def sayHello(self):
#         print("Hello there!")

# obj = User("Mohit", 19)
# print(obj.sayHello())
# print(obj.bio("Noida"))

class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say(self):
        return ("hi there!")
    def bio(self, place):
        return (f"my name is {self.name} and i am from {place}")

class Business(Customer):
    def move(self):
        print(f"my name is {self.name}")

user = Customer("Mohit" , 19)
print(user.say())

business = Business
print(business.move())