import Employee

employee = []

while True:

    print("\n----- MENU -----")
    print("1. Insert")
    print("2. Update")
    print("3. Display")
    print("4. Sorting")
    print("5. Searching")
    print("6. Delete")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    match ch:

        case 1:
            emp = Employee.Employee()
            emp.getData()
            emp.calSalary()

            found = False

            for e in employee:
                if e.eid == emp.eid:
                    found = True
                    break

            if found:
                print("Employee ID already exists")
            else:
                employee.append(emp)
                print("Employee data successfully added")
                
        
        case 2:
            key = input("Enter Employee ID to update: ")
            found = False
            for i in range(len(employee)):
                
                if str(employee[i].eid) == key:
                    e1=Employee.Emp()
                    e1.enm = input("Enter employee name: ")
                    e1.bs=int(input("input enter salary"))
                    e1.eid=employee[i].eid
                    e1.calSalary()
                    employee[i]=e1
                    found=True                    
                    if not found:
                        print("Employee ID not found")
        
        case 3:
                    if len(employee) == 0:
                        print("No data found")
                    else:
                        print("\n----- EMPLOYEE DETAILS -----")
        
                        for emp in employee:
                            emp.putData()
        
        case 5:
                    key = input("Enter Employee ID or Name: ").lower()
                    found = False
        
                    for emp in employee:
        
                        if str(emp.eid) == key or emp.enm.lower() == key:
                            emp.putData()
                            found = True
        
                    if not found:
                        print("Employee not found")
        

        case 7:
            print("Exit the program")
            break

        
        case _:
            print("Invalid choice! Please enter 1-7.")
