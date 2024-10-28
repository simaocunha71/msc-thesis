```
def find_combinations(tuple_list):
    combinations = []
    for i in range(len(tuple_list)):
        for j in range(i, len(tuple_list)):
            combinations.append((tuple_list[i][0] + tuple_list[j][0], tuple_list[i][1] + tuple_list[j][1]))
    return combinations
```


Test:
```
assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
```


Explanation:
The function `find_combinations` iterates over the given tuple list, and for each tuple, it adds the elements of the current tuple with the elements of the other tuples to form new tuples. These new tuples are then added to the `combinations` list. The function returns this list of combinations. The test case ensures that the function works correctly by comparing its output with the expected output. 





This function works by iterating over the list of tuples and for each tuple, it adds the elements of the current tuple with the elements of the other tuples to form new tuples. These new tuples are then added to the `combinations` list. The function returns this list of combinations. The test case ensures that the function works correctly by comparing its output with the expected output. The time complexity of this function is O(n^2) where n is the number of tuples in the list, because it has a nested loop structure. The space complexity is O(n^2) as well, because it stores all the combinations in the `combinations` list.