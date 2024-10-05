def reverse_delete(s,c):
    res = ''
    for x in s:
        if x not in c:
            res += x
    return res, res == res[::-1]

print(reverse_delete('abcde', 'ae'))
print(reverse_delete('abcdef', 'b'))
print(reverse_delete('abcdedcba', 'ab'))