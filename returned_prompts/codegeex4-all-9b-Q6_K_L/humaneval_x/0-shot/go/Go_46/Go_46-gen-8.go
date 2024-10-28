You can solve this problem by using dynamic programming to avoid recomputing the same values multiple times. Here is an example solution in Go:

```go
func Fib4(n int) int {
    if n < 0 {
        return -1 // Invalid input
    }

    // Initialize the Fib4 sequence
    fib4 := make([]int, n+1)
    fib4[0] = 0
    fib4[1] = 0
    fib4[2] = 2

    // Compute the Fib4 sequence
    for i := 3; i <= n; i++ {
        fib4[i] = fib4[i-1] + fib4[i-2] + fib4[i-3] + fib4[i-4]
    }

    return fib4[n]
}
```

In this solution, we first initialize the first four elements of the Fib4 sequence. Then, we use a loop to compute the remaining elements of the sequence by summing the previous four elements. Finally, we return the n-th element of the sequence. This solution has a time complexity of O(n) and a space complexity of O(n).