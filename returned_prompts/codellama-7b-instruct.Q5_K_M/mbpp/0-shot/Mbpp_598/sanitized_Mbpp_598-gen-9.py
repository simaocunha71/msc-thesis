def armstrong_number(n):
    return sum([int(i)**3 for i in str(n)])==n