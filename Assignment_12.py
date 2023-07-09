from Assignment_12_folder.Delemp import delete
from Assignment_12_folder.Addemp import Adddd
from Assignment_12_folder.Searchemp import Finding
from Assignment_12_folder.ViewEmp import ViewEmp
from Assignment_12_folder.UpdateEmp import Updatee


while True:
    print("\nEmployee Management Sysyen")
    print("1. Add")
    print("2. View")
    print("3. Search")
    print("4. Delete")
    print("5. Update")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        Adddd()
    elif choice == "2":
        ViewEmp()
    elif choice == "3":
        Finding()
    elif choice == "4":
        delete()
    elif choice == "5":
        Updatee()
    elif choice == "6":
        print("Okay...")
        break
    else:
        print("Wrong input bro")
