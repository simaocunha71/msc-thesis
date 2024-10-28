def div_list(a,b):
    if len(a) != len(b):
        return "Error"
    c = []
    for i in range(len(a)):
        c.append(a[i]/b[i])
    return c