Here is the solution in Go:
```go
package main

import (
    "math"
    "strconv"
)

func Skjkasdkd(lst []int) int {
    var maxPrime int
    for _, v := range lst {
        if isPrime(v) && v > maxPrime {
            maxPrime = v
        }
    }
    return sumOfDigits(maxPrime)
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

func sumOfDigits(n int) int {
    sum := 0
    for _, c := range strconv.Itoa(n) {
        digit, _ := strconv.Atoi(string(c))
        sum += digit
    }
    return sum
}

func main() {
    lst := []int{0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3}
    result := Skjkasdkd(lst)
    println(result) // Output: 10
}
```
This code defines three functions: `Skjkasdkd`, `isPrime`, and `sumOfDigits`. The `Skjkasdkd` function iterates over the input list, finds the largest prime number, and returns the sum of its digits. The `isPrime` function checks whether a given number is prime, and the `sumOfDigits` function calculates the sum of the digits of a given number.

In the `main` function, we test the `Skjkasdkd` function with a sample input list and print the result. You can modify the input list to test the function with different inputs.