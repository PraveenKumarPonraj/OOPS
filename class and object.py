class Employee:
    '''Employee Details''' #Documentation string
    
    def __init__(self,Empcode,name,age,gender,role):
        self.Empcode=Empcode
        self.name=name
        self.age=age
        self.gender=gender
        self.role=role


Emp1 = Employee("E252","Praveen",23,"Male","Trainee")

Emp2 = Employee("E253","Ram",22,"Male","Trainee")

Emp3 = Employee("E254","vignesh",25,"Male","Trainee")

Emp4 = Employee("E255","sandhya",24,"female","Trainee")

print(Emp1.__dict__)
print(Emp2.__dict__)
print(Emp3.__dict__)
print(Emp4.__dict__)

