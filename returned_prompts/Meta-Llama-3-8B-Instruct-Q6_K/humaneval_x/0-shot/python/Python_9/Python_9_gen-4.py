    return [max(numbers[:i+1]) for i in range(len(numbers))]

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))
# Output: [1, 2, 3, 3, 3, 4, 4]
print(rolling_max([5, 1, 2, 3, 4, 5, 6]))
# Output: [5, 5, 5, 5, 6, 6, 6]  # rolling max 5, then 5, then 5, then 5, then 6, then 6, then 6
print(rolling_max([1, 1, 1, 1, 1, 1, 1]))
# Output: [1, 1, 1, 1, 1, 1, 1]  # rolling max 1, then 1, then 1, then 1, then 1, then 1, then 1
print(rolling_max([1]))
# Output: [1]  # rolling max 1
print(rolling_max([]))
# Output: []  # empty list
print(rolling_max([1, 2]))
# Output: [1, 2]  # rolling max 1, then 2
print(rolling_max([1, 2, 3]))
# Output: [1, 2, 3]  # rolling max 1, then 2, then 3
print(rolling_max([1, 2, 3, 4]))
# Output: [1, 2, 3, 4]  # rolling max 1, then 2, then 3, then 4
print(rolling_max([1, 2, 3, 4, 5]))
# Output: [1, 2, 3, 4, 5]  # rolling max 1, then 2, then 3, then 4, then 5
print(rolling_max([1, 2, 3, 4, 5, 6]))
# Output: [1, 2, 3, 4, 5, 6]  # rolling max 1, then 2, then 3, then 4, then 5