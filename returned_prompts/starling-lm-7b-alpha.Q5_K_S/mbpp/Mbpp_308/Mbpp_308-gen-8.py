"""
Here's a Python function that solves this problem:

```python
def large_product(list1, list2, n):
    """Returns the top n largest products of one element from each list.

    Arguments:
    list1 - a list of positive integers
    list2 - a list of positive integers
    n - an integer

    Returns:
    A list of the n largest products
    """
    # Sort both lists in descending order
    list1.sort(reverse=True)
    list2.sort(reverse=True)

    # Initialize the result list
    result = []

    # Generate the largest products
    for i in range(n):
        result.append(list1[i] * list2[i])

    # Return the result
    return result
```

You can test this function with the example provided in the problem:

```python
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
```
"""

def large_product(list1, list2, n):
    """Returns the top n largest products of one element from each list.

    Arguments:
    list1 - a list of positive integers
    list2 - a list of positive integers
    n - an integer

    Returns:
    A list of the n largest products
    """
    # Sort both lists in descending order
    list1.sort(reverse=True)
    list2.sort(reverse=True)

    # Initialize the result list
    result = []

    # Generate the largest products
    for i in range(n):
        result.append(list1[i] * list2[i])

    # Return the result
    return result

# Test the function
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
``