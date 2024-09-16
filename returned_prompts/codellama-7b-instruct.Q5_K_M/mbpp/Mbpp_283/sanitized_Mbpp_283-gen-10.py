def validate(n):
    count = [0] * 10
    while n > 0:
        count[n % 10] += 1
        n //= 10
    for i in range(10):
        if count[i] > i:
            return False
    return True