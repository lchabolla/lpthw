def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Dividing {a} / {b}")
    return a / b

print("\nLet's do some math with just functions!\n")

age = float(input("What's your age?\s"))
height = float(input("What's your height in inches?\s"))
weight = float(input("What's your weight in pounds?\s"))
iq = float(input("What's your IQ?\s"))

print(f"\nAge: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit type it in anywayself.
print("\nHere is a puzzle.\n")

what = add (age, subtract(height, multiply(weight, divide(iq, 2)))) # 4391

print("\nThat becomes: ", what, "Can you do it by hand?")
