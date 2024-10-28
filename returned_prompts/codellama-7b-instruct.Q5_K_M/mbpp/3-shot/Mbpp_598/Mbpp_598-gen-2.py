
def armstrong_number(n):
    num_list = list(map(int, str(n)))
    total = 0
    for i in num_list:
        total += i ** 3
    if n == total:
        return True
    else:
        return False


