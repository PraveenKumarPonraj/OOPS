class Person:
    def __init__(self,name,empid):
        self.name=name
        self.id=empid


class Employee(Person):
    def __init__(self,name,empid,age,salary):
        super().__init__(name,age)
        self.age=age 
        self.salary=salary  

    def __str__(self):
        return 'Name={}\n age={}'.format(self.name,self.age)
emp = Employee("pk",101,23,15000)
print(emp)
