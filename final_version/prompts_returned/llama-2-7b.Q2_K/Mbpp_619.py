"""
Write a function to move all the numbers to the end of the given string.
assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
"""

def move_num(s):
    if s[-1] is not None:
        return s[:-1]+str(s[-1])+s[1:]
    else:
        return str(s[0])+str(s[1:])