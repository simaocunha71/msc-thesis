def sum(a, b):
    sum = 0
    for i in range(1, a + 1):
        if i % a == 0 and i % b == 0:
            sum += i
    return sum