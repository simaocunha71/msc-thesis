To solve the problem of computing the n-th element of the Fibfib number sequence, we can use dynamic programming. The sequence is defined as follows:
- Fibfib(0) == 0
- Fibfib(1) == 0
- Fibfib(2) == 1
- Fibfib(n) == Fibfib(n-1) + Fibfib(n-2) + Fibfib(n-3)

We can use a cache to store the previously computed values to avoid redundant calculations. This approach ensures that each value is computed only once, resulting in an efficient solution.

Here's the implementation in Go:

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

Let's test the function with the provided test cases:

```go
func main() {
    fmt.Println(Fibfib(1)) // Output: 0
    fmt.Println(Fibfib(5)) // Output: 4
    fmt.Println(Fibfib(8)) // Output: 24
}
```

The function should return the expected results for the given test cases.