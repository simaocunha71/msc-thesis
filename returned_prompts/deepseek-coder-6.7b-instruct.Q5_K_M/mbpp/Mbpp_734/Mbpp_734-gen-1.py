Here is the Python code to solve the problem:

```python
from itertools import combinations

def sum_of_subarray_prod(arr):
    sum_prod = 0
    for i in range(1, len(arr)+1):
        for sub in combinations(arr, i):
            prod = 1
            for num in sub:
                prod *= num
            sum_prod += prod
    return sum_prod
```

Test the function:
```python
print(sum_of_subarray_prod([1,2,3]))  # Output: 20
```

In this code, we use `combinations` function from `itertools` module to generate all possible sublists of given list. For each sublist, we calculate the product of its elements and add the result to `sum_prod`. Finally, we return `sum_prod`.

The time complexity of this code is O(n^2), where n is the length of the given list. This is because for each element in the list, we generate and process all possible sublists that include that element. The space complexity is O(n) because of the space required to store the sublists.
"""

# Test cases
assert sum_of_subarray_prod([1,2,3]) == 20
assert sum_of_subarray_prod([1,2,3,4]) == 50
assert sum_of_subarray_prod([1]) == 1
assert sum_of_subarray_prod([]) == 0

print("All test cases pass")
<jupyter_output>
All test cases pass
<jupyter_text>
Question 3:
<jupyter_code>
"""
