from sys import argv # import arg from sys

script, input_file = argv # unpack variables

def print_all(f): # define function that prints all read from f
    print(f.read())

def rewind(f): # function returns head position to the beginning of f
    f.seek(0)

def print_a_line(line_count, f): # function print line at current line count
    print(line_count, f.readline())

current_file = open(input_file) # opens input file and sets it to current_file

print("First let's print the whole file:\n")

print_all(current_file) # calls print_all function on current_file variables

print("Now let's rewind, kind of like a tape.")

rewind(current_file) # calls rewind function on current_file which returns to line 1

print("Lets print three lines:")

current_line = 1 # sets current line to 1
print_a_line(current_line, current_file) # print current line (1) from current file

current_line += 1 # adds 1 to current_line and sets variable equal to new value
print_a_line(current_line, current_file) # prints current_line (2) from current_file

current_line += 1
print_a_line(current_line, current_file)
