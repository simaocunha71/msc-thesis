Here's one way you can define the function:

```python
def sum_Of_Subarray_Prod(lst):
    # If list is empty, return 0
    if not lst:
        return 0
    # Otherwise, calculate the sum of products of all possible sublists
    else:
        # Initialize sum
        sum_ = 0
        # Iterate through the list, calculating the product of each sublist
        for i in range(len(lst)+1):
            product = 1
            for j in range(i, len(lst)):
                product *= lst[j]
                sum_ += product
        # Return the sum
        return sum_
```

This function works by using nested loops to generate all possible sublists of the input list. It then calculates the product of each sublist and adds it to a running total, which is ultimately returned.

To test the function, you can use the `assert` statement to check if the output matches the expected result for a given input. For example, `assert sum_Of_Subarray_Prod([1,2,3]) == 20` will raise an error if the function does not correctly calculate the sum of products of all possible sublists of the input list `[1,2,3]`.

It's worth noting that the time complexity of this function is O(n^3), where n is the length of the input list. This is because the function needs to generate all possible sublists, each of which involves selecting n elements from the original list.

```python
def sum_Of_Subarray_Prod(lst):
    if not lst:
        return 0
    else:
        sum_ = 0
        for i in range(len(lst)+1):
            product = 1
            for j in range(i, len(lst)):
                product *= lst[j]
                sum_ += product
        return sum_
```

You can use the `assert` statement to verify the correctness of the function. For example, `assert sum_Of_Subarray_Prod([1,2,3]) == 20` will raise an error if the function does not correctly calculate the sum of products of all