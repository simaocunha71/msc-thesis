
```go
func Fibfib(n int) int {
    var f0, f1, f2 int = 0, 0, 1

    for i := 2; i <= n; i++ {
        f0, f1 = f1, f2
        f2 = f0 + f1 + f2
    }

    return f2
}
```

This function is a O(n) solution to the problem. It initializes three variables f0, f1 and f2 and computes the Fibonacci sequence in a loop. The for loop is the key point of the solution, which makes the function more efficient than a recursive function.

```go
for i := 2; i <= n; i++ {
    f0, f1 = f1, f2
    f2 = f0 + f1 + f2
}
```

The for loop is used to compute the Fibonacci sequence up to the n-th term. In each iteration, f0, f1 and f2 are updated. f2 is the sum of f0, f1 and f2.

```go
return f2
```

The function returns the n-th term of the Fibonacci sequence, f2.

```go
var f0, f1, f2 int = 0, 0, 1
```

This line initializes three variables f0, f1 and f2 with initial values 0, 0 and 1 respectively.
```
```

```go
func Fibfib(n int) int {

    var f0, f1, f2 int = 0, 0, 1

    for i := 2; i <= n; i++ {
        f0, f1 = f1, f2
        f2 = f0 + f1 + f2
    }

    return f2
}
```

Here is a function that efficiently computes the n-th element of the Fibfib number sequence. It initializes three variables f0, f1 and f2 with initial values 0, 0 and 1. Then, it uses a for loop to compute the Fib