"""
def odd_position(list):
    if len(list) % 2 != 0:
        return False
    for i in range(0,len(list)-1,2):
        if list[i] % 2 != 0:
            return False
    return True

assert odd_position([2,1,4,3,6,7,6,3]) == True
"""

