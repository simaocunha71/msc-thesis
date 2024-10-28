def armstrong_number(n):
    digits = [int(i) for i in str(n)]
    return sum([pow(i, len(str(n))) for i in digits]) == n