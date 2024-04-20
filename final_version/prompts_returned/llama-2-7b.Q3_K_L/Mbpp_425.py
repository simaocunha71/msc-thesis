"""
Write a function to count the number of sublists containing a particular element.
assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
"""

def count_element_in_list(l, elem):
    # base case here
    if len(l) == 0:
        return
    
    # write your function here.
    for e in l:
        if elem in e:
            return True
        else:
            count = count_element_in_list(e,elem)
            print(count, 'counted: ', elem)
            return 1 + count