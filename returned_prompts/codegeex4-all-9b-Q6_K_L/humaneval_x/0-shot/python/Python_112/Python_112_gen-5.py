def reverse_delete(s,c):
    res = ''.join(ch for ch in s if ch not in c)
    return (res, res == res[::-1])

print(reverse_delete("abcde","ae"))
print(reverse_delete("abcdef","b"))
print(reverse_delete("abcdedcba","ab"))