Here is the Java solution for the problem:

```java
public int modp(int n, int p) {
    if (n == 0) {
        return 1;
    }
    int half = modp(n / 2, p);
    if (n % 2 == 0) {
        return (half * half) % p;
    } else {
        return ((half * half) % p * 3) % p;
    }
}
```

This solution uses a divide-and-conquer approach, which significantly reduces the number of multiplications. The base case is when n is 0, in which case the result is 1. For other cases, it first computes the result for n/2, then squares it and multiplies by 3 if n is odd, or simply squares it if n is even. The result is then taken modulo p.

This solution has a time complexity of O(log n), since each recursive call reduces n by approximately half, and a space complexity of O(log n) due to the recursive call stack.