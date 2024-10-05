To solve this problem, we can compare each element with its adjacent element in the list. If the adjacent element is greater than the current element, it means the list is not sorted in ascending order. Also, if there are duplicate numbers in the list, it also means the list is not sorted in ascending order.

Here's how you can solve this problem in Python:

```python
def is_sorted(lst):
    # Check if the list has more than one duplicate number
    if len(lst) > len(set(lst)):
        return False

    # Compare each element with its adjacent element
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            return False

    return True
```

In this solution, we first check if the length of the list is greater than the length of the set of the list. If it is, it means the list has more than one duplicate number, and thus it is not sorted in ascending order.

Then, we iterate through the list starting from the second element (index 1). For each element, we compare it with its adjacent element (index i-1). If the adjacent element is greater than the current element, it means the list is not sorted in ascending order, and we return False.

If we reach the end of the loop without finding any out-of-order elements, it means the list is sorted in ascending order, and we return True.

You can use this `is_sorted` function to check if a list of numbers is sorted in ascending order without duplicate numbers.

For example, you can call the function like this:

```python
print(is_sorted([5]))  # True
print(is_sorted([1, 2, 3, 4, 5]))  # True
print(is_sorted([1, 3, 2, 4, 5]))  # False
print(is_sorted([1, 2, 3, 4, 5, 6]))  # True
print(is_sorted([1, 2, 3, 4, 5, 6, 7]))  # True
print(is_sorted([1, 