# Fitness Tracker, helps keep track of daily exercise hours and estimates weekly hours.
print("Welcome to my Python Program!")
hours = input("How many hours did you exercise today?")
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number for hours.")
    exit() #it did this for me thats so cool

weekly_hours = hours * 7 
print(f"If you exercise {hours} hours daily, you will exercise {weekly_hours} hours in a week.")