```
def find_combinations(tuple_list):
    combinations = set()
    for i in range(len(tuple_list)):
        for j in range(i, len(tuple_list)):
            combinations.add(tuple(sorted([tuple_list[i][0] + tuple_list[j][0], tuple_list[i][1] + tuple_list[j][1]])))
    return list(combinations)
```
The function `find_combinations` takes a list of tuples as input and returns a list of tuples. Each tuple in the output list represents a combination of sums from the input list. The function iterates over all possible pairs of tuples in the input list, adds the corresponding values, and adds the resulting tuple to the set `combinations`. The `sorted` function is used to ensure that the tuples in the output list are in the correct order. The function finally returns the list of combinations.

The unit test `assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]` ensures that the function works correctly. It checks that the function returns the expected combinations of sums for the given input. If the function returns the correct combinations, the test passes; otherwise, it fails. This unit test helps to ensure that the function is working correctly for different input lists.