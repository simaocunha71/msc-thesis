
def solve(s):
    return ''.join([c.lower() if c.isalpha() else c for c in s[::-1]])
