def reverse_delete(s,c):
    result = s.translate(None, c)
    return (result, result == result[::-1])

# Test cases
print(reverse_delete("abcde", "ae"))  # should return ('bcd', False)
print(reverse_delete("abcdef", "b"))  # should return ('acdef', False)
print(reverse_delete("abcdedcba", "ab"))  # should return ('cdedc', True)