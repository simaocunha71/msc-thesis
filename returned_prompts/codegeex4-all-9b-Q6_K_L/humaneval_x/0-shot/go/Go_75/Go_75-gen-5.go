```go
func IsMultiplyPrime(a int) bool {
    factors := make(map[int]bool)
    for i := 2; i <= a; i++ {
        if a%i == 0 {
            factors[i] = true
            for a%i == 0 {
                a = a / i
            }
        }
    }
    if len(factors) != 3 {
        return false
    }
    for k := range factors {
        if !isPrime(k) {
            return false
        }
    }
    return true
}

func isPrime(num int) bool {
    if num <= 1 {
        return false
    }
    for i := 2; i*i <= num; i++ {
        if num%i == 0 {
            return false
        }
    }
    return true
}
```
