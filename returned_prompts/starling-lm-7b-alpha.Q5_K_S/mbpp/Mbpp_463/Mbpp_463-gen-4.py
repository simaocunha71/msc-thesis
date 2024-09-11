"""
The maximum product of a subarray is the maximum product of all the numbers in the subarray.

Here's a function to find the maximum product subarray of an array:

```python
def max_subarray_product(arr):
    max_product = float('-inf')
    curr_product = 1
    for num in arr:
        curr_product *= num
        max_product = max(max_product, curr_product)
        if curr_product < 1:
            curr_product = 1
    return max_product
```

The function works by iterating through the array, keeping track of the maximum product of the subarray seen so far, as well as the product of all the numbers seen so far. At each step, it updates the maximum product and resets the product to 1 if it becomes less than 1 (since a negative number multiplied by a positive number becomes negative, and the product of two negative numbers is a positive number)."""


# Python3 program to find maximum product of a subarray

def maxProductSubarray(arr, n):
    max_product = float('-inf')
    curr_product = 1
    for i in range(n):
        curr_product *= arr[i]
        max_product = max(max_product, curr_product)
        if curr_product < 1:
            curr_product = 1
    return max_product

# Driver program to test the above function
arr = [1, -2, -3, 0, 7, -8, -2]
n = len(arr)
print(maxProductSubarray(arr, n))

# This code is contributed by PrinciRaj1
# 

```python
"""

Here's a test of the function:

```python
def test_max_subarray_product():
    assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
    assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
    assert max_subarray_product([1])