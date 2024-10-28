```
def find_combinations(tuples):
    result = []
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            result.append((tuples[i][0] + tuples[j][0], tuples[i][1] + tuples[j][1]))
    return result
```


The problem is asking to find all combinations of sums of tuples in a given list of tuples. Each tuple in the list represents a pair of values. The function should return a list of new tuples, where each new tuple is the sum of the corresponding elements in the original tuples.

For example, if the input list is `[(2, 4), (6, 7), (5, 1), (6, 10)]`, the function should return `[(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]`.

The unit test `assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]` helps to clarify the problem.

The solution is a simple nested loop that iterates over the input list and combines each pair of tuples. The result is a list of new tuples, where each new tuple is the sum of the corresponding elements in the original tuples. The function returns this list of new tuples.