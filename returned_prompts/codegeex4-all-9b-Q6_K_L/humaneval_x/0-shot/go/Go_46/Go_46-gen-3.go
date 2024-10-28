You can use dynamic programming to solve this problem. Create an array of size n+1 to store the Fib4 numbers. Initialize the first four elements of the array with the given values. Then, use a loop to calculate the remaining Fib4 numbers by adding the previous four numbers in the array.

Here is the modified code:

```go
func Fib4(n int) int {
    if n < 2 {
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

This solution has a time complexity of O(n) and a space complexity of O(n).