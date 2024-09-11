def issort_list(list_var):
    list_var.sort()
    if list_var==sorted(list_var):
        return True
    else:
        return False

# assert issort_list([1,2,4,6,8,10,12,14,16,17])==True

# assert issort_list([2,1,4,6,8,10,12,14,16,17])==False

"""
In the above program, we first sort the list and then check whether the list is sorted or not. If the original
list and the sorted list are same, then the list is sorted. Otherwise, the list is not sorted.
"""

# The time complexity of the above program is O(n log(n)) and the space complexity is O(1).

# Here, n is the length of the list.

# The time complexity is due to the sorting of the list which takes O(n log(n)) time.

# The space complexity is constant as no extra space is used in the program.


# Here is an alternative method to check whether a list is sorted or not.

def issort_list(list_var):
    for i in range(len(list_var)-1):
        if list_var[i]>list_var[i+1]:
            return False
    return True

# assert issort_list([1,2,4,6,8,10,12,14,16,17])==True

# assert issort_list([2,1,4,6,8,10,12,14,16,17])==False

"""
In the above program, we iterate through the list and check whether the current element is greater than the next
element. If we find any such case, then the list is not sorted. Otherwise, the list is sorted.
"""

# The time complexity of the above program is O(n) and the space complexity is O(1).

# Here, n is the length of the list.

# The time complexity is due to the iteration through the list which takes O(n) time.

# The