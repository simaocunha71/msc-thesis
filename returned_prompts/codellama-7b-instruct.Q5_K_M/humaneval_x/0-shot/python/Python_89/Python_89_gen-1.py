
def encrypt(s):
    s = s.lower()
    result = ''
    for i in range(len(s)):
        if s[i].isalpha():
            result += chr((ord(s[i]) - ord('a') + 2) % 26 + ord('a'))
        else:
            result += s[i]
    return result