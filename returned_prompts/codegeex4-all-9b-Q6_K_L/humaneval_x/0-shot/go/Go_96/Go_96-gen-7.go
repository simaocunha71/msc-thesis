Here is a solution written in Go:

```go
func CountUpTo(n int) []int {
    if n <= 1 {
        return []int{}
    }
    primes := make([]int, 0, n)
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

This solution works by iterating over all numbers from 2 to n-1 and checking if each number is prime by dividing it by all numbers from 2 to its square root. If a number is divisible by any of these numbers, it is not prime and the loop breaks. If a number is not divisible by any of these numbers, it is prime and is added to the `primes` slice. The function then returns the `primes` slice.