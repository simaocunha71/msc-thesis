def solve(s):
    s = list(s)
    for i in range(len(s)):
        if s[i].isalpha():
            s[i] = s[i].swapcase()
        else:
            s[i] = s[i][::-1]
    return ''.join(s)

print(solve("1234")) # "4321"
print(solve("ab")) # "AB"
print(solve("#a@C")) # "#A@c"