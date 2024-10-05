```go
func CountUpTo(n int) []int {
    primes := make([]int, 0)
    for i := 2; i < n; i++ {
        isPrime := true
        for j := 2; j < i; j++ {
            if i%j == 0 {
                isPrime = false
                break
            }
        }
        if isPrime {
            primes = append(primes, i)
        }
    }
    return primes
}
```
