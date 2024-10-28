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
    for _, c := range strconv.Itoa(n) {
        d, _ := strconv.Atoi(string(c))
        sum += d
    }
    return sum
}

func Skjkasdkd(lst []int) int {
    maxPrime := 0
    for _, n := range lst {
        if isPrime(n) && n > maxPrime {
            maxPrime = n
        }
    }
    return sumOfDigits(maxPrime)
}

func main() {
    lst := []int{0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3}
    fmt.Println(Skjkasdkd(lst)) // Output: 10
}
```


In this solution, we define three helper functions: `isPrime` to check if a number is prime, `sumOfDigits` to calculate the sum of the digits of a number, and `Skjkasdkd` to find the largest prime number in the list and return the sum of its digits.

In the `isPrime` function, we check if a number is less than or equal to 1, in which case it's not prime. Then we iterate from 2 to the square root of the number, and if the number is divisible by any of these values, it's not prime.

In the `sumOfDigits` function, we convert the number to a string, iterate over each character, convert it back to an integer, and add it to the sum.

In the `Skjkasdkd` function, we iterate over the list, checking if each number is prime and if it's greater than the current maximum prime. If it is, we update the maximum prime. Finally, we return the sum of the digits of the maximum prime.

In the `main` function, we test the `Skjkasdkd` function with the given list and print the result.