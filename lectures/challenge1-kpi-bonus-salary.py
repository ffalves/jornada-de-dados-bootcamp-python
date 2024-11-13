# A constant value for the bonus
BONUS_CONSTANT = 1000

# Ask the user for their name, salary and bonus percentage
name = input("Hi! What is your name? ")
salary = float(input("What is your salary? "))
bonus = float(input("What is your bonus percentage? "))
bonus_per = bonus/100

# Calculate the total salary
total = bonus_per * salary + salary + BONUS_CONSTANT

# Print the total salary
print(f"Hi {name}, your total salary is {total}")
