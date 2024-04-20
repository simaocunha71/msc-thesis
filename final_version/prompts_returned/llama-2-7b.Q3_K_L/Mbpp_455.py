"""
Write a function to check whether the given month number contains 31 days or not.
assert check_monthnumb_number(5)==True
"""

def check_monthnumb_number(month):
    if month<1 and month>12:
        return False;
    else:
        days=1+weekday(month,1);
        if (days-1)>30:
            return False;
        else:
            return True;
check_monthnumb_number(5)