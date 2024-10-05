Here is a solution in Go:
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
    sum := 0
    for _, c := range strconv.Itoa(maxPrime) {
        sum += int(c - '0')
    }
    return sum
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

func main() {
    lst := []int{0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3}
    result := Skjkasdkd(lst)
    println(result) // Output: 10
}
```
This code defines two helper functions: `isPrime` checks if a given number is prime, and `Skjkasdkd` finds the largest prime number in the list and returns the sum of its digits. The `Skjkasdkd` function iterates over the list, checks each number if it's prime, and updates the `maxPrime` variable if it finds a larger prime number. Then it converts the `maxPrime` number to a string, iterates over each character, converts it back to an integer, and sums them up. The `main` function demonstrates how to use the `Skjkasdkd` function with a sample list.