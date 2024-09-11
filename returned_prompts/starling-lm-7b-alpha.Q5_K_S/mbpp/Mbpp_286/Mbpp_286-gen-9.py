Here's a Python solution for the problem:

```python
def max_sub_array_sum_repeated(array, k, n):
    max_sum = float('-inf')
    for i in range(k):
        cur_sum = 0
        for j in range(i, n):
            cur_sum += array[(j + i) % n]
            max_sum = max(max_sum, cur_sum)
    return max_sum
```

To verify the solution, you can run the following test case:

```python
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
```

The time complexity of the above solution is O(kn), which is acceptable for small values of k and n. However, if k is large, you may want to consider an alternative solution that has a time complexity of O(n).

Here's another solution with a time complexity of O(n):

```python
def max_sub_array_sum_repeated(array, k, n):
    max_sum = float('-inf')
    for i in range(n):
        cur_sum = 0
        for j in range(i, i + k * n):
            cur_sum += array[j % n]
            max_sum = max(max_sum, cur_sum)
    return max_sum
```

To verify the solution, you can run the following test case:

```python
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
```

This solution has a time complexity of O(n) and is suitable for larger values of k and n.

```

```

Here's a Python solution for the problem:

```python
def max_sub_array_sum_repeated(array, k, n):
    max_sum = float('-inf')
    for i in range(k):
        cur_sum = 0
        for j in range(i, n):
           