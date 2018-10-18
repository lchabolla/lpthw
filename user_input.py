from sys import argv

script, user_name, = argv
prompt = 'Type something, stupid!>'

print(f"{v1} is a stupid user name.")
print(f"You will be known as PwNdN3wB")

user_name = "PwNdN3wB" ##Bad practice, hardcoding

print(f"{v1}, welcome. What kind of computer do you have? Apple or PC")
v2 = input(prompt)

if v2 == "Apple":
    print(f"{v2}...You paid too much.")
else:
    print(f"Windows or Linux?")
    v2 = input(prompt)
    if v2 == "Windows":
        print(f"{v2}? Please tell me you're a gamer...")
    else:
        if v2 == "Linux":
            print(f"{v2}, FTW! You must have no life.")
        else:
            print(f"{v2}. Capitilize the letter or learn how to read/type.")

print(f"You're still here? Ugh...")
v3 = input(prompt)
