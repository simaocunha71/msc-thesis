```java
public int largestPrimeFactor(int n) {
    int largestPrime = 0;
    for (int i = 2; i <= n; i++) {
        while (n % i == 0) {
            largestPrime = i;
            n /= i;
        }
    }
    return largestPrime;
}
```