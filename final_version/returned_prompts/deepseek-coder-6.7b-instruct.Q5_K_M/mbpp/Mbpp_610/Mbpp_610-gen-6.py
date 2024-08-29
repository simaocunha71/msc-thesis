
def remove_kth_element(lst, k):
    del lst[k]
    return lst

print(remove_kth_element([1,1,2,3,4,4,5,1],3))

# Output: [1, 1, 2, 3, 4, 4, 5, 1]

# Alternatively, you can use the pop method as well:

def remove_kth_element(lst, k):
    lst.pop(k)
    return lst

print(remove_kth_element([1,1,2,3,4,4,5,1],3))

# Output: [1, 1, 2, 3, 4, 4, 5, 1]

"""
Both of these functions will work for any list and any integer k where k is the index of the element that you want to remove.
"""

