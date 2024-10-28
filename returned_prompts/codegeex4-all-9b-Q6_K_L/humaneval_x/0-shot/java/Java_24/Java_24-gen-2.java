Here is a simple Java solution using a for loop to iterate from 1 to n/2 and check if n is divisible by the current number:

```java
public int largestDivisor(int n) {
    for (int i = n / 2; i > 0; i--) {
        if (n % i == 0) {
            return i;
        }
    }
    return n;
}
```

This function starts from the half of n and checks if n is divisible by i. If n is divisible by i, then i is the largest divisor of n that is smaller than n. If no such divisor is found, n itself is the largest divisor.