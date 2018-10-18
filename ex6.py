types_of_people = 10 # define types of people variable
x = f"There are {types_of_people} types of people." # defining x, f is to format string variable when printing

binary = "binary" # defining binary variable with string "binary"
do_not = "don't" # defining do_not variable with string value "don't"
y = f"Those who know {binary} and those who {do_not}." # defining y, f is to format string variable when printing

print(x) # prints x variable
print(y) # prints y variable

print(f"I said: {x}") # prints additional string data along with variable x string
print(f"I also said: '{y}'") #prints additonal string data along with variable y string

hilarious = False # defining variable hilarious with boolean False
joke_evaluation = "Isn't that joke so funny?! {}" # defining variable that will accept any variable when formatted with .format()

print(joke_evaluation.format(hilarious)) # prints joke_evaluation variable and formats hilarious string variable

w = "This is the left side of..." # defining w variable
e = "a string with a right side." # defining e variable

print(w + e) # prints both string variables, no formatting required as they are just string, no variables
