Here is a solution in Go:

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

This function uses a nested loop to check if each number from 2 to n-1 is prime. If the number is prime, it is appended to the primes slice. Finally, the primes slice is returned.

Note that this solution is not the most efficient way to find prime numbers. There are more efficient algorithms available, such as the Sieve of Eratosthenes. However, for the sake of simplicity, this solution is used here.