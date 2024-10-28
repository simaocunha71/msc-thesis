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
The code checks if a given number is prime or not. If the number is less than or equal to 1, it returns false as they are not prime numbers. Then it iterates from 2 to the square root of the number to check if the number is divisible by any of these values. If it finds a divisor, it returns false. If it doesn't find any divisors, it returns true. This is because a prime number has no divisors other than 1 and itself. 

This function is efficient because it only needs to check up to the square root of the number, not the number itself. This is because a larger factor of the number would be a multiple of a smaller factor that has already been checked. 

This function also handles the edge cases of 1 and 2, which are not considered prime numbers in mathematics. 

This function can be further optimized by using a more efficient algorithm, such as the Miller-Rabin primality test, which is more suitable for large numbers. However, for small to medium-sized numbers, this function should be sufficient. 