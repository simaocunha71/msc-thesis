


def sum_squares(lst):
    result = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            result += lst[i] ** 2
        elif i % 4 == 0:
            result += lst[i] ** 3
        else:
            result += lst[i]
    return result


print(sum_squares([1, 2, 3]))  # Output: 6
print(sum_squares([]))  # Output: 0
print(sum_squares([-1, -5, 2, -1, -5]))  # Output: -126


Explanation:

In this function, we iterate through each index of the list. We check if the index is a multiple of 3 or 4. If it is, we square or cube 
the number at that index (depending on the conditions) and add it to the result. If the index is not a multiple of 3 or 4, we just add the 
number at that index to the result. Finally, we return the result.

This solution works because it correctly handles all the given conditions. It squares numbers at indices that are multiples of 3 and cubes 
numbers at indices that are multiples of 4 but not multiples of 3. It leaves numbers at indices that are not multiples of 3 or 4 unchanged. 

It also correctly handles empty lists by returning 0.

It has a time complexity of O(n), where n is the length of the list, as it needs to iterate through each index of the list once. It has a 
space complexity of O(1), as it only uses a single variable to keep track of the result, regardless of the size of the list.
"""


def sum_squares(lst):
    result = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            result += lst[i] ** 2
        elif i % 4 == 0:
            result += lst[i] ** 3
        else:
            result += lst[i]
    return result


