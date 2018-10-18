from sys import argv # importing argv from sys for line 12

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input() #was missing variable
print("How much do you weigh?", end=' ') # missing ) at end of print()
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

script, filename = argv # why is this being called here?

txt = open(filename) # misspelled filename

print(f"Here's your file {filename}:") # missing f for string function
print(txt.read())# missing t in txt.read()

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read()) # replace _ for . in txt_again.read() as it is a function


print('Let\'s practice everything.') # two ways to fix this \ or by sub '' for ""

# why the following line? what are you trying to accomplish?
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------") # missing closing "
print(poem)
print("--------------") # missing opening "


five = 10 - 2 + 3 - 6 # missing minus six, implied another digit with trailing -
print(f"This should be five: {five}") # missing )

def secret_formula(started): # missing : at end of function def
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100 # missing / operand
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) # missing crates variable, variable found in line 61

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point) # missing _ for start_point
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula)) # no need for * in (*formula)?



people = 20
cats = 30 # misspelled cats
dogs = 15


if people < cats:
    print ("Too many cats! The world is doomed!") # missing ()

if people > cats: # < operand reversed
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs: # missing : at end of if statement
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs: # missing : at the end of if statement
    print("People are less than or equal to dogs.") # missing ending "

if people == dogs: # = sets variable, == compares
    print("People are dogs.")
