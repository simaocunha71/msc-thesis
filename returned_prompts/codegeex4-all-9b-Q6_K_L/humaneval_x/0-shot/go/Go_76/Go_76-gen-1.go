Here is a simple solution in Go:

```go
func IsSimplePower(x, n int) bool {
    // If the number is 1, it's trivially a power of any number.
    if x == 1 {
        return true
    }

    // We start with n and keep multiplying it by itself until we either
    // reach x or exceed it.
    for i := 1; i < x; i++ {
        n *= x

        // If we reach x, it's a power.
        if n == x {
            return true
        }

        // If we exceed x, it's not a power.
        if n > x {
            return false
        }
    }

    // If we haven't returned yet, x isn't a power.
    return false
}
```
This solution works by repeatedly multiplying `n` by `x` until it either equals `x` (in which case it's a power) or exceeds `x` (in which case it's not a power). If `x` is 1, it's trivially a power of any number, so we return true in that case.