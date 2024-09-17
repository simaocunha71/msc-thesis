def sum_list(a,b):
    if len(a) != len(b):
        return "The length of the two list must be the same."
    else:
        c = []
        for i in range(len(a)):
            c.append(a[i]+b[i])
        return c