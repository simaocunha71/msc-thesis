def reverse_delete(s,c):
    s = ''.join([i for i in s if i not in c])
    return s, s == s[::-1]

print(reverse_delete("abcde", "ae"))
print(reverse_delete("abcdef", "b"))
print(reverse_delete("abcdedcba", "ab"))