def closest_num(n):
    str_n = str(n)
    if n < 10:
        return -1
    else:
        for i in range(len(str_n) - 1, 0, -1):
            if str_n[i] < str_n[i-1]:
                str_n = str_n[:i-1] + str_n[i] + ''.join(sorted(str_n[i-1:i] + str_n[i+1:]))
                return int(str_n)
        return int(str_n)