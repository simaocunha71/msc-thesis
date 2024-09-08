This problem can be solved using the itertools.combinations function to generate all possible pairs of numbers. Then, we can use the map function to sum up each pair. The final result is a list of tuples, where each tuple is a pair of numbers that can be obtained by summing up two numbers in the original tuples.

Here is the Python code that implements this solution:

```python
from itertools import combinations

def find_combinations(tuples_list):
    result = []
    for i in range(2, len(tuples_list)+1):
        for comb in combinations(tuples_list, i):
            result.append(tuple(map(sum, zip(*comb))))
    return result
```

This function first generates all combinations of pairs of tuples of length 2 to the length of the input list. For each combination, it calculates the sum of the numbers in each tuple and adds the result to the result list. The final result is a list of tuples, where each tuple is a pair of numbers that can be obtained by summing up two numbers in the original tuples.

Please note that this function assumes that all tuples in the input list have exactly two numbers. If this is not the case, you may need to modify the function to handle different lengths of tuples.

Also, please note that the order of the numbers in the tuples does not matter when calculating the sum, so (2, 4) and (4, 2) would be considered the same when calculating the sum. If you want to consider the order of the numbers in the tuples when calculating the sum, you would need to modify the function to use the permutations function instead of the combinations function.
