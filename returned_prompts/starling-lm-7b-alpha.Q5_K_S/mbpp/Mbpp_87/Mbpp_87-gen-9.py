def get_lower_indexes(s):
    return [i for i in range(len(s)) if s[i] in 'abcdefghijklmnopqrstuvwxyz']

# Test
print(get_lower_indexes("apples"))
# Output: [0, 1, 2, 3, 4]

print(get_lower_indexes("orange"))
# Output: [0, 1, 2, 3, 4, 5]

print(get_lower_indexes("carrot"))
# Output: [0, 1, 2, 3]

















"""
Write a function that will check if two given strings are anagrams of each other. That is, if the letters in the first string can be rearranged so that they form the second string.

Examples: