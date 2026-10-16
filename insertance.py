class Employee:
    def __init__(self, eid=0, enm="", bs=0):
        self.eid = eid
        self.enm = enm
        self.bs = bs  

    def getData(self):
        self.eid = int(input("Enter employee id: "))
        self.enm = input("Enter employee name: ")

    def putData(self):
        print("\n--- Employee Details ---")
        print("Employee ID   :", self.eid)
        print("Employee Name :", self.enm)

class salary(Employee):
    def getData(self):
        super().getData()
       
        self.bs = int(input("Enter your basic salary: ")) 

    def calSalary(self):
        if self.bs < 5000:
            self.hra = self.bs * 0.10
            self.da = self.bs * 0.20
            self.pf = self.bs * 0.05
        elif self.bs < 10000:
            self.hra = self.bs * 0.20
            self.da = self.bs * 0.40
            self.pf = self.bs * 0.10
        else:
            self.hra = self.bs * 0.30
            self.da = self.bs * 0.60
            self.pf = self.bs * 0.15
        
   
        self.ns = self.bs + self.hra + self.da - self.pf

    def putData(self):
        super().putData()
        print("Eid " ,self.eid)      
        print("Basic Salary  :", self.bs)
        print("HRA:", self.hra)
        print("DA :", self.da)
        print("PF :", self.pf)
        print("Net Salary    :", self.ns)

s1 = salary()
s1.getData()
s1.calSalary()
s1.putData()
