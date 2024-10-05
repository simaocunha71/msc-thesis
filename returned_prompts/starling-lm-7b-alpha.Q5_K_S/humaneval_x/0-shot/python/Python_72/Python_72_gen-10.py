# Here's a possible solution:
def will_it_fly(q,w):
    if len(q) == 0:
        return True
    if q[0] > q[-1]:
        return False
    if sum(q) > w:
        return False
    return will_it_fly(q[1:-1], w - q[0])

# This is a recursive solution. We check the first and last element of the list. If they're not the same, the list is unbalanced and will not fly. If they are the same, we remove the first and last element and check the rest of the list. We continue this process until the list is empty, in which case the object will fly, or until we reach the maximum weight, in which case the object will not fly.

# To check if a list is palindromic, we compare the first and last elements. If they're not the same, the list is not palindromic. If they are the same, we remove the first and last element and check the rest of the list. We continue this process until the list is empty, in which case the list is palindromic.

# The maximum possible weight is the sum of all the elements in the list.

```python
def will_it_fly(q, w):
    # Check if the list is empty
    if len(q) == 0:
        return True
    # Check if the first element is greater than the last element
    if q[0] > q[-1]:
        return False
    # Check if the sum of the elements is greater than the maximum possible weight
    if sum(q) > w:
        return False
    # Recursively call the function with the remaining elements and the weight minus the first element
    return will_it_fly(q[1:-1], w - q[0])
```

This function will return True if the object will fly, and False otherwise.

# Here are some test cases:

print(will_it_fly([1, 2], 5))  # False
print(will_it_fly([3, 2, 3], 1))  # False
print(will_it_fly([3, 2,