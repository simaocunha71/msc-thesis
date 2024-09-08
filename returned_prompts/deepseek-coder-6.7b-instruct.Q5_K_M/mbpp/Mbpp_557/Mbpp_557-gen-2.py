def first_non_repeating_char(s):
    for i in s:
        if s.count(i)==1:
            return i

print(first_non_repeating_char("abcabc"))
print(first_non_repeating_char("abc"))

"""
Write a function to find the longest common prefix from a list of strings.
assert longest_common_prefix(["flower","