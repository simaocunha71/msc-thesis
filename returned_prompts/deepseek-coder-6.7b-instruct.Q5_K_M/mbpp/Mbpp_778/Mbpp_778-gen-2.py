def pack_consecutive_duplicates(lst):
    result = []
    temp = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            temp.append(lst[i])
        else:
            result.append(temp)
            temp = [lst[i]]
    result.append(temp)
    return result


print(pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]))

# Output: [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]

"""
This function works by iterating over the given list. If the current element is the same as the previous one, it is added to a temporary list. Otherwise, the temporary list is added to the result and a new temporary list is started. After the loop finishes, the last temporary list is added to the result.
"""

# Test Cases:
assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
assert pack_consecutive_duplicates([1, 1, 1, 2, 3, 3, 3, 4, 4, 4, 5, 6, 6, 7, 7, 7, 8, 8])==[[1, 1, 1], [2], [3, 3, 3], [4, 4, 4], [5], [6, 6], [7