from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?\n")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print(f"This is what you wrote:\n {line1}\n {line2}\n {line3}\n\n")
confirm = input("Is this correct? y/n\n")
if confirm == "y":
    print("I'm going to write these to the file.")

    target.write(line1)
    target.write("\n")
    target.write(line2)
    target.write("\n")
    target.write(line3)
    target.write("\n")

    print("And finally, we close it.")
    target.close()
else:
    if confirm == "n":
        print("Re-run program.")
        print("Closing file.")
        target.close()
