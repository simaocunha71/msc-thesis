```go
func Factorize(n int) []int {
    if n < 2 {
        return []int{}
    }

    factors := []int{}
    for i := 2; i <= n; i++ {
        if n%i == 0 {
            factors = append(factors, i)
            n /= i
            i--
        }
    }

    return factors
}
```
