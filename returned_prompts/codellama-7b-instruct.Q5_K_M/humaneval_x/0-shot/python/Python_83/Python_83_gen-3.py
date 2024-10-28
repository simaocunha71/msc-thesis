
def starts_one_ends(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return starts_one_ends(n-1) + starts_one_ends(n-2)
