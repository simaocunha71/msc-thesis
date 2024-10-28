Here is a simple solution in Java. The logic is to iterate from n-1 down to 1 and return the first number that divides n evenly.

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

This solution works but it is not efficient. It has a time complexity of O(n) which can be improved. We can check the divisibility by 2 and 3 first, then check the odd numbers starting from 5. This will reduce the time complexity to O(sqrt(n)).

```java
public int largestDivisor(int n) {
    if (n % 2 == 0) {
        return 2;
    }
    for (int i = 3; i * i <= n; i += 2) {
        if (n % i == 0) {
            return i;
        }
    }
    return n; // If n is a prime number, the largest divisor is n itself
}
```

This solution first checks if n is divisible by 2. If it is, then 2 is the largest divisor. Otherwise, it checks the odd numbers starting from 3 up to the square root of n. If it finds a number that divides n evenly, then that number is the largest divisor. If no number is found, then n is a prime number and the largest divisor is n itself.