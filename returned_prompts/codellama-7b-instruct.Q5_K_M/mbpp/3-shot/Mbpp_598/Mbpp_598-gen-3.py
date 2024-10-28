
def armstrong_number(n):
    n = str(n)
    return sum([int(i) ** 3 for i in n]) == n


