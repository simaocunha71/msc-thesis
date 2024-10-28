def armstrong_number(n):
    num_list = list(map(int, str(n)))
    sum = 0
    for i in num_list:
        sum += i**3
    if sum == n:
        return True
    else:
        return False
