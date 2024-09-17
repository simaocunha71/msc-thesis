def is_woodall(n):
    if str(n) == ''.join(sorted(str(n))):
        return True
    else:
        return False