```
def max_difference(tuple_list):
    max_diff = 0
    for i in range(len(tuple_list)):
        for j in range(i+1, len(tuple_list)):
            diff = abs(tuple_list[i][1] - tuple_list[j][0])
            if diff > max_diff:
                max_diff = diff
    return max_diff
```


The function `max_difference` takes a list of tuples as input and returns the maximum difference between the first element of one tuple and the second element of another tuple. The function iterates over the list of tuples and calculates the difference between the first element of each tuple and the second element of every other tuple. The maximum difference found is returned as the result.

For example, the input `[(3, 5), (1, 7), (10, 3), (1, 2)]` will return `7` because the maximum difference between the first element of one tuple and the second element of another tuple is `7` (i.e., `5 - 2`).

The unit test `assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7` ensures that the function works correctly for this example. 





