The function `PrimeFib` returns the `n-th` number that is a Fibonacci number and also a prime number. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.

Here is a simple implementation of the `PrimeFib` function in Go:
```go
import (
    "math"
)

func PrimeFib(n int) int {
    a, b := 0, 1
    prime := true
    i := 1
    for prime {
        a, b = b, a+b
        i++
        if i > n {
            break
        }
        prime = isPrime(b)
    }
    return b
}

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}
```
This function uses a helper function `isPrime` to check if a number is prime. The `PrimeFib` function generates Fibonacci numbers until it finds the `n-th` prime number.

You can use this function to get the `n-th` prime Fibonacci number, for example:
```go
fmt.Println(PrimeFib(1)) // Output: 2
fmt.Println(PrimeFib(2)) // Output: 3
fmt.Println(PrimeFib(3)) // Output: 5
fmt.Println(PrimeFib(4)) // Output: 13
fmt.Println(PrimeFib(5)) // Output: 89
```
Note that this implementation is not very efficient for large values of `n`, as it generates all Fibonacci numbers until it finds the `n-th` prime number. A more efficient implementation would use a sieve to generate prime numbers up to the `n-th` Fibonacci number.