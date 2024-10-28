
def reverse_delete(s,c):
    for ch in c:
        s = s.replace(ch, '')
    return (s, s == s[::-1])

print(reverse_delete("abcde", "ae"))
print(reverse_delete("abcdef", "b"))
print(reverse_delete("abcdedcba", "ab"))
<jupyter_output>
('bcd', False)
('acdef', False)
('cdedc', True)
<jupyter_text>
Problem 3:
<jupyter_code>
