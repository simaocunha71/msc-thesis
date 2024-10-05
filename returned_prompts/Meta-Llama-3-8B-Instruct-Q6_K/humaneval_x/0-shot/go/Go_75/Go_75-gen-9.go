```go
func IsMultiplyPrime(a int) bool {
    // Check if the number is less than 1
    if a < 1 {
        return false
    }
    // Find the prime factors of the number
    factors := make([]int, 0)
    for i := 2; i <= a; i++ {
        for a%i == 0 {
            factors = append(factors, i)
            a /= i
        }
    }
    // Check if the number of prime factors is 3
    if len(factors) != 3 {
        return false
    }
    // Check if all the prime factors are prime numbers
    for _, factor := range factors {
        if !isPrime(factor) {
            return false
        }
    }
    return true
}

func isPrime(n int) bool {
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
Z:


Suggested solution:

Here is a possible solution in Go:
```go
package main

import (
    "fmt"
)

func isPrime(n int) bool {
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

func isMultiplyPrime(a int) bool {
    factors := make([]int, 0)
    for i := 2; i <= a; i++ {
        for a%i == 0 {
            factors = append(factors, i)
            a /= i
        }
    }
    if len(factors) != 3 {
        return false
    }
    for _, factor := range factors {
        if !isPrime(factor) {
            return false
        }
    }
    return true
}

func main() {
    fmt.Println(isMultiplyPrime(30)) // Output: true
    fmt.Println(isMultiplyPrime(31)) // Output: false
}
```
Explanation:

The `isPrime` function checks whether a given number is prime. It does this by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is, the function returns false. If it's not divisible by any of these values