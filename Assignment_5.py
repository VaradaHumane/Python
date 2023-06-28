num = []
for i in range(5):
    num1 = int(input("Enter a number: "))
    num.append(num1)

sum = sum(num)
print("sum:", sum)

small= min(num)
print("small:", small)

large= max(num)
print("large:", large)

ascending = sorted(num)
print("ascending:", ascending)

descending = sorted(num, reverse=True)
print("descending:", descending)

Tuple = tuple(num)
print("tuple:",Tuple)

del num
print("List deleted.")
