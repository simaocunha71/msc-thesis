def solve(s):
    result = ''
    for ch in s:
        if ch.isalpha():
            result += ch.swapcase()
        else:
            result += ch
    if result.isalpha():
        return result[::-1]
    return result

print(solve("1234"))
print(solve("ab"))
print(solve("#a@C"))
print(solve("ab#A"))
print(solve("abc"))
print(solve("abA"))