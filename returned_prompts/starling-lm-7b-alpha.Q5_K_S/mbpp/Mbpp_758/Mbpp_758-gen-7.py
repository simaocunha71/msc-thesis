def unique_sublists(lst):
    lst = sorted(lst)
    return {frozenset(lst[i:j]): j - i for i, j in zip(range(len(lst)), lst[1:])}

unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]])

"""
The function first sorts the list to ensure that the same list does not appear twice with different indices. Then, for each index in the sorted list, it creates a set of the sublist from that index to the next index, and counts the number of indices that this sublist appears. The result is a dictionary where the keys are the sublists, and the values are the number of times the sublist appears in the original list.
"""


def unique_sublists(lst):
    lst.sort()
    result = {}
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist = tuple(lst[i:j])
            if sublist not in result:
                result[sublist] = 0
            result[sublist] += 1
    return result

unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]])

# Time complexity: O(n^2)
# Space complexity: O(n^2)


def unique_sublists(lst):
    lst.sort()
    result = {}
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist = tuple(lst[i:j])
            if sublist not in result:
                result[sublist] = 0
            result[sublist] += 1
    return result

unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17],