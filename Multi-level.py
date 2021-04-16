class Animal:
    def eat(self):
        print("i can eat")
class Dog(Animal):
    def bark(self):
        print("I can run")
class Cat(Dog):
    def get_grumpy(self):
        print("i am getting grumpy")        
dog1=Dog()
dog1.eat()
dog1.bark()                

cat1=Cat()
cat1.eat()
