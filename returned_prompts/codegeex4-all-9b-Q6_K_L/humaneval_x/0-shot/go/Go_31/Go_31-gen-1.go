Here is the Go code to check if a number is prime or not:

```go
func IsPrime(n int) bool {
    if n <= 1 {
        return false
    }

    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }

    return true
}
```

This function works by checking if the given number is divisible by any number from 2 to the square root of the number. If the number is divisible by any of these numbers, it is not a prime number. Otherwise, it is a prime number.