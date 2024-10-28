def armstrong_number(n):
    num = n
    sum = 0
    temp = 0
    while num>0:
        digit = num%10
        sum += digit**3
        num //= 10
    if temp == n:
        return True
    else:
        return False

