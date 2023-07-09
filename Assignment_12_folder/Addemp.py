def Adddd():
    try:
        with open('Assignment12_emp.txt', 'a') as f:
            name = input("enter name: ")
            id = input("enter id: ")
            
            f.write(f"{name}-{id}\n")
            print("done")
    except Exception:
        print("error occured in adding")