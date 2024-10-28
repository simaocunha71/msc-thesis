
# Define the is_sorted function
def is_sorted(lst):
    # Check if the length of the list is less than 2
    if len(lst) < 2:
        return True
    # Compare the first two elements of the list
    if lst[0] > lst[1]:
        return False
    # Iterate over the list starting from the second element
    for i in range(len(lst)-1):
        # Compare the current element with the next one
        if lst[i] > lst[i+1]:
            return False
    # If all comparisons are successful, the list is sorted and unique
    return True

# Test the function
print(is_sorted([5]))  # True
print(is_sorted([1, 2, 3, 4, 5]))  # True
print(is_sorted([1, 3, 2, 4, 5]))  # False
print(is_sorted([1, 2, 3, 4, 5, 6]))  # True
print(is_sorted([1, 2, 3, 4, 5, 6, 7]))  # True
print(is_sorted([1, 3, 2, 4, 5, 6, 7]))  # False
print(is_sorted([1, 2, 2, 3, 3, 4]))  # True
print(is_sorted([1, 2, 2, 2, 3, 4]))  # False



# Here's a possible solution to the problem:

# We define a function called `is_sorted` that takes a list as input.
# Inside the function, we first check if the length of the list is less than 2. If it is, it means that the list is either empty or contains only one element, which is automatically sorted, so we can return `True`.

# If the length of the list is not less than 2, we proceed to compare the first two elements of the list. If the first element is greater than the second element, it means that the list is not sorted, so we return `False`.