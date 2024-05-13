"""
Write a function to find the shared elements from the given two lists.
assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
"""
import collections

def similar_elements(l1, l2):
    '''
       Write a function to find the shared elements from given two lists.
       Args:
        l1 (List[int]): First list of elements.
        l2 (List[int]): Second list of elements.
       Return Value:
        Set [element]: A set object that contains all the common elements between both lists.
    '''

    result = set()

    for num in l1:
        if num not in l2 and num not in result:
            result.add(num)

    return result