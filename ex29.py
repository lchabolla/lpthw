people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")

if people == dogs and people <= cats:
    print("People are dogs and there are too many cats.")

# Study drills
# 1. The if statement run the code underneath the statement if it matches the condition
# 2. The code needs to be indented so the python recognizes that this is the code that should be ran
# if it matches the boolean condition
# 3. If you don't indent you get an IndentationError
# 4. Is on line 29 - 30
# 5. If you change the initial values, the output may differ depending if the if conditions are met
