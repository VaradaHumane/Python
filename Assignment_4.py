# break statement
for i in range(1, 6):
    if i == 4:
        break
    print(i)


# continue statement
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)


# pass statement
for i in range(1, 6):
    if i == 3:
        pass
    else:
        print(i)


# for with else
for i in range(1, 6):
    print(i)
else:
    print("loop done")


# while with else
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop condition is False!")
