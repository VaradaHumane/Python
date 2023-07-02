def assignment7(file="trial.txt"):
    try:
        yes = open(file, "a+")

        roll = int(input("roll no: "))
        name = input("name: ")
        classs = input("class: ")

        yes.writelines(
            ["roll no: {0}, name: {1}, class: {2}".format(roll, name, classs)]
        )

        yes.seek(0)
        dataholder = yes.readlines()

        for line in dataholder:
            print(line)

    except IOError:
        print("error")


assignment7()
