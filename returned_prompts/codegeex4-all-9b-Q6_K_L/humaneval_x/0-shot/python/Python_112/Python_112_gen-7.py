def reverse_delete(s,c):
    return (s.translate(None, c), s.translate(None, c) == s.translate(None, c)[::-1])

print reverse_delete("abcde","ae")
print reverse_delete("abcdef","b")
print reverse_delete("abcdedcba","ab")