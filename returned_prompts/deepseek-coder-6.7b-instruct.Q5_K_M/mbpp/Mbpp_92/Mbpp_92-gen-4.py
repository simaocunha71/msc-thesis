
def is_undulating(n):
    s = str(n)
    for i in range(2, len(s)):
        if s[i] == s[i-1] or s[i] == s[i-2]:
            return False
    return True


