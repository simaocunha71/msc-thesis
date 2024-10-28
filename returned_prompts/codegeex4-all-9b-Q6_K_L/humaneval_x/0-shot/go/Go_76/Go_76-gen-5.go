You can use the following code to solve the problem:

```go
func IsSimplePower(x, n int) bool {
    if n == 1 {
        return x == 1
    }
    if x%n != 0 {
        return false
    }
    return IsSimplePower(x/n, n)
}
```

The code works by recursively checking if `x` is a simple power of `n`. If `n` is 1, the function returns `true` if `x` is also 1. If `x` is not divisible by `n`, the function returns `false`. Otherwise, the function recursively calls itself with `x/n` and `n` as the new arguments until `x` is 1 or `n` is 1.