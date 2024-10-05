def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
    # Convert the string to lowercase and convert it to a set to remove duplicates
    # Then, return the length of the set, which is the number of distinct characters
    # This function works because sets in Python automatically remove duplicates, 
    # and the order of elements in a set is not guaranteed to be the same as the order 
    # in which they were inserted, which is why we don't care about the order of characters
    # and can use a set to find the number of distinct characters.

# Testing the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 4

# The function correctly counts the number of distinct characters in the input string
# and ignores the case of the characters. It also works correctly even if the input string 
# contains duplicate characters. The function uses the set data structure to remove duplicates 
# and the len function to count the number of elements in the set. This makes the function 
# efficient for large input strings.