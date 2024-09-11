"""
def odd_position(input_list):
    for index, item in enumerate(input_list):
        if index % 2 == 0 and item % 2 != 0:
            return False
    return True
"""

def odd_position(input_list):
    for index, item in enumerate(input_list):
        if index % 2 == 0 and item % 2 == 0:
            return False
    return True

# assert odd_position([2,1,4,3,6,7,6,3]) == True

def odd_position(input_list):
    for index, item in enumerate(input_list):
        if index % 2 == 0 and item % 2 != 1:
            return False
    return True

# assert odd_position([2,1,4,3,6,7,6,3]) == True

def odd_position(input_list):
    for index, item in enumerate(input_list):
        if index % 2 == 0 and item % 2 != 0:
            return False
    return True

# assert odd_position([2,1,4,3,6,7,6,3]) == True

def odd_position(input_list):
    for index, item in enumerate(input_list):
        if index % 2 == 0 and item % 2 != 1:
            return False
    return True

# assert odd_position([2,1,4,3,6,7,6,3]) == True

def odd_position(input_list):
    for index, item in enumerate(input_list):
        if index % 2 != 0 and item % 2 != 0:
            return False
    return True

# assert odd_position([2,1,4,3,6,7,6,3]) == True

def odd_position(input_list):
    for index, item in enumerate(input_list):
        if index % 2 != 0 and item % 2 != 1:
            return False
    return True

# assert odd_position([2,1,4,3,