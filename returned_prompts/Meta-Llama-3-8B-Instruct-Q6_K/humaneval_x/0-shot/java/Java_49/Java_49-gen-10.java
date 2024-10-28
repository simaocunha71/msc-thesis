Here is a simple and efficient solution for the problem:

```java
public int modp(int n, int p) {
    if (n == 0) {
        return 1;
    }
    if (n % 2 == 0) {
        int half = modp(n / 2, p);
        return (half * half) % p;
    } else {
        return (n * modp(n - 1, p)) % p;
    }
}
```

This solution uses the property of modular exponentiation, which states that `(a * b) mod p = ((a mod p) * (b mod p)) mod p`. It also uses the fact that `a^(2n) mod p = ((a mod p)^(n) mod p)^2 mod p`, and `a^(2n+1) mod p = (a mod p) * (a^(2n) mod p) mod p`.

The function works by recursively dividing the exponent `n` by 2, until it is 0, and then combining the results using the above properties. If `n` is odd, it multiplies the result by `n` and takes the remainder modulo `p`.

This solution is efficient because it only requires a constant amount of extra memory and it does a constant amount of work for each recursive call. The time complexity is O(log n), where n is the exponent.

Note that this solution assumes that `p` is a prime number. If `p` is not prime, the solution may not work correctly. In that case, you would need to use a more complex algorithm, such as the Montgomery ladder.