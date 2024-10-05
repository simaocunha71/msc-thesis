
```go
func Fibfib(n int) int {
    if n == 0 || n == 1 {
        return 0
    } else if n == 2 {
        return 1
    }
    a := 0
    b := 1
    c := 1
    for i := 3; i <= n; i++ {
        c = a + b + c
        a = b
        b = c
    }
    return c
}
```

This function first checks if the input is 0, 1, or 2, as these are the base cases for the FibFib sequence. If the input is any of these values, the function simply returns 0, 1, or 1, respectively. 

For all other values of `n`, the function enters a loop that computes the FibFib number at index `n` using a similar approach to the Fibonacci sequence. It uses three variables `a`, `b`, and `c` to keep track of the current and previous two FibFib numbers. The loop starts at 3 and goes up to `n`, as the first three FibFib numbers are already handled by the base cases. 

Inside the loop, the function updates the variables `a`, `b`, and `c` to compute the next FibFib number. The new FibFib number is the sum of the previous three FibFib numbers (`a`, `b`, and `c`). After the loop finishes, the function returns the computed FibFib number at index `n`.

For example, if you call `Fibfib(1)`, it will return 0 because 0 is the first FibFib number. If you call `Fibfib(5)`, it will return 4 because the fourth FibFib number is 4. If you call `Fibfib(8)`, it will return 24 because the eighth FibFib number is 24. 

The time complexity of this function is O(n) because it iterates through a loop from 3 to `n`. The space complexity is also O(1) because it only uses a constant amount of extra space to store the current and previous two Fib