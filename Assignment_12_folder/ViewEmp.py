def ViewEmp():
    try:
        with open("Assignment12_emp.txt", "r") as f:
            emp = f.readlines()
            if emp:
                print("\nEmployees: \n")
                for emp in emp:
                    name, id = emp.strip().split("-")
                    print(f"Name: {name}, ID: {id}")
            else:
                print("empty")
    except Exception as e:
        print("error")
