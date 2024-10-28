def solve(s):
    if s.isalpha():
        if s.islower():
            return s.upper()
        else:
            return s.lower()
    else:
        return s[::-1]