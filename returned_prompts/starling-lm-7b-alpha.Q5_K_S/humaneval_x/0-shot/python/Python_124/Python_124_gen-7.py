
def valid_date(date):
    #parse the date string
    date_list = date.split("-")
    month, day, year = date_list[0], date_list[1], date_list[2]
    #check if date is not empty
    if len(date) == 0:
        return False
    #check if number of days is valid
    if int(month) == 2:
        if int(day) > 29 or int(day) < 1:
            return False
    elif int(month) == 1 or int(month) == 3 or int(month) == 5 or int(month) == 7 or int(month) == 8 or int(month) == 10 or int(month) == 12:
        if int(day) > 31 or int(day) < 1:
            return False
    elif int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11:
        if int(day) > 30 or int(day) < 1:
            return False
    #check if month is valid
    if int(month) > 12 or int(month) < 1:
        return False
    #check if year is valid
    if int(year[0:4]) > int(year[4:]):
        return False
    #check if date is in the correct format
    if len(date) != 10 or date[2] != "-" or date[5] != "-":
        return False
    #if all conditions are satisfied, return True
    return True

#test
print(valid_date('03-11-2000')) # True
print(valid_date('15-01-2012')) # False
print(valid_date('04-0-2040')) # False
print(valid_date('06-04-2020')) # True
print(valid_date('06/04/2020')) # False

#test with invalid month
print(valid_date('13-03-20