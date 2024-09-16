def is_undulating(num):
    s = str(num)
    return any(s[i] > s[i-1] for i in range(1, len(s))) and \
           any(s[i] > s[i+1] for i in range(len(s)-1))