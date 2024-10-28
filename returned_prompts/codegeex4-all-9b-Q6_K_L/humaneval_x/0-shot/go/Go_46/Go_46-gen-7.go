You can use dynamic programming to solve this problem. Here's a solution in Go:

```go
func Fib4(n int) int {
    if n == 0 || n == 1 {
        return 0
    }
    if n == 2 {
        return 2
    }
    if n == 3 {
        return 0
    }
    fib := make([]int, n+1)
    fib[0], fib[1], fib[2], fib[3] = 0, 0, 2, 0
    for i := 4; i <= n; i++ {
        fib[i] = fib[i-1] + fib[i-2] + fib[i-3] + fib[i-4]
    }
    return fib[n]
}
```

This solution has a time complexity of O(n) and a space complexity of O(n).