def largest_subset(numbers):
    g = 0
    for i in range(len(numbers)):
        g = gcd(g, numbers[i])
        if g == 1:
            return 0
    return len(numbers)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a