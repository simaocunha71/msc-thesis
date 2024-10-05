The largest prime factor of a number is the largest prime number that divides the given number. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

Here's a solution in Go:

```go
func LargestPrimeFactor(n int) int {
    factor := 2
    for n > 1 {
        if n%factor == 0 {
            n /= factor
        } else {
            factor++
        }
    }
    return factor
}
```

This solution works by dividing the input number `n` by the current factor `factor`. If `n` is divisible by `factor`, it means that `factor` is a prime factor of `n`, so we divide `n` by `factor` and continue the loop. If `n` is not divisible by `factor`, we increment `factor` by 1 and continue the loop. The loop continues until `n` becomes 1, at which point `factor` is the largest prime factor of the original input number.

Let's test the solution with the provided examples:

```go
fmt.Println(LargestPrimeFactor(13195)) // Output: 29
fmt.Println(LargestPrimeFactor(2048))  // Output: 2
```

Both examples return the expected output.