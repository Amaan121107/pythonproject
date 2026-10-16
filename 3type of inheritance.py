class ABS:
    def getData(self):
        self.z=50 #public inheritance in this all are use
        self._y=20 #protect inheritance only child will use
        self._x=10 #private inhertance only parent can access

class XYZ(ABS):
    def putData(self):
        print("HELLO")

    def getData(self):
        super().getData()
        self.z=50
        self._y=20
       
x1=ABS()
x1.getData()
print("z:",x1.z)
print("x:",x1._x)
print("y:",x1._y)
x1.putData()

    

        