```go
func Factorize(n int) []int {
    factors := []int{}
    for i := 2; i <= int(math.Sqrt(float64(n))+1); i++ {
        for n%i == 0 {
            factors = append(factors, i)
            n = n / i
        }
    }
    if n > 1 {
        factors = append(factors, n)
    }
    return factors
}
```
