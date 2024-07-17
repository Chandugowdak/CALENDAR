import calendar  # IMPORTING CALENDAR MODULE TO WORK WITH DATES

# FUNCTION TO GET USER INPUT AND DISPLAY THE CALENDAR FOR A SPECIFIED MONTH AND YEAR
def display_month_calendar():
    n = int(input("Enter the Year You Want: "))  # GET YEAR FROM USER
    m = int(input("Enter the Month You Want: "))  # GET MONTH FROM USER

    # CHECKING IF THE INPUT YEAR AND MONTH ARE VALID
    if m < 1 or m > 12:
        print("Invalid month! Please enter a value between 1 and 12.")
    else:
        # PRINTING THE CALENDAR FOR THE SPECIFIED MONTH AND YEAR
        print(calendar.month(n, m))
        
        # PRINTING ADDITIONAL INFORMATION
        print("\nAdditional Information:")
        print(f"Year: {n}, Month: {calendar.month_name[m]}")
        print(f"Number of days in the month: {calendar.monthrange(n, m)[1]}")
        print(f"First day of the month: {calendar.day_name[calendar.monthrange(n, m)[0]]}")

# CALLING THE FUNCTION TO EXECUTE THE PROGRAM
display_month_calendar()
