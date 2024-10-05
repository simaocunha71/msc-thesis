Here is the solution in Go:
```go
package main

import (
    "fmt"
    "math"
    "strconv"
)

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i <= math.Sqrt(float64(n)); i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}

func sumOfDigits(n int) int {
    sum := 0
    for n > 0 {
        digit := n % 10
        sum += digit
        n /= 10
    }
    return sum
}

func Skjkasdkd(lst []int) int {
    maxPrime := 0
    for _, v := range lst {
        if isPrime(v) && v > maxPrime {
            maxPrime = v
        }
    }
    return sumOfDigits(maxPrime)
}

func main() {
    lst := []int{0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3}
    fmt.Println(Skjkasdkd(lst)) // Output: 10
}
```
This program defines two helper functions: `isPrime` checks whether a number is prime, and `sumOfDigits` calculates the sum of the digits of a number. The main function `Skjkasdkd` iterates over the input list, finds the largest prime number, and returns the sum of its digits. In the `main` function, we test the `Skjkasdkd` function with a sample list and print the result.