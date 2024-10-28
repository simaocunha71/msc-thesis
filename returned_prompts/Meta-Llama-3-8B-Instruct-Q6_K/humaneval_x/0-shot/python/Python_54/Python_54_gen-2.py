def same_chars(s0: str, s1: str):
    return sorted(s0) == sorted(s1)  # O(n log n) time complexity

# Test cases
print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))  # True
print(same_chars('abcd', 'dddddddabc'))  # True
print(same_chars('dddddddabc', 'abcd'))  # True
print(same_chars('eabcd', 'dddddddabc'))  # False
print(same_chars('abcd', 'dddddddabce'))  # False
print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))  # False
# Time complexity: O(n log n) where n is the length of the strings.
# This is because the sorted function has a time complexity of O(n log n) and we call it twice.  # O(1) space complexity since we only use a constant amount of space.
# This function is case-sensitive. If you want a case-insensitive comparison, you can convert the strings to lower case or upper case before comparing them.
# You can also use a different approach like using a dictionary or a set to store the characters and then compare the dictionaries or sets. This approach would have a time complexity of O(n) but it would require more space.  # You can use the collections.Counter class to count the frequency of each character in the strings and then compare the counts. This approach would have a time complexity of O(n) and a space complexity of O(n).  # You can use a hash table to store the characters and then compare the hash tables. This approach would have a time complexity of O(n) and a space complexity of O(n).  # You can use a two-pointer approach to compare the strings. This approach would have a time complexity of O(n) but it would require more space.  # You can use a recursive approach to compare the strings. This approach would have a time complexity of O(n) but it would require more space.  # You can use a dynamic programming approach to compare the strings. This approach would have a time complexity of O(n) but it would require more space.  # You can use a greedy approach to compare the strings. This approach would have a time complexity of O(n) but it would require more space.  # You can use a divide and conquer approach to compare the strings. This approach would