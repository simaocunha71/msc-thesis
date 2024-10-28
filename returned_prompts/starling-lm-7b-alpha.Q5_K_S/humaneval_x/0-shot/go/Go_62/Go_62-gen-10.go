
To derive a polynomial, you multiply each term by its corresponding power of x and then reduce the power of x by one. For example, if we have a polynomial 3 + 1*x + 2*x^2, its derivative will be 1*x^0 + 2*2*x^1 + 0*x^2. Here's how you can implement this:

```go
func Derivative(xs []int) []int {
    result := make([]int, len(xs)-1)
    for i := 0; i < len(xs)-1; i++ {
        result[i] = xs[i+1] * (i + 1)
    }
    return result
}
```

Here's an example of how you can test this function:

```go
fmt.Println(Derivative([]int{3, 1, 2, 4, 5}))  // [1, 4, 12, 20]
fmt.Println(Derivative([]int{1, 2, 3}))       // [2, 6]
```

This will output:

```
[1, 4, 12, 20]
[2, 6]
```

This is the expected result as explained above.

```go
```

```
```

```go
```

```go
```

```go
```

```go
```

```go
```

```go
```

```go
```

```go
```

```go
```
```

```go
```

```go
```
```

```go
```

```go
```

```go
```
```

```go
```
```

```go
```
```

```go
```

```go
```
```
```
```
```

```go
```
```

```go
