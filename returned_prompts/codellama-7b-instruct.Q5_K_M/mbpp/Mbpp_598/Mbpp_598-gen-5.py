def armstrong_number(n):
    number_of_digits = len(str(n))
    sum = 0
    for digit in str(n):
        sum += int(digit)**number_of_digits
    if sum == n:
        return True
    else:
        return False



