print("How old are you?", end=' ')
age = int(input())
print("How tall are you?")
print("Feet?", end=' ')
height_feet = int(input())
print("Inches?", end=' ')
height_inch = int(input())
print("How much do you weigh in pounds?", end=' ')
weight = int(input())


print(f"So, you're {age} old, {height_feet}' {height_inch}\" tall and {weight} pounds heavy.")

lbs_per_kg = 2.20462
weight_kg = weight * lbs_per_kg

cm_per_in = 2.54
cm_per_ft = cm_per_in * 12
height_cm = height_feet * cm_per_ft + height_inch * cm_per_in

hours_per_year = 8765.81277
age_hours = hours_per_year * age

print(f"You are {age_hours} hours old, weigh {weight_kg} kilograms and are {height_cm} centimeters tall.")
