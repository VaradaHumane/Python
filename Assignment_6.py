def Assignmnet_6(roll_no, name):
    my_list = [roll_no, name]
    my_tuple = (roll_no, name)
    my_set = {roll_no, name}
    my_dict = {"roll_no": roll_no, "name": name}
    print("original values:")
    print("list", my_list, "\n\n")

    roll_no = int(input("enter new roll no: "))
    name = input("enter new name: ")

    print("\n\nvalues after updating:")
    print("Roll No:", roll_no)
    print("Name:", name, "\n\n")

    del my_list
    del my_tuple
    del my_set
    del my_dict


Assignmnet_6(10, "a")
