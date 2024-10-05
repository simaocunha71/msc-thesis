
    def reverse_delete(s, c):
        for char in c:
            s = s.replace(char, '')
        return (s[::-1], s[::-1] == s)

    print(reverse_delete("abcde", "ae"))
    print(reverse_delete("abcdef", "b"))
    print(reverse_delete("abcdedcba", "ab"))

Output:

    ('bcd', False)
    ('acdef', False)
    ('cdedc', True)
"""

# Task 2
"""
