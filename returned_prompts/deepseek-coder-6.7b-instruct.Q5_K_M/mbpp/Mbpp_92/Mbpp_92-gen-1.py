
def is_undulating(n):
    s = str(n)
    for i in range(len(s)-2):
        if s[i] == s[i+1] or s[i+1] != s[i+2]:
            return False
    return True


print(is_undulating(1212121))

#tests/test_3.py
"""
