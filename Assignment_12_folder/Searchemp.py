def Finding():
    try:
        search = input("enter id: ")
        with open("Assignment12_emp.txt", "r") as f:
            emp = f.readlines()
            flag = False

            for employee in emp:
                name, id = employee.strip().split("-")
                if id == search:
                    print("\nEmployee Found: \n")
                    print(f"name: {name}, id: {id}")
                    flag = True
                    break
                if not flag:
                    print("404 not found")
    except Exception as e:
        print("error")
