
def armstrong_number(n):
    n = str(n)
    sum = 0
    for i in n:
        sum += int(i) ** 3
    if sum == int(n):
        return True
    return False


