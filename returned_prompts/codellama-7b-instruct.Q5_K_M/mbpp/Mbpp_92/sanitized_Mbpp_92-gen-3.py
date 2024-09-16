def is_undulating(num):
    if len(str(num)) == 1:
        return False
    else:
        s = str(num)
        for i in range(len(s)-1):
            if int(s[i]) > int(s[i+1]):
                return False
        return True