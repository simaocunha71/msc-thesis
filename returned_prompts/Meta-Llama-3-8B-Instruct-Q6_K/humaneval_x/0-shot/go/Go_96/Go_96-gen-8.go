```go
package main

import (
    "fmt"
    "math"
)

func isPrime(num int) bool {
    if num < 2 {
        return false
    }
    for i := 2; i <= int(math.Sqrt(float64(num))); i++ {
        if num%i == 0 {
            return false
        }
    }
    return true
}

func CountUpTo(n int) []int {
    var primes []int
    for i := 2; i < n; i++ {
        if isPrime(i) {
            primes = append(primes, i)
        }
    }
    return primes
}

func main() {
    fmt.Println(CountUpTo(5))  // [2,3]
    fmt.Println(CountUpTo(11)) // [2,3,5,7]
    fmt.Println(CountUpTo(0))  // []
    fmt.Println(CountUpTo(20)) // [2,3,5,7,11,13,17,19]
    fmt.Println(CountUpTo(1))  // []
    fmt.Println(CountUpTo(18)) // [2,3,5,7,11,13,17]
}
```

Explanation:
The provided Go code defines a function `CountUpTo` that takes an integer `n` as input and returns a slice of prime numbers less than `n`. The function uses a helper function `isPrime` to check whether a given integer is prime or not.

The `isPrime` function iterates from 2 to the square root of the input number and checks if the number is divisible by any of these values. If it is, the function returns `false`, indicating that the number is not prime. If the number is not divisible by any of these values, the function returns `true`, indicating that the number is prime.

The `CountUpTo` function iterates from 2 to `n-1` and checks each number using the `isPrime` function. If the number is prime, it is added to the slice of prime numbers. Finally, the function returns the slice of prime numbers.

In the `main` function, the `CountUpTo` function is called with different input values and the resulting slices of prime numbers are printed to the console. The output matches the expected results.