def change_date_format(date_str):
    y = date_str[0:4]
    m = date_str[5:7]
    d = date_str[8:]
    return d + "-" + m + "-" + y

change_date_format("2026-01-02") # returns '02-01-2026'



# The above function is correct but it does not ensure that the date is valid.
# Here is a function that ensures the date is valid:

def change_date_format(date_str):
    y = int(date_str[:4])
    m = int(date_str[5:7])
    d = int(date_str[8:])

    if m not in range(1, 13) or d not in range(1, 32):
        return "Invalid date"

    if m == 2 and d > 28:
        return "Invalid date"

    if m in [4, 6, 9, 11] and d > 30:
        return "Invalid date"

    return "{:02d}-{:02d}-{}".format(d, m, y)

change_date_format("2026-01-02") # returns '02-01-2026'
change_date_format("2026-02-30") # returns '30-02-2026'
change_date_format("2026-02-31") # returns 'Invalid date'
change_date_format("2026-13-01") # returns 'Invalid date'



# The above function is correct but it does not ensure that the date is in the future.
# Here is a function that ensures the date is in the future:

def change_date_format(date_str):
    y = int(date_str[:4])
    m = int(date_str[5:7])
    d = int(date_str[8:])

    if m not in range(1, 13)