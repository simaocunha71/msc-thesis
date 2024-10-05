    return sorted(s0) == sorted(s1)  # sort the characters in each string and compare
    # This function works by sorting the characters in each string and comparing the sorted strings.
    # If the characters are the same, the sorted strings will be equal, indicating that the characters in the original strings are the same.
    # This function works regardless of the order of the characters in the original strings and it also works for strings of different lengths.
    # The time complexity of this function is O(n log n) where n is the length of the strings. This is because sorting is done in O(n log n) time complexity. The space complexity is O(n) where n is the length of the strings. This is because the sorted strings are stored in memory.  # noqa: E501


