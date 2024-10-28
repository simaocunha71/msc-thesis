
```go
var a, b, c int

if n == 0 {
    return a
} else if n == 1 {
    return b
} else if n == 2 {
    return c
}

for i := 3; i <= n; i++ {
    a, b = b, c
    c = a + b + c
}

return c
```

Explanation:
This function first checks if the parameter is 0, 1, or 2, and returns the result directly. Then it enters a loop that computes the FibFib sequence until the desired value is reached.

```go
var a, b, c int

if n == 0 {
    return a
} else if n == 1 {
    return b
} else if n == 2 {
    return c
}
```

The first three values of the FibFib sequence are 0, 0, 1. In this part of the function, it checks if the parameter matches any of these values and returns the result directly. This saves time because the first three values of the FibFib sequence can be computed directly without the need for a loop.

```
for i := 3; i <= n; i++ {
    a, b = b, c
    c = a + b + c
}
```

This part of the function enters a loop that computes the FibFib sequence until the desired value is reached. It uses three variables to store the last three values of the sequence. In each iteration, it updates these values and calculates the next value of the sequence. When the loop ends, the variable c holds the n-th value of the sequence.

```go
return c
```

Finally, the function returns the result, which is the n-th value of the FibFib sequence.

```
```

```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
