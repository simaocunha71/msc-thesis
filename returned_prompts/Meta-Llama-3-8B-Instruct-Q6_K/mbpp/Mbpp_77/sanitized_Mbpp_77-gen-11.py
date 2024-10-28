def is_Diff(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum % 11 != 0