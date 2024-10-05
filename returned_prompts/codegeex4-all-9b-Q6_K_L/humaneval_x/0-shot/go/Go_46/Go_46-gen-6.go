To efficiently compute the n-th element of the Fib4 number sequence, you can use a dynamic programming approach. This avoids the exponential time complexity of recursion and allows you to compute the sequence in linear time.

Here's a solution in Go:

```go
func Fib4(n int) int {
    // Handle the base cases
    if n == 0 || n == 1 {
        return 0
    }
    if n == 2 {
        return 2
    }
    if n == 3 {
        return 0
    }

    // Initialize the first four elements of the sequence
    fib := make([]int, n+1)
    fib[0], fib[1], fib[2], fib[3] = 0, 0, 2, 0

    // Compute the Fib4(n) using the relation Fib4(n) = Fib4(n-1) + Fib4(n-2) + Fib4(n-3) + Fib4(n-4)
    for i := 4; i <= n; i++ {
        fib[i] = fib[i-1] + fib[i-2] + fib[i-3] + fib[i-4]
    }

    // Return the n-th element of the sequence
    return fib[n]
}
```

This function initializes the first four elements of the sequence and then iteratively computes each subsequent element using the given relation. The function returns the n-th element of the sequence.

Here are some example calls to the function:

```go
fmt.Println(Fib4(5)) // Output: 4
fmt.Println(Fib4(6)) // Output: 8
fmt.Println(Fib4(7)) // Output: 14
```