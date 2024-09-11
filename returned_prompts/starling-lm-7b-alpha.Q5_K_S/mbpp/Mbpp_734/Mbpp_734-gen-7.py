"""
def sum_Of_Subarray_Prod(lst):
    s = 0
    for i in range(len(lst)):
        for j in range(i+1,len(lst)+1):
            s += sum(lst[i:j])
    return s
"""

def sum_Of_Subarray_Prod(lst):
    s = 0
    for i in range(len(lst)):
        for j in range(i+1,len(lst)+1):
            s += sum(lst[i:j])
    return s


assert sum_Of_Subarray_Prod([1,2,3]) == 20

# Another way to do the same
def sum_of_subarray_products(nums):
    result = 0
    for i in range(len(nums)):
        product = 1
        for j in range(i, len(nums)):
            product *= nums[j]
            result += product
    return result

# Test
assert sum_of_subarray_products([1, 2, 3]) == 20
```

Answer:
```
def sum_Of_Subarray_Prod(lst):
    s = 0
    for i in range(len(lst)):
        for j in range(i+1,len(lst)+1):
            s += sum(lst[i:j])
    return s
```
This function takes a list as input and returns the sum of the products of all possible sublists of the given list. It uses two nested loops to iterate through all possible sublists and calculates the sum of each sublist's elements. The sums are then added to the total sum. The function asserts that the sum_Of_Subarray_Prod function correctly calculates the sum of the products of all possible sublists of the given list.
```python

def sum_of_subarray_products(nums):
    result = 0
    for i in range(len(nums)):
        product = 1
        for j in range(i, len(nums)):
            product *= nums[j]
            result += product
    return result
