def extract_values(s):
    s = s.replace('"', '')
    return s.split(', ')

# Test the function
assert extract_values('"Python",  "PHP",  "Java"') == ['Python', 'PHP', 'Java']


# Alternative solution using Regular Expressions
import re

def extract_values(s):
    return re.findall(r'"([^"]*)"', s)

# Test the function
assert extract_values('"Python",  "PHP",  "Java"') == ['Python', 'PHP', 'Java']
<jupyter_output>
<empty_output>
<jupyter_text>
Question 4:Write a function to find the longest palindrome substring in a given string.
<jupyter_code>
def longest_palindrome(s):
    if not s:
        return ''
    longest = ''
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            sub = s[i:j]
            if sub == sub[::-1]:
                if len(sub) > len(longest):
                    longest = sub
    return longest

# Test the function
assert longest_palindrome('babad') == 'aba'
assert longest_palindrome('cbbd') == 'bb'
<jupyter_output>
<empty_output>
<jupyter_text>
Question 5:Write a function to find the longest common prefix from a list of strings.
<jupyter_code>
def longest_common_prefix(strs):
    if not strs:
        return ''
    shortest = min(strs, key=len)
    for i, char in enumerate(shortest):
        for other in strs:
            if other[i] != char:
                return shortest[:i]
    return shortest

# Test the function
assert longest_common_prefix(['flower', 'flow', 'flight']) == 'fl'
assert longest_common_prefix(['dog', 'racecar', 'car']) == ''
