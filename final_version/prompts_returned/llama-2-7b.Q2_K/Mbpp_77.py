"""
Write a python function to find whether a number is divisible by 11.
assert is_Diff (12345) == False
"""

def is_Divisible(num):
    '''
      The code below will test if the Number is Divisible of 11
    :param num:
    :return: boolean value that indicates whether or not a number is divisible by eleven.
        - True: if integer divisible by eleven; False otherwise.
    '''
    if (num % 11) != 0:
        return False
    else:
        return True