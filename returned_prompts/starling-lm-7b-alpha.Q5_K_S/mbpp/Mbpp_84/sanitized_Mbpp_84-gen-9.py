from math import sqrt
def sequence(n):
    if n == 0: return 2
    if n == 1: return 3
    if n == 2: return 5
    if n == 3: return 8
    if n == 4: return 13
    if n == 5: return 21
    if n == 6: return 34
    if n == 7: return 55
    if n == 8: return 89
    if n == 9: return 144
    if n == 10: return 233
    #return sum(sequence(n-1), sequence(n-2), sequence(n-3))
    if (n-3) % 3 == 0:
        return sequence(n-3) + sequence(n-2) + sequence(n-1)
    if (n-2) % 3 == 0:
        return sequence(n-2) + sequence(n-1) + sequence(n)
    if (n-1) % 3 == 0:
        return sequence(n-1) + sequence(n) + sequence(n+1)
    if (n-4) % 3 == 0:
        return sequence(n-4) + sequence(n-3) + sequence(n-2)
    if (n-5) % 3 == 0:
        return sequence(n-5) + sequence(n-4) + sequence(n-3)
    if (n-6) % 3 == 0:
        return sequence(n-6) + sequence(n-5) + sequence(n-4)
    if (n-7) % 3 == 0:
        return sequence(n-7) + sequence(n-6) + sequence(n-5)
    if (n-8) % 3 == 0:
        return sequence(n-8) + sequence(n-7) + sequence(n-6)
    if (n-9) % 3 == 0:
        return sequence(n-9) + sequence(n-8) + sequence(n-7)