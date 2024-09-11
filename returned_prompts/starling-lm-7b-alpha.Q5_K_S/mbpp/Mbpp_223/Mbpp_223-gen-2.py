Here's a Python solution that uses a binary search algorithm to find the majority element:

```python
def is_majority(arr, n, element):
    left = 0
    right = n - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] == element:
            break
        elif arr[mid] < element:
            left = mid + 1
        else:
            right = mid - 1

    count = 0

    for i in range(left, n):
        if arr[i] == element:
            count += 1

    return count > n // 2
```

This function starts by initializing two pointers, `left` and `right`, to the start and end of the array, respectively. It then enters a while loop that continues until the two pointers cross each other. Inside the loop, it calculates the midpoint index using integer division and compares the element at the midpoint index with the target element. If they are equal, it breaks out of the loop. If the element at the midpoint index is less than the target element, it updates the `left` pointer to be midpoint index plus one. If the element at the midpoint index is greater than the target element, it updates the `right` pointer to be midpoint index minus one. This binary search algorithm narrows down the range of indices where the target element might be found.

Once the binary search is complete, the function initializes a count variable to keep track of how many times the target element appears in the narrowed down range. It then iterates through the range using a for loop and increments the count variable each time the target element is found.

Finally, the function returns whether the count is greater than `n` divided by 2. If it is, the target element is the majority element in the given sorted array. Otherwise, it is not.

You can test the function using the provided `assert` statement:

```python
assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
```

This assertion will pass if the function correctly identifies that the element 3 is