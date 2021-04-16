class Details:
    def __init__(self):
        self.__id="<No Id>"
        self.__name="<No Name>"
        self.__gender="<No Gender>"
    def setData(self,id,name,gender):
        self.__id=id
        self.__name=name
        self.__gender=gender
    def showData(self):
        print("Id: ",self.__id)
        print("Name: ", self.__name)
        print("Gender: ", self.__gender)

class Employee(Details): 
    def __init__(self):
        self.__company="<No Company>"
        self.__dept="<No Dept>"
    def setEmployee(self,id,name,gender,comp,Technology):
        self.setData(id,name,gender)
        self.__company=comp
        self.__Technology=Technology
    def showEmployee(self):
        self.showData()
        print("Company: ", self.__company)
        print("Technology: ", self.__Technology)

class Trainee(Details): 
    def __init__(self):
        self.__Technology="<No Tech>"
        
    def setEmployee(self,id,name,gender,comp,Technology):
        self.setData(id,name,gender)
        self.__company=comp
        self.__Technology=Technology
    
    def showEmployee(self):
        self.showData()
        print("company:",self.__company)
        print("Technology: ", self.__Technology)
        

def main():
    print("Employee Detail")
    e=Employee()
    e.setEmployee(1,"Saran","Male","5G","Angular")
    e.showEmployee()
    print("\nTrainee Detail")
    d = Trainee()
    d.setEmployee(2, "ramalingam", "male", "5G", "Python")
    d.showEmployee()

if __name__=="__main__":
    main()