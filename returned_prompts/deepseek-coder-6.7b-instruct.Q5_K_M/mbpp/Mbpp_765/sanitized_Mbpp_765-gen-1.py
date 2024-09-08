def is_polite(n):
    i = 1
    count = 0
    while count < n:
        if bin(i).count('1') > bin(i).count('10'):
            count += 1
        i += 1
    return i-1