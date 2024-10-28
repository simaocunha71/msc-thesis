
def count_distinct_characters(string):
    return len(set(string))


# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected: 3
print(count_distinct_characters('Jerry'))  # Expected: 4
print(count_distinct_characters('Hello, World!'))  # Expected: 10



# Time Complexity: O(n), where n is the length of the string. This is because we're iterating through the string exactly once to create the set.
# Space Complexity: O(k), where k is the number of unique characters in the string. This is because the set will only store unique characters.


# In Python, the set() function returns an unordered collection of unique elements. Since a set cannot contain duplicate values, the length of the set will always be the number of unique items in the set.

# The time complexity of the set() function is O(n), where n is the size of the iterable. This is because the function needs to iterate through the entire iterable to ensure that no duplicate values are added to the set.

# The space complexity of the set() function is also O(n), where n is the size of the iterable. This is because the function needs to store each unique value in the set, which requires additional memory.










```

```