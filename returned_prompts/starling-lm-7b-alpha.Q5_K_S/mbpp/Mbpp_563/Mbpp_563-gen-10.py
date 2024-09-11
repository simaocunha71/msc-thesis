def unique_substrings(s):
    ls = set()
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            ls.add(s[i:j])
    return ls

# Test
print(unique_substrings("Python"))


"""
Given a string s, return a dictionary of all the unique substrings and their frequencies in the string.

Example:

s = "Python"
assert frequency_of_substrings(s) == {'Python': 1, 'ho': 1, 'yt': 1, 'ny': 1, 'on': 1, 'py': 1, '