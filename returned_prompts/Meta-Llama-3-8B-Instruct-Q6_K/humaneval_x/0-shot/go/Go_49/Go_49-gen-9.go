// Return 2^n modulo p (be aware of numerics).
// >>> Modp(3, 5)
// 3
// >>> Modp(1101, 101)
// 2
// >>> Modp(0, 101)
// 1
// >>> Modp(3, 11)
// 8
// >>> Modp(100, 101)
// 1
def Modp(n, p):
    if n == 0:
        return 1
    if n % 2 == 0:
        if n // 2 % 2 == 0:
            return Modp(n // 2, p) * Modp(n // 2, p) % p
        else:
            return Modp(n // 2, p) * Modp(n // 2, p) * 2 % p
    else:
        return 2 * Modp(n - 1, p) % p

B:
// Return 2^n modulo p (be aware of numerics).
// >>> Modp(3, 5)
// 3
// >>> Modp(1101, 101)
// 2
// >>> Modp(0, 101)
// 1
// >>> Modp(3, 11)
// 8
// >>> Modp(100, 101)
// 1
def Modp(n, p):
    if n == 0:
        return 1
    if n % 2 == 0:
        return pow(2, n // 2, p) * pow(2, n // 2, p)
    else:
        return pow(2, n - 1, p) * 2 % p

C:
// Return 2^n modulo p (be aware of numerics).
// >>> Modp(3, 5)
// 3
// >>> Modp(1101, 101)
// 2
// >>> Modp(0, 101)
// 1
// >>> Modp(3, 11)
// 8
// >>> Modp(100, 101)
// 1
def Modp(n, p):
    return pow(2, n, p)

D:
// Return 2^n modulo p (be aware of numerics).
// >>> Modp(3, 5)
// 3
// >>> Modp(1101, 101)
// 2