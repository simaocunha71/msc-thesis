You can use a loop to iterate from n-1 down to 1, checking if the current number divides n evenly. The first number that divides n evenly will be the largest divisor. Here's the updated code:

```java
public int largestDivisor(int n) {
    for (int i = n - 1; i >= 1; i--) {
        if (n % i == 0) {
            return i;
        }
    }
    return -1; // If no divisor is found, return -1
}
```

This code will return the largest divisor of n that is less than n, or -1 if no divisor is found.