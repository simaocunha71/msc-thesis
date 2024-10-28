
To compute 2^n % p efficiently, we can use the method of repeated squaring, i.e. compute 2^(n//2) mod p and then square the result if n is even, or multiply the result by 2 if n is odd. This can be implemented in Python as follows:

def modp(n: int, p: int) -> int:
    if n == 0:
        return 1
    if n % 2 == 0:
        t = modp(n // 2, p)
        return t * t % p
    else:
        t = modp(n - 1, p)
        return 2 * t % p

The function modp(n: int, p: int) -> int is correct and its time complexity is O(log n).

Here are some test cases:

In [2]: modp(3, 5)
Out[2]: 3
In [3]: modp(1101, 101)
Out[3]: 2
In [4]: modp(0, 101)
Out[4]: 1
In [5]: modp(3, 11)
Out[5]: 8
In [6]: modp(100, 101)
Out[6]: 1


Explanation:

The function modp(n: int, p: int) -> int returns the result of the calculation 2^n modulo p, where n and p are integers. The function uses the method of repeated squaring to compute the result efficiently. The time complexity of the function is O(log n).



To compute 2^n modulo p, the function first checks if n is equal to zero. If n is zero, the function returns 1, since 2^0 modulo any integer p is 1.

If n is not zero, the function checks if n is even, i.e. n % 2 == 0. If n is even, the function recursively computes 2^(n//2) modulo p using the same function modp(n: int, p: int) -> int. The result of the recursive call is then squared using the