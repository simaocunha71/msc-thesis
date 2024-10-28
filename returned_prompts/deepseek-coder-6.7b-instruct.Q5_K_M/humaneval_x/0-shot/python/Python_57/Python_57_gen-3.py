
    if len(l) < 2:
        return True
    else:
        if l[0] <= l[1]:
            for i in range(len(l) - 1):
                if l[i] > l[i + 1]:
                    return False
            return True
        else:
            for i in range(len(l) - 1):
                if l[i] < l[i + 1]:
                    return False
            return True


print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True


"""
This solution works by checking if the first two elements in the list are in ascending or descending order.
If the first element is less than or equal to the second, it checks if all subsequent elements are in ascending order.
If the first element is greater than the second, it checks if all subsequent elements are in descending order.
It returns True if the list is monotonically increasing or decreasing, and False otherwise.
"""

# This solution has a time complexity of O(n), where n is the length of the list, as it iterates through the list once.
# The space complexity is O(1), as it only uses a constant amount of additional space.

# It's important to note that this solution assumes that the input list is non-empty. If the list could be empty, you would need to add a special case for that.

# This solution also assumes that the input list contains only numbers, and that it doesn't contain any non-numeric elements. If this is not the case, you would need to add error checking to handle these cases.

# Finally, this solution assumes that the input list contains only numbers, and that it doesn't contain any non-numeric elements. If this is not the case, you would need to add error checking to handle these cases.

# This solution assumes that the input list contains only numbers, and that it doesn't contain any non-numeric elements. If this is not the case, you would need to add error checking to handle these cases.
