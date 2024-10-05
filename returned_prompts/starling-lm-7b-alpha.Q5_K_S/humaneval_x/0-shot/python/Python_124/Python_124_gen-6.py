    import re

    def valid_date(date):
        # Check if the date string is not empty
        if not date:
            return False
        # Check if the date string is in the format mm-dd-yyyy
        if not re.match("^[0-9]{2}-[0-9]{2}-[0-9]{4}$", date):
            return False
        # Convert the date string to a list of integers
        date_list = [int(i) for i in date.split("-")]

        # Check if the months are within the range 1 to 12
        if not 1 <= date_list[0] <= 12:
            return False

        # Check if the number of days is within the range for the given month
        if date_list[0] == 2 and date_list[1] > 29:
            return False
        elif date_list[0] in [1, 3, 5, 7, 8, 10, 12] and date_list[1] > 31:
            return False
        elif date_list[0] in [4, 6, 9, 11] and date_list[1] > 30:
            return False

        # If all checks pass, the date is valid
        return True

# Test the function
print(valid_date('03-11-2000'))  # Should return True
print(valid_date('15-01-2012'))  # Should return False
print(valid_date('04-0-2040'))  # Should return False
print(valid_date('06-04-2020'))  # Should return True
print(valid_date('06/04/2020'))  # Should return False





# Here's a step-by-step explanation of how the solution works:

# First, we define the function valid_date that takes a date string as input.

# Inside the function, we check if the date string is not empty using the condition if not date. We return False if this is the case, as the date is not