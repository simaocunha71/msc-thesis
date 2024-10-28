Here is a possible solution in Go:

```go
func PrimeLength(s string) bool {
    length := len(s)
    if length <= 1 {
        return false
    }
    for i := 2; i*i <= length; i++ {
        if length%i == 0 {
            return false
        }
    }
    return true
}
```

This function first checks if the length of the string is less than or equal to 1, in which case it returns `false` since a prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

Then, it uses a loop to check if the length is divisible by any number from 2 to the square root of the length. If it is, then the length is not a prime number and the function returns `false`.

If the function gets through the loop without finding a divisor, then the length is a prime number and the function returns `true`.