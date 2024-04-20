"""
Write a python function takes in an integer and check whether the frequency of each digit in the integer is less than or equal to the digit itself.
assert validate(1234) == True
"""

def validate(n):
    if n < 10:   #check if the number is less then 10, if its true break the loop and assign True as a return value.
        break
    else:
        n = n % 10
    while n > 1:      #break each digit of the integer and check whether it is less than or equal to that specific digit of the integer.
        n, remainder = divmod(n, str(n))   #divide the number by ten and assign it to the variable n in a string form, then convert it back to int type.
    return True if remainder < 10 else False