```go
func PrimeLength(s string) bool {
    n := len(s)
    if n == 1 {
        return true
    }
    for i := 2; i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}
```
Explanation:

The function `PrimeLength` takes a string `s` as input and returns `true` if the length of the string is a prime number, and `false` otherwise.

The function first checks if the length of the string is 1, in which case it returns `true` because 1 is considered a prime number.

Then, it iterates from 2 to the length of the string `n` and checks if `n` is divisible by any of the numbers in this range. If it is, it returns `false` because `n` is not a prime number.

If the function does not find any divisors in this range, it returns `true` because `n` is a prime number.

Note that this function is not efficient for large strings because it checks divisibility up to the length of the string, which can be slow. For larger strings, a more efficient algorithm would be needed.