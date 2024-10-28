
    if s:
        if s.isalpha():
            return s.swapcase()
        else:
            return s[::-1]
    else:
        return s
