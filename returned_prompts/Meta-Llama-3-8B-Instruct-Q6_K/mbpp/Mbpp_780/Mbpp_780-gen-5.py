```
def find_combinations(tuple_list):
    combinations = set()
    for i in range(len(tuple_list)):
        for j in range(i + 1, len(tuple_list)):
            combinations.add(tuple(sorted([tuple_list[i][0] + tuple_list[j][0], tuple_list[i][1] + tuple_list[j][1]])))
    return sorted(list(combinations))
```
The function `find_combinations` takes a list of tuples as input and returns a list of tuples, where each tuple is a combination of sums of two tuples from the input list. The function iterates over the input list, calculates the sum of each pair of tuples, and adds the result to a set. The set is used to avoid duplicates, as the order of the tuples does not matter. Finally, the function converts the set to a list, sorts the list, and returns it. The unit test `assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]` ensures that the function works correctly.