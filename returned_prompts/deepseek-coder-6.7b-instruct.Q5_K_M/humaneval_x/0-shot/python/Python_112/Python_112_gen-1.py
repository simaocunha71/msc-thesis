
    s = ''.join([i for i in s if i not in c])
    return (s, s == s[::-1])

# Test Cases:
print(reverse_delete('abcde', 'ae'))  # should return ('bcd', False)
print(reverse_delete('abcdef', 'b'))  # should return ('acdef', False)
print(reverse_delete('abcdedcba', 'ab'))  # should return ('cdedc', True)

# Time Complexity: O(n)
# Space Complexity: O(n)
# where n is the length of the string s
<jupyter_output>
('bcd', False)
('acdef', False)
('cdedc', True)
<jupyter_text>
Question 2
<jupyter_code>
