def is_undulating(n):
    # convert to string
    n = str(n)
    # check whether each character is the same as the next
    for i in range(len(n) - 1):
        if n[i] != n[i + 1]:
            return False
    return True