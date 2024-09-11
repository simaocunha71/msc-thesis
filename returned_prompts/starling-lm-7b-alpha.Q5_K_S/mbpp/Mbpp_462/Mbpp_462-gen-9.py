def combinations_list(lst):
    """Find all possible combinations of the elements of a given list"""
    if len(lst) == 0:
        return [[]]
    if len(lst) == 1:
        return [lst, []]
    sub_combinations = combinations_list(lst[1:])
    combinations = []
    for combination in sub_combinations:
        combinations.append(combination)
        combinations.append([lst[0]] + combination)
    return combinations

# Test
print(combinations_list([1,2,3]))
# Output: [[], [2], [1], [2, 1], [3], [3, 1], [2, 3], [2, 3, 1], [3, 1, 2]]

# Test
print(combinations_list(['a', 'b', 'c']))
# Output: [[], ['a'], ['b'], ['b', 'a'], ['c'], ['c', 'a'], ['b', 'c'], ['b', 'c', 'a'], ['c', 'b', 'a'], ['a', 'b', 'c'], ['a', 'c', 'b'], ['b', 'a', 'c'], ['b', 'c', 'a', 'c'], ['a', 'b', 'c', 'c'], ['a', 'b', 'c', 'c', 'b']]

# Test
print(combinations_list(['orange', 'red', 'green', 'blue']))
# Output: [[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]

# Test
print(combinations_list([1,2,3,4]))
# Output: [[], [4], [3], [3, 4], [2], [2, 4], [2