"""
Write a python function to check whether the given list contains consecutive numbers or not.
assert check_Consecutive([1,2,3,4,5]) == True
"""

def check_Consecutive(arr):
    if arr == []:  # Empty List
        return False
    else :
        n = [i for i in range(len(arr) - 1)]
        n.append(arr[0])
        if any(n.count(i) != 2 for i in range (len(arr))) == True:
            return True
        else:
            return False