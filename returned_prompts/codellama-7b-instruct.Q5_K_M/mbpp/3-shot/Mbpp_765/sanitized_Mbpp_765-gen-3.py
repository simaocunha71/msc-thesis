def is_polite(n):
    if n < 10:
        return n
    digits = [int(x) for x in str(n)]
    count = 0
    for i in range(len(digits)):
        if digits[i] == 0 or digits[i] == 1:
            count += 1
    if count < 2:
        return n+1
    else:
        return is_polite(n+1)