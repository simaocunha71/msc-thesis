
// Here is a possible solution in Go:

```go
func Fibfib(n int) int {
    if n < 2 {
        return 0
    }
    if n == 2 {
        return 1
    }

    a, b, c := 0, 0, 1
    for i := 3; i <= n; i++ {
        a, b, c = b, c, a+b+c
    }
    return c
}
```

This function uses a simple loop to compute the n-th Fibfib number. It uses three variables `a, b, c` to hold the last three numbers of the sequence. In each iteration of the loop, it updates `a, b, c` to the last two elements and the next element of the sequence.

The time complexity of this function is O(n) and the space complexity is O(1), which makes it quite efficient.

This function can be used to compute the n-th Fibfib number for any non-negative integer n.
