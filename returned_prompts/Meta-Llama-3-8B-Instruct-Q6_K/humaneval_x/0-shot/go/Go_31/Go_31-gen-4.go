```go
func IsPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i * i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}
```

Explanation:

*   We start by checking if the number `n` is less than or equal to 1. If it is, we immediately return `false` because prime numbers are greater than 1.
*   We then use a `for` loop to iterate from 2 to the square root of `n`. This is because a larger factor of `n` would be a multiple of smaller factor that has already been checked.
*   Inside the loop, we check if `n` is divisible by the current number `i` using the modulo operator (`%`). If `n` is divisible by `i`, we return `false` because `n` is not a prime number.
*   If the loop completes without finding a divisor, we return `true` because `n` is a prime number. This is because a prime number has no divisors other than 1 and itself.