"""
To check whether a specified list is sorted or not, you can follow this approach:

1. Initialize a boolean variable, `result`, to False. This variable will be used to store whether the list is sorted or not.
2. Loop through the list from the second element to the end using the `range` function along with `len` function.
3. In each iteration, compare the current element with the next element. If the current element is greater than the next element, set the `result` variable to True and break out of the loop. If the condition is not met, continue to the next iteration.
4. After the loop, check the value of the `result` variable. If it is True, the list is not sorted; otherwise, it is sorted.
5. Return the value of the `result` variable.

Here's an example implementation of the solution in Python:

```python
def issort_list(lst):
    result = False
    for i in range(1, len(lst)):
        if lst[i-1] > lst[i]:
            result = True
            break
    return result
```

You can use the `assert` statement to verify the correctness of the function. In this case, we are asserting that the `issort_list` function returns True when the input list `[1,2,4,6,8,10,12,14,16,17]` is passed as an argument.
"""

def issort_list(lst):
    result = False
    for i in range(1, len(lst)):
        if lst[i-1] > lst[i]:
            result = True
            break
    return result

assert issort_list([1,2,4,6,8,10,12,14,16,17]) == True

# You can add more assertions to test the function with different input lists and expected outputs.
```

```python
# Here are some additional assertions to test the function with different input lists and expected outputs:

assert issort_list([1, 2, 3]) == True
assert issort_list([3, 2, 1]) == False
assert iss