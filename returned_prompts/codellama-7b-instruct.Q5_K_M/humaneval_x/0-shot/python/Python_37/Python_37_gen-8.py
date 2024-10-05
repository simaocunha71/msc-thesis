

def sort_even(l):
    l = list(l)
    for i in range(len(l)):
        if i % 2 == 0:
            l[i] = sorted(l[i])
    return l
