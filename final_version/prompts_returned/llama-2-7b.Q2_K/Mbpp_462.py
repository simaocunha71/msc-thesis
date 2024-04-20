"""
Write a function to find all possible combinations of the elements of a given list.
assert combinations_list(['orange', 'red', 'green', 'blue'])==[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]
"""

def combination(nums):
    n = len(nums)

    if n == 1:
        return [[x]]
    
    size = pow(2, n - 1)
    set = [set() for _ in range(size)]

    for x in nums:
        idx = set.index(set([x]))

        if idx == len(set):
            set.append([x])
            break
        
        else:
            set[idx] |= set([x])

    return [list(i) for i in set]