```go
func IsMultiplyPrime(a int) bool {
    primeFactors := primeFactors(a)
    if len(primeFactors) == 3 {
        return true
    }
    return false
}

func primeFactors(n int) []int {
    factors := []int{}
    for i := 2; i <= n; i++ {
        if n%i == 0 {
            factors = append(factors, i)
            n = n / i
            i--
        }
    }
    return factors
}
```