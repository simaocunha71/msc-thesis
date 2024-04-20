"""
Write a function that takes in two lists and replaces the last element of the first list with the elements of the second list.
assert replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8])==[1, 3, 5, 7, 9, 2, 4, 6, 8]
"""
def replace_list(l1, l2):
    assert len(l2)<len(l1), 'The second list should be less than the first'
    result = []
    
    for i in range(0, len(l1)-1):
        if i == len(l2)-1:
            pass
        else:  # We have an equal length list
            result.append(l1[i])
        else:   # Add the element of l2 at index i
            l2 = [l2[0]] + [x for x in l2]
            break
    return result
