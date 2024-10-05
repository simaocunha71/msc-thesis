Here is a possible implementation of the modp function in Java:

```java
public int modp(int n, int p) {
    if (n == 0) {
        return 1;
    }
    int result = 1;
    int power = n;
    while (power > 0) {
        if ((power & 1) == 1) {
            result = (result * 2) % p;
        }
        power >>= 1;
        if (power > 0) {
            power--;
            power = (power * 2) % p;
        }
    }
    return result;
}
```

This implementation uses the binary exponentiation algorithm, which is an efficient way to compute powers of a number modulo another number. The algorithm works by repeatedly squaring the base and reducing the exponent by half, while also multiplying the result by the base if the current bit of the exponent is 1. The time complexity of this algorithm is O(log n), where n is the exponent.