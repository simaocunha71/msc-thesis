The Fib4 number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:

Fib4(0) -> 0
Fib4(1) -> 0
Fib4(2) -> 2
Fib4(3) -> 0
Fib4(n) -> Fib4(n-1) + Fib4(n-2) + Fib4(n-3) + Fib4(n-4).

In order to compute the n-th element of the Fib4 number sequence efficiently, we can use a dynamic programming approach. We will initialize an array with the first four elements of the sequence and then use a loop to compute the remaining elements.

Here is the implementation in Go:

```go
func Fib4(n int) int {
    if n < 0 {
        return -1 // Invalid input
    }

    // Initialize the array with the first four elements of the sequence
    fib := make([]int, n+1)
    fib[0], fib[1], fib[2], fib[3] = 0, 0, 2, 0

    // Compute the remaining elements
    for i := 4; i <= n; i++ {
        fib[i] = fib[i-1] + fib[i-2] + fib[i-3] + fib[i-4]
    }

    return fib[n]
}
```

Let's test the function with the provided test cases:

```go
func main() {
    fmt.Println(Fib4(5)) // Output: 4
    fmt.Println(Fib4(6)) // Output: 8
    fmt.Println(Fib4(7)) // Output: 14
}
```

The function should return the correct output for all the test cases.