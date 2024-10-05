```go
func LargestPrimeFactor(n int) int {
    factor := 2
    for factor*factor <= n {
        if n%factor == 0 {
            n = n / factor
        } else {
            factor++
        }
    }
    return n
}
```
