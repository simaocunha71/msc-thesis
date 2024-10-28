
def valid_date(date):
    # convert date to list of integers
    date_list = list(map(int,date.split('-')))
    # check if the date is not empty
    if len(date_list) != 3:
        return False
    # check if the month is between 1 and 12
    if date_list[0] < 1 or date_list[0] > 12:
        return False
    # check if the day is between 1 and 31 for months 1,3,5,7,8,10,12
    if (date_list[0] == 1 or date_list[0] == 3 or date_list[0] == 5 or date_list[0] == 7 or date_list[0] == 8 or date_list[0] == 10 or date_list[0] == 12):
        if (date_list[1] < 1 or date_list[1] > 31):
            return False
    # check if the day is between 1 and 30 for months 4,6,9,11
    elif (date_list[0] == 4 or date_list[0] == 6 or date_list[0] == 9 or date_list[0] == 11):
        if (date_list[1] < 1 or date_list[1] > 30):
            return False
    # check if the day is between 1 and 29 for the month 2
    elif (date_list[0] == 2):
        if (date_list[1] < 1 or date_list[1] > 29):
            return False
    # check if the year is between 0000 and 9999
    if (date_list[2] < 0 or date_list[2] > 9999):
        return False
    # return true if all conditions are satisfied
    return True


# Test
print(valid_date('03-11-2000'))  # True
print(valid_date('15-01-