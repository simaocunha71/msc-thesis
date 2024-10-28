```java
public int fibfib(int n) {
    if (n <= 1) {
        return 0;
    } else if (n == 2) {
        return 1;
    } else {
        int[] fibfib = new int[n + 1];
        fibfib[0] = 0;
        fibfib[1] = 0;
        fibfib[2] = 1;
        for (int i = 3; i <= n; i++) {
            fibfib[i] = fibfib[i - 1] + fibfib[i - 2] + fibfib[i - 3];
        }
        return fibfib[n];
    }
}
```
The function `fibfib` calculates the `n-th` element of the fibfib number sequence. If `n` is less than or equal to 1, it returns 0. If `n` is 2, it returns 1. Otherwise, it calculates the `n-th` element using dynamic programming. The array `fibfib` stores the elements of the sequence from 0 to `n`. The function iterates from 3 to `n` and updates the elements of the sequence using the recurrence relation `fibfib[i] = fibfib[i - 1] + fibfib[i - 2] + fibfib[i - 3]`. Finally, it returns the `n-th` element of the sequence.