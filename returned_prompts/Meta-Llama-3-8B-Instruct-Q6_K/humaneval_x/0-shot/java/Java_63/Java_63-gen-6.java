Here is the Java function that efficiently computes the n-th element of the fibfib number sequence:

```java
public int fibfib(int n) {
    if (n <= 1) {
        return 0;
    }
    int[] fibfib = new int[n + 1];
    fibfib[1] = fibfib[2] = 0;
    for (int i = 3; i <= n; i++) {
        fibfib[i] = fibfib[i - 1] + fibfib[i - 2] + fibfib[i - 3];
    }
    return fibfib[n];
}
```

This function uses dynamic programming to efficiently compute the n-th element of the fibfib number sequence. It first checks if n is less than or equal to 1, in which case it returns 0. Then it creates an array of size n + 1 to store the fibfib numbers. It initializes the first two elements of the array to 0. Then it iterates from 3 to n, and at each iteration, it calculates the i-th fibfib number as the sum of the (i-1)th, (i-2)th, and (i-3)th fibfib numbers. Finally, it returns the n-th fibfib number.

This function has a time complexity of O(n) and a space complexity of O(n), which is efficient for computing the n-th element of the fibfib number sequence.