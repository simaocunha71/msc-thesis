
def solve(s):
    result = ''
    for i in range(len(s)):
        if s[i].isalpha():
            result += s[i].upper() if s[i].islower() else s[i].lower()
        else:
            result += s[i]
    if not result:
        result = s[::-1]
    return result
