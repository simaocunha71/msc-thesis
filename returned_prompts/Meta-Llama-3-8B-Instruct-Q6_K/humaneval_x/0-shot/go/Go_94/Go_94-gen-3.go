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
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
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
    for _, num := range lst {
        if isPrime(num) && num > maxPrime {
            maxPrime = num
        }
    }
    return sumOfDigits(maxPrime)
}

func main() {
    lst := []int{0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3}
    fmt.Println(Skjkasdkd(lst))  // Output: 10
}
```
The function `Skjkasdkd` iterates over the input list and checks if each number is prime using the `isPrime` function. If a prime number is found and it's greater than the current maximum prime, it updates the maximum prime. Finally, it returns the sum of the digits of the maximum prime using the `sumOfDigits` function.

Note that this solution assumes that the input list contains only integers. If the list can contain non-integer values, you may need to add additional error handling. Also, this solution uses a simple trial division method to check for primality, which may not be efficient for very large numbers. For a more efficient solution, you may want to use a more advanced primality test, such as the Miller-Rabin primality test.