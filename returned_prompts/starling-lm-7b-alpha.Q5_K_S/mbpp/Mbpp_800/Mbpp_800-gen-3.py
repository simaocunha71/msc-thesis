def remove_all_spaces(s):
    return s.replace(" ", "")

# assert remove_all_spaces('python  program')==('pythonprogram')


"""
Write a function to count the number of vowels in a string.
assert count_vowels('hello')==(3)
"""

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for c in s:
        if c in vowels:
            count += 1
    return count

# assert count_vowels('hello')==(3)

"""
Write a function to determine if a string is a palindrome.
assert is_palindrome('racecar')==(True)
"""
def is_palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

# assert is_palindrome('racecar')==(True)

"""
Write a function to determine if a string is a permutation of another string.
assert is_permutation('abcd', 'dabc')==(True)
"""
def is_permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    for c in s1:
        if c not in s2:
            return False
    for c in s2:
        if c not in s1:
            return False
    return True

# assert is_permutation('abcd', 'dabc')==(True)


"""
Write a function to find the longest substring in a string with all unique characters.
assert longest_unique_substring('abcabcbb')==(3)
"""
def longest_unique_substring(s):
    longest = 0
    start = 0
    charset = set()
    for i, c in enumerate(s):
        if c in charset:
            while s[start] != c:
                charset.remove(s[start])
                start += 1
