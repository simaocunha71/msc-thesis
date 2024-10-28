
To compute the n-th element of the Fibfib number sequence efficiently, we can use dynamic programming to store the previously computed values and avoid redundant calculations. Here's the modified code:

```go
func Fibfib(n int) int {
    if n == 0 || n == 1 {
        return 0
    }
    if n == 2 {
        return 1
    }

    fibfib := make([]int, n+1)
    fibfib[0] = 0
    fibfib[1] = 0
    fibfib[2] = 1

    for i := 3; i <= n; i++ {
        fibfib[i] = fibfib[i-1] + fibfib[i-2] + fibfib[i-3]
    }

    return fibfib[n]
}
```

In this code, we create an array `fibfib` of size `n+1` to store the previously computed values. We initialize the first three elements of the array based on the given conditions. Then, we use a for loop to calculate the remaining elements of the Fibfib sequence. Finally, we return the n-th element of the sequence. This approach ensures that we efficiently compute the n-th element of the Fibfib sequence without redundant calculations.