
def solve(s):
    result = ""
    for i in range(len(s)):
        if s[i].isalpha():
            result += s[i].lower() if s[i].isupper() else s[i].upper()
        else:
            result += s[i]
    return result if not result else result[::-1]

