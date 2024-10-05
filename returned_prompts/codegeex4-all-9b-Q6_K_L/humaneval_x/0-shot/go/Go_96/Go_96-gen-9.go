```go
func CountUpTo(n int) []int {
    primes := []int{}
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

This function takes an integer n and returns an array of the first n prime numbers that are less than n. It uses a nested loop to check if each number is prime, and if it is, it adds it to the primes array. Finally, it returns the primes array.