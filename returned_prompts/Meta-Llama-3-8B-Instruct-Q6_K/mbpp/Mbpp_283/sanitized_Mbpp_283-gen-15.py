def validate(n):
    freq = [0] * 10
    while n > 0:
        digit = n % 10
        freq[digit] += 1
        n //= 10
    for i in range(10):
        if freq[i] > i:
            return False
    return True