def all_Characters_Same(s):
    if len(s) == 0:
        return True
    if len(s) == 1:
        return True
    if len(s) == 2:
        if s[0] == s[1]:
            return True
        else:
            return False
    if len(s) > 2:
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                return False
        return True