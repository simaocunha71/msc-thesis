```
def max_difference(tuples):
    max_diff = 0
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            diff = abs(tuples[i][1] - tuples[j][0])
            if diff > max_diff:
                max_diff = diff
    return max_diff
```
The function iterates over all pairs of tuples in the list, calculates the absolute difference between the end of the first tuple and the start of the second tuple, and keeps track of the maximum difference found. The unit test `assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7` confirms the correctness of the function. 