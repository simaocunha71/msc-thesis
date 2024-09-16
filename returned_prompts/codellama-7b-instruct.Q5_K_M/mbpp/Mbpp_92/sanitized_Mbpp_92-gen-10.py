def is_undulating(num):
    n = str(num)
    for i in range(1, len(n)):
        if int(n[i]) < int(n[i-1]):
            return False
    return True