"""
Write a python function to find sum of products of all possible sublists of a given list. 
assert sum_Of_Subarray_Prod([1,2,3]) == 20
"""
# Time: O(n)
def sum_of_sublist_product(lst):
    prod = 0
    for i in lst:
        if len(i)>=2:
            prod += i[0]*i[1]
    
    return prod