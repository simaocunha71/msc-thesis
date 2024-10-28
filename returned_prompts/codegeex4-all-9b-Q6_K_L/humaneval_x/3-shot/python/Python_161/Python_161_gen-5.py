    if s.isalpha():
        return s.upper() if s.islower() else s.lower()
    else:
        return s[::-1]