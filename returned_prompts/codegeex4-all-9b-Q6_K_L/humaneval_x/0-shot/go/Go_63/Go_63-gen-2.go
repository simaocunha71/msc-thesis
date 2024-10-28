The FibFib number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:

Fibfib(0) == 0
Fibfib(1) == 0
Fibfib(2) == 1
Fibfib(n) == Fibfib(n-1) + Fibfib(n-2) + Fibfib(n-3).

We can use dynamic programming to solve this problem. We will create an array to store the Fibfib numbers and initialize the first three elements. Then, for each subsequent element, we will compute it as the sum of the previous three elements. Finally, we will return the n-th element of the array.

Here is the code in Go:

```
func Fibfib(n int) int {
    if n < 0 {
        return -1
    }
    if n == 0 || n == 1 {
        return 0
    }
    if n == 2 {
        return 1
    }
    fib := make([]int, n+1)
    fib[0] = 0
    fib[1] = 0
    fib[2] = 1
    for i := 3; i <= n; i++ {
        fib[i] = fib[i-1] + fib[i-2] + fib[i-3]
    }
    return fib[n]
}
```

This function takes an integer `n` as input and returns the n-th element of the Fibfib number sequence. If `n` is negative, the function returns -1. If `n` is 0 or 1, the function returns 0. If `n` is 2, the function returns 1. For all other values of `n`, the function computes the n-th element using dynamic programming.