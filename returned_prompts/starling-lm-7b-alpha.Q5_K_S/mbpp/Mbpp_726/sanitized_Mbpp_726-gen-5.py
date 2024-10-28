def multiply_elements(t):
    r = []
    for i in range(len(t)-1):
        r.append(t[i]*t[i+1])
    return tuple(r)