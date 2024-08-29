def change_date_format(date):
    # split the date by '-'
    date_parts = date.split('-')
    # reverse the order of the parts
    date_parts = [date_parts[2], date_parts[1], date_parts[0]]
    # join the parts with '-' to get the desired format
    return '-'.join(date_parts)

# Test the function
assert change_date_format("2026-01-02") == '02-01-2026'


"""
