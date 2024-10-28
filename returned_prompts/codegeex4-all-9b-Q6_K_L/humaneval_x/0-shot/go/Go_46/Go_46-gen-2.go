You can solve this problem by using dynamic programming to store the previous results of the Fib4 sequence. Here is the solution:

```go
func Fib4(n int) int {
    if n < 0 {
        return -1
    }
    if n == 0 || n == 1 {
        return 0
    }
    if n == 2 {
        return 2
    }

    fib := make([]int, n+1)
    fib[0], fib[1], fib[2], fib[3] = 0, 0, 2, 0

    for i := 4; i <= n; i++ {
        fib[i] = fib[i-1] + fib[i-2] + fib[i-3] + fib[i-4]
    }

    return fib[n]
}
```

This solution initializes a slice `fib` with the first four elements of the Fib4 sequence. Then, it iterates from the 4th element to the n-th element and calculates each element based on the previous four elements in the sequence. Finally, it returns the n-th element of the Fib4 sequence.

The time complexity of this solution is O(n), where n is the input number. The space complexity is also O(n), as we are storing the previous results in a slice.