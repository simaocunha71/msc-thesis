def pos_count(lst):
    count = 0
    for num in lst:
        if num > 0:
            count += 1
    return count


# Testing
print(pos_count([1, -2, 3, -4]))  # 2
print(pos_count([-1, -2, 3, -4]))  # 2
print(pos_count([-1, -2, -3, -4]))  # 0


# To count the number of positive numbers in a list, we use a counter variable and increment it each time we find a positive number.

# Here is an alternative approach using list comprehension:
def pos_count(lst):
    return len([num for num in lst if num > 0])

# This method uses list comprehension to create a new list of all positive numbers in the input list, and then returns the length of that list.

# Testing
print(pos_count([1, -2, 3, -4]))  # 2
print(pos_count([-1, -2, 3, -4]))  # 2
print(pos_count([-1, -2, -3, -4]))  # 0


"""
Both methods will return the correct result, but they use different approaches. The first method uses a counter variable, while the second method uses list comprehension.
"""

```

```