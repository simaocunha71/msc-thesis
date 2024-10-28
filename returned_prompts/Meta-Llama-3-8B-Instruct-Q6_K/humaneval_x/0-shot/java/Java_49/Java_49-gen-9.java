```java
public int modp(int n, int p) {
    if (p == 1) {
        return 0;
    }
    long res = 1;
    n = n % p;
    while (n > 0) {
        if ((n & 1) == 1) {
            res = (res * (long) (p - 1)) % p;
        }
        n = n >> 1;
        p = (long) p * (long) p % p;
    }
    return (int) res;
}
```

This problem can be solved using the property of modular exponentiation. The idea is to use the fact that a^(p-1) % p is congruent to 1. So, we can calculate a^(n-1) % p by repeatedly squaring a and reducing the result modulo p, until n becomes 0. 

Here is the Java code that implements this:

```java
public int modp(int n, int p) {
    if (p == 1) {
        return 0;
    }
    long res = 1;
    n = n % p;
    while (n > 0) {
        if ((n & 1) == 1) {
            res = (res * (long) (p - 1)) % p;
        }
        n = n >> 1;
        p = (long) p * (long) p % p;
    }
    return (int) res;
}
```

This code calculates the result modulo p, which ensures that the result is within the range of integers. The time complexity of this code is O(log n), where n is the input number. The space complexity is O(1), as it only uses a constant amount of space. 





The above code is incorrect. It should be `res = (res * (long) p) % p;` instead of `res = (res * (long) (p - 1)) % p;`. The correct code should be:

```java
public int modp(int n, int p) {
    if (p == 1) {
        return 1;
    }
    long res = 1;
    n = n % p;
    while (n > 0) {
        if ((n & 1) == 1) {
            res = (res * (long) p) % p;
        }
        n