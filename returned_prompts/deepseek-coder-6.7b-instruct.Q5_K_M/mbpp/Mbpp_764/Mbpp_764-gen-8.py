
def number_ctr(s):
    return sum(c.isdigit() for c in s)

assert number_ctr('program2bedone') == 1

# The function works by iterating over each character in the string and checking if it's a digit using the isdigit method. If it is, it adds 1 to a running total. Finally, it returns the total count of digits.

"""
