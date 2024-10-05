

def count_distinct_characters(string: str) -> int:
    string = string.lower()
    distinct_characters = set(string)
    return len(distinct_characters)

print(count_distinct_characters('xyzXYZ'))
print(count_distinct_characters('Jerry'))


# 1st test case: 'xyzXYZ' 
# Lowercasing the string we get 'xyzxyz'.
# Creating a set from it will remove duplicates and we'll end up with {'x', 'y', 'z'}
# The length of this set is 3, so the function returns 3.

# 2nd test case: 'Jerry'
# Lowercasing the string we get 'jerry'.
# Creating a set from it will remove duplicates and we'll end up with {'j', 'e', 'r', 'y'}
# The length of this set is 4, so the function returns 4.


# This code takes a string as input, converts it to lower case, and then creates a set from it.
# The set data structure in Python automatically removes duplicates, so the resulting set only contains distinct characters.
# Finally, the function returns the length of this set, which is the number of distinct characters in the original string.


# In case you want to ignore spaces:

def count_distinct_characters(string: str) -> int:
    string = string.replace(' ', '').lower()
    distinct_characters = set(string)
    return len(distinct_characters)

print(count_distinct_characters('Jerry and Tom'))
# In this case, the string becomes 'jerryandtom' and the set becomes {'j', 'e', 'r', 't', 'a', 'n', 'd', 'o', 'm'}
# So the function returns 8.


# In case you want to ignore case and spaces:

def count_distinct_characters(string: str) -> int:
    string = string.replace(' ', '').lower()
    distinct_characters = set(string)
    return len(distinct_characters