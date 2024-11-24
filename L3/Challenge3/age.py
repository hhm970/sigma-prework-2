from datetime import datetime, timedelta

# We get the user to input the days, month, and year
# for their desired date.
print("Days must have two digits.")
user_day = input("Enter day: ")
print("Months must have two digits.")
user_month = input("Enter month: ")
print("Years must have four digits.")
user_year = input("Enter year: ")
user_date = datetime.strptime(
    f"{user_day}-{user_month}-{user_year}", "%d-%m-%Y")
print(f"Your date is {user_date}.")

# We now wish to count the number of years between user_date
# and today's date.
# We set up a year counter, and user timedelta to add 365 days
# onto user_date, until it exceeds today's date.
year_counter = 0
now_date = datetime.now()
print(f"Today's date is {now_date}.")
year = timedelta(days=365)

# Note that this inequality accounts for days, hours, minutes,
# and seconds too!
# So therefore the year_counter must be deducted by 1 to
# account for this.
while user_date < now_date:
    user_date += year
    year_counter += 1
print(year_counter - 1)
