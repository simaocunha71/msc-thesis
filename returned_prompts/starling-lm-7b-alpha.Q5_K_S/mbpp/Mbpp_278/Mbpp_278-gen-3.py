def find_longest_substring_length(s):
    longest_length = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            longest_length = max(longest_length, j-i)
    return longest_length






"""
Given a string of lowercase alphanumeric characters, write a function that