
    if len(l) < 2:
        return True
    return all(l[i] <= l[i + 1] for i in range(len(l) - 1)) or all(l[i] >= l[i + 1] for i in range(len(l) - 1))


print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True


# This function works by iterating through the list and comparing each element to the next one. If all elements are less than or equal to the next one (indicating a monotonically increasing list) or all elements are greater than or equal to the next one (indicating a monotonically decreasing list), the function returns True. Otherwise, it returns False.

# If the list is empty or has only one element, the function will return True because such lists are considered to be monotonically increasing or decreasing.

# This solution has a time complexity of O(n) because it iterates through the list once.

# This solution has a space complexity of O(1) because it uses a constant amount of additional space to store the result and iterate through the list.
<jupyter_output>
<empty_output>
<jupyter_text>
