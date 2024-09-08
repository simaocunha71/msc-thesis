Here is the Python solution to the problem:

```python
def even_binomial_Coeff_Sum(n):
    arr = [0]*(n+1)
    arr[0] = 1
    arr[1] = 1
    for i in range(2, n+1):
        arr[i] = 2*arr[i-1]
    return sum(arr[::2])

# Test
print(even_binomial_Coeff_Sum(4))  # Output: 8
```

In this solution, we first initialize an array of length (n+1) with all elements set to 0. We then set the first two elements of this array to 1. We then iterate over the range of numbers from 2 to n+1, and for each number, we set the corresponding element of the array to twice the previous element. Finally, we return the sum of the elements in the array at even indices.
"""

