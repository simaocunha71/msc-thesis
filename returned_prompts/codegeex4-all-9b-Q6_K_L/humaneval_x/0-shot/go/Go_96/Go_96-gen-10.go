Here is the GoLang solution:

```go
func CountUpTo(n int) []int {
    primes := []int{}
    for i := 2; i < n; i++ {
        isPrime := true
        for j := 2; j*j <= i; j++ {
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

This function works by iterating through all numbers from 2 to n-1 and checking if each number is a prime number. A number is considered prime if it is only divisible by 1 and itself. The function uses a nested loop to perform this check. If a number is found to be prime, it is appended to the `primes` slice. Finally, the `primes` slice is returned.