def delete():
    try:
        delete = input("enter id: ")
        with open("Assignment12_emp.txt", "r") as f:
            emp = f.readlines()
        with open("Assignment12_emp.txt", "w") as f:
            flag = False
            for employee in emp:
                name, id = employee.strip().split("")
                if id != delete:
                    f.write(employee)
                else:
                    flag = True

            if flag:
                print("deleted ", employee)
            else:
                print("404 not found")
    except Exception:
        print("error")
