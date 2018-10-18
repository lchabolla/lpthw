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

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"\nAge: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit type it in anywayself.
print("\nHere is a puzzle.\n")

what = add (age, subtract(height, multiply(weight, divide(iq, 2)))) # 4391

print("\nThat becomes: ", what, "Can you do it by hand?")
