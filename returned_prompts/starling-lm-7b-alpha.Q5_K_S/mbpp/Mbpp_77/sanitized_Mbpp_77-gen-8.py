def is_Diff(n):
    if abs(sum(map(int, str(n))) - (len(str(n)) % 2) * 9) % 11 == 0:
        return False
    else:
        return True