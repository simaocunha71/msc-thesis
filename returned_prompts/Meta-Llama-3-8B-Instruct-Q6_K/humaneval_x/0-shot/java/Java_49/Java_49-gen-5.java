Here is a simple and efficient solution using the property of modular arithmetic that `a ≡ b (mod p)` implies `a^n ≡ b^n (mod p)`.

```java
public int modp(int n, int p) {
    if (n == 0) {
        return 1;
    }
    if (n % 2 == 0) {
        int half = modp(n / 2, p);
        return (half * half) % p;
    } else {
        int half = modp(n / 2, p);
        return ((half * half) % p * n) % p;
    }
}
```

This function uses the property of modular arithmetic to compute `2^n modulo p` efficiently. It recursively divides `n` by 2 until it becomes 0, and at each step, it squares the result modulo `p` and multiplies it by `n` if `n` is odd. The time complexity of this function is O(log n) and the space complexity is O(1).