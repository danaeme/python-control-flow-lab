# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # Your control flow logic goes here
    month = input("Enter the month of the year (Jan-Dec): ")
    day = int(input("Enter the day of the month: "))

    if month in ["Jan", "Feb"] or (month == "Dec" and day >= 21) or (month == "Mar" and day <= 19):
        season = "Winter"
    elif month in ["Apr", "May"] or (month == "Mar" and day >= 20) or (month == "Jun" and day <= 20):
        season = "Spring"
    elif month in ["Jul", "Aug"] or (month == "Jun" and day >= 21) or (month == "Sep" and day <= 21):
        season = "Summer"
    elif month in ["Oct", "Nov"] or (month == "Sep" and day >= 22) or (month == "Dec" and day <= 20):
        season = "Fall"
    else:
        season = "Enter a valid date."
    
    print(f"{month} {day} is in {season}.")

# Call the function
determine_season()
