
def armstrong_number(n):
    num_str = str(n)
    sum = 0
    for i in num_str:
        sum += int(i)**len(num_str)
    if sum == int(n):
        return True
    else:
        return False


