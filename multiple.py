class Trainee:
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age

class Role:
    def __init__(self,jobtitle,techonology):
        self.jobtitle=jobtitle
        self.technology=techonology
        


class Members(Trainee,Role):
    def __init__(self,name,id,age,jobtitle,technology):
        Trainee.__init__(self,name,id,age)
        Role.__init__(self,jobtitle,technology)
        print("Name: {}\n id: {}\n age: {}\n technology: {}\n jobtitle: {}".format(self.name,self.id,self.age,self.technology,self.jobtitle))

mem=Members("praveen",252,23,"Trainees","Python")
