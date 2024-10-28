```go
func Factorize(n int) []int {
    factors := []int{}
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n%i == 0 {
            factors = append(factors, i)
            n /= i
            i--
        }
    }
    if n > 1 {
        factors = append(factors, n)
    }
    return factors
}
```

Explanation:
1. Initialize an empty slice `factors` to store the prime factors.
2. Iterate from 2 to the square root of `n` (inclusive).
3. If `n` is divisible by `i`, add `i` to the `factors` slice, divide `n` by `i`, and decrement `i` by 1 to ensure that we check the same number again (in case it is a factor multiple times).
4. If `n` is greater than 1 after the loop, it means that `n` itself is a prime number, so add it to the `factors` slice.
5. Return the `factors` slice.