
def count_distinct_characters(string):
    """Given a string, find out how many distinct characters (regardless of case) does it consist of"""
    char_set = set()
    for char in string:
        char_set.add(char.lower())
    return len(char_set)

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected: 3
print(count_distinct_characters('Jerry'))  # Expected: 4
print(count_distinct_characters('aaaBBB'))  # Expected: 2


# Other Test Cases:
print(count_distinct_characters('abcdefghijklmnopqrstuvwxyz'))  # Expected: 26
print(count_distinct_characters('!@#$%^&*()_+-={}[]:";\'<>?,./|'))  # Expected: 22
print(count_distinct_characters('1234567890'))  # Expected: 10
print(count_distinct_characters('abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+-={}[]:";\'<>?,./|'))  # Expected: 42


# Time complexity: O(n), where n is the length of the input string.
# Space complexity: O(n)





# Here's a step-by-step breakdown of how the `count_distinct_characters` function works:

# Step 1: Initialize an empty set called `char_set`. This set will be used to store distinct characters from the input string.

# Step 2: Iterate over each character in the input string. For each character, add it to the set `char_set` after converting it to lowercase. This is done to ensure that characters are added to the set regardless of their case. For example, the character 'X' and 'x' are considered the same, so only one of them will be added to the set.

# Step 3: After