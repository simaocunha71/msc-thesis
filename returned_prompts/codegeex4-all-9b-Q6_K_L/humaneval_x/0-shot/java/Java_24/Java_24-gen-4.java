Here is a possible implementation in Java:

```java
public int largestDivisor(int n) {
    for (int i = n / 2; i > 0; i--) {
        if (n % i == 0) {
            return i;
        }
    }
    return 1;
}
```

This function starts from `n / 2` and goes down to `1`. For each number `i`, it checks if `n` is divisible by `i` (i.e., `n % i == 0`). If it is, it returns `i` as the largest divisor. If no divisor is found, it returns `1` as the largest divisor.