def reverse_delete(s,c):
    s = s.replace(c, '')
    return (s, s == s[::-1])

# Test cases
print(reverse_delete("abcde", "ae"))  # ('bcd', False)
print(reverse_delete("abcdef", "b"))  # ('acdef', False)
print(reverse_delete("abcdedcba", "ab"))  # ('cdedc', True)