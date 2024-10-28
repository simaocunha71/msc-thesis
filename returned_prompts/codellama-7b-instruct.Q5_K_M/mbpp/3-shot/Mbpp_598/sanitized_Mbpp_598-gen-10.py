def armstrong_number(n):
    return n == sum([int(i)**3 for i in str(n)])