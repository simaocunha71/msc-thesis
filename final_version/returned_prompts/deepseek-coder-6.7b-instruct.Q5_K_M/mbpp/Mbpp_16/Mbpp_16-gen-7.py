def text_lowercase_underscore(s):
    return any(c.islower() and c.islower() for c in s)

print(text_lowercase_underscore("aab_cbbbc"))

"""
def text_lowercase_underscore(s):
    for i in range(len(s)-1):
        if s[i].islower() and s[i+1].islower() and s[i+1]=="_":
            return True
    return False
print(text_lowercase_underscore("aab_cbbbc"))
"""

Explanation:
The function `text_lowercase_underscore` checks if any two consecutive characters in the input string are lowercase letters and the next character is an underscore. If it finds such a pair, it returns `True`; otherwise, it returns `False`.

In the string "aab_cbbbc", the pair "bb" is a lowercase letter followed by an underscore, so the function should return `True`.
"""

"""
