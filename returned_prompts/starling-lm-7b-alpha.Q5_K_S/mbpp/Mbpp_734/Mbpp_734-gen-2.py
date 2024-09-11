"""
def sum_Of_Subarray_Prod(lst):
    res = 0
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            prod = 1
            for k in range(i, j+1):
                prod *= lst[k]
            res += prod
    return res

def test_sum_Of_Subarray_Prod():
    assert sum_Of_Subarray_Prod([1,2,3]) == 20

test_sum_Of_Subarray_Prod()
"""

def sum_Of_Subarray_Prod(lst):
    res = 0
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            prod = 1
            for k in range(i, j+1):
                prod *= lst[k]
            res += prod
    return res

def test_sum_Of_Subarray_Prod():
    assert sum_Of_Subarray_Prod([1,2,3]) == 20

test_sum_Of_Subarray_Prod()


```
Here's the Python code to solve this problem:

The function `sum_Of_Subarray_Prod` takes a list as input and returns the sum of the products of all possible sublists of that list. It uses two nested loops to iterate through all possible sublists, and another loop to calculate the product of each sublist's elements. The product is added to the `res` variable, which holds the sum of all sublist products.

The `test_sum_Of_Subarray_Prod` function is used to test the correctness of the `sum_Of_Subarray_Prod` function. It calls `sum_Of_Subarray_Prod` with the input `[1,2,3]` and asserts that the result is equal to `20`.

When you run the program, the `test_sum_Of_Subarray_Prod` function will be executed, and if the assertion is true, it means that the `sum_Of_Subarray_Prod` function is working correctly.

Note that this