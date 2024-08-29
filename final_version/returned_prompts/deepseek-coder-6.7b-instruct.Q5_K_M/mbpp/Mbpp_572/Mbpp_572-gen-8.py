def two_unique_nums(lst):
    return list(set(lst))

print(two_unique_nums([1,2,3,2,3,4,5]))

# Output: [1, 2, 3, 4, 5]

# The above function works by converting the input list to a set. A set in Python is a collection type that is unordered, mutable, and has no duplicate elements.
# The list() function is then used to convert the set back to a list, effectively removing any duplicate elements.


