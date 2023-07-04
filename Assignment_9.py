from Assignment_9_file import File, StringOperations, Exception

file_op = File("trial.txt")
file_op.create_file()
file_op.write_file("Sup")
print(f"data: {file_op.read_file()}")
file_op.append_file("hie")


print()


# palindrome check


str = input("enter string: ")
string_op = StringOperations(str)
if string_op.palin() == True:
    print("is palindrome")
else:
    print("not palindrome")


# everything else
print(f"lowercase: {string_op.lower()}")

print(f"uppercase: {string_op.upper()}")

print(f"caps: {string_op.caps()}")

print(f"unique characters: {string_op.count_chars()}")

print(f"splitted: {string_op.split_string()}")

print(f"length is: {string_op.string_length()}")

print(f"reversed string: {string_op.rev_string()}")

oldString = input("enter substring: ")
newString = input(f"enter a new substring to replace: {oldString}: ")
replacedString = string_op.replace(oldString, newString)
print(f"replacing: {replacedString}")

print()


# try block

try:
    string_op.raise_exception()
except Exception as e:
    print(e)

a