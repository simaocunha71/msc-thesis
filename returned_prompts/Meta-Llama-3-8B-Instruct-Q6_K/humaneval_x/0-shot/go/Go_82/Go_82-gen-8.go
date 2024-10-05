```go
func PrimeLength(s string) bool {
    len := len(s)
    if len <= 1 {
        return false
    }
    for i := 2; i*i <= len; i++ {
        if len%i == 0 {
            return false
        }
    }
    return true
}
```
Explanation:
The function `PrimeLength` takes a string `s` as input and returns `true` if the length of the string is a prime number, and `false` otherwise.

First, we calculate the length of the string using `len(s)`.

Then, we check if the length is less than or equal to 1. If it is, we immediately return `false`, since the length of a string with 0 or 1 characters cannot be prime.

Next, we iterate from 2 to the square root of the length (inclusive). For each number `i` in this range, we check if the length is divisible by `i` using the modulo operator (`%`). If it is, we return `false`, since the length is not a prime number.

If we reach the end of the loop without finding a divisor, we return `true`, since the length is likely to be a prime number.

Note that we only need to check up to the square root of the length, since a larger factor of the length would imply the existence of a smaller factor. This optimization makes the function more efficient for larger input strings.