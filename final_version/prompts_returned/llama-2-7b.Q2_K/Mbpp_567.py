"""
Write a function to check whether a specified list is sorted or not.
assert issort_list([1,2,4,6,8,10,12,14,16,17])==True
"""

def issort(l):
    def helper(prev, v):
        if prev == None: # 1st element and not equal to any of previous elements
            return True
        else:
            return helper(prev, v) or (helper(None,v) is True)
    print("Sorted? ", issort_list([1,2,4,6,8,10]))
    return helper(None, l[::-1]) is True
