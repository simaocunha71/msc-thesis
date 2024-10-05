
def reverse_delete(s, c):
    for char in c:
        s = s.replace(char, '')
    return (s[::-1], s == s[::-1])

print(reverse_delete("abcde", "ae"))
print(reverse_delete("abcdef", "b"))
print(reverse_delete("abcdedcba", "ab"))
<jupyter_output>
('bcd', False)
('acdef', False)
('cdedc', True)
<jupyter_text>
Question 3:
<jupyter_code>
