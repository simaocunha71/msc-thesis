
def reverse_delete(s,c):
    for ch in c:
        s = s.replace(ch, '')
    return (s, s == s[::-1])

print(reverse_delete("abcde", "ae"))  # ('bcd', False)
print(reverse_delete("abcdef", "b"))  # ('acdef', False)
print(reverse_delete("abcdedcba", "ab"))  # ('cdedc', True)

# This solution works by iterating over each character in string c and replacing all occurrences of that character in string s.
# After that, it checks whether the resulting string is the same when reversed (which is equivalent to checking if it's a palindrome).
# It returns the resulting string and a boolean indicating whether or not the string is a palindrome.
<jupyter_output>
('bcd', False)
('acdef', False)
('cdedc', True)
<jupyter_text>
Question 5
<jupyter_code>
