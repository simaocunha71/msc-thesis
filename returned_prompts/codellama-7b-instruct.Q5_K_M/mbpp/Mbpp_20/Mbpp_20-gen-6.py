"""
def is_woodall(n):
    s = str(n)
    if len(s) != 3:
        return False
    for i in range(len(s)):
        if int(s[i]) != i+1:
            return False
    return True
"""
