def Updatee():
    try:
        NewID: input("enter id: ")
        with open('Assignment12_emp.txt', '+r') as f:
            emp = f.readlines()
            flag = False

            for i, employee in enumerate(emp):
                name, id = employee.strip().split('-')
                if id == NewID:
                    flag = True

                    print("\nThe guy u selected is: \n")
                    print(f"name: {name}, id: {id}")

                    newGuy = input("enter new guy's name: ")
                    new_id = input("enter new guy's id: ")

                    if newGuy:
                        emp[i] = f"{newGuy}-{new_id}\n"
                    else:
                        emp[i] = f"{name}-{id}\n"
                    
                    f.seek(0)
                    f.writelines(emp)
                    f.truncate()

                    print("updated")
                    break

            if not flag:
                print("404 not found")
    except Exception:
        print("error")