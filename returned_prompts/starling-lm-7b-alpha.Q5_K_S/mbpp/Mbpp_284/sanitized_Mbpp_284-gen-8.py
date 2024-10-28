import sys
def check_element(lst, elem):
    for item in lst:
        if item != elem:
            return False
    return True