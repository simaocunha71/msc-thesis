```go
func PrimeFib(n int) int {
    fib := 0
    a, b := 0, 1
    for i := 1; i <= n; i++ {
        fib = a + b
        a, b = b, fib
        if isPrime(fib) {
            return fib
        }
    }
    return -1
}

func isPrime(num int) bool {
    if num <= 1 {
        return false
    }
    for i := 2; i <= int(math.Sqrt(float64(num))); i++ {
        if num%i == 0 {
            return false
        }
    }
    return true
}
```
In this solution, we generate Fibonacci numbers using a loop, and for each generated number, we check if it's prime using the `isPrime` function. If it is, we return that number. If we reach the `n-th` number without finding a prime one, we return -1. The `isPrime` function checks if a number is prime by checking if it has any divisors other than 1 and itself. It does this by iterating up to the square root of the number and checking if the number is divisible by any of the values in that range. If it is, it's not prime, so we return false. If we reach the end of the loop without finding a divisor, the number is prime, so we return true.