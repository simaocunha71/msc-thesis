
def valid_date(date):
    # check if the date string is not empty
    if not date:
        return False
    # split the date string
    date_list = date.split('-')
    # check if the date string is in the format: mm-dd-yyyy
    if len(date_list) != 3:
        return False
    # convert the date string to integer
    month, day, year = map(int, date_list)
    # check if the number of days is valid
    if (month == 2 and day > 29) or (month in [1,3,5,7,8,10,12] and day > 31) or (month in [4,6,9,11] and day > 30):
        return False
    # check if the month is valid
    if month < 1 or month > 12:
        return False
    # check if the year is valid
    if year < 0:
        return False

    return True



# test cases
print(valid_date('03-11-2000')) # True
print(valid_date('15-01-2012')) # False
print(valid_date('04-0-2040')) # False
print(valid_date('06-04-2020')) # True
print(valid_date('06/04/2020')) # False


# To solve this problem, you can follow these steps:

# Step 1: Check if the date string is not empty. If it is empty, return False.
# Step 2: Split the date string by '-' to get the month, day, and year. Convert them to integers.
# Step 3: Check if the number of days is valid for the given month and year. If not, return False.
# Step 4: Check if the month is valid (1 to 12). If not, return False.
# Step 5: Check if the year is valid (non-negative). If not, return False.
# Step 6: If all the above conditions are satisfied, return True.



