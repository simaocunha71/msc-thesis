Here is a Java solution using dynamic programming to store previously computed values and avoid redundant calculations. This solution has a time complexity of O(n) and a space complexity of O(n).

```java
public int fibfib(int n) {
    if (n < 0) {
        throw new IllegalArgumentException("n must be a non-negative integer.");
    }
    if (n == 0 || n == 1) {
        return 0;
    }
    if (n == 2) {
        return 1;
    }

    int[] fibfib = new int[n + 1];
    fibfib[0] = 0;
    fibfib[1] = 0;
    fibfib[2] = 1;

    for (int i = 3; i <= n; i++) {
        fibfib[i] = fibfib[i - 1] + fibfib[i - 2] + fibfib[i - 3];
    }

    return fibfib[n];
}
```

This solution first checks for some base cases (n = 0, n = 1, and n = 2), then initializes an array to store the fibfib values. It then iterates from 3 to n, computing each fibfib value as the sum of the previous three values. Finally, it returns the n-th fibfib value.