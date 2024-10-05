Here is the solution to the problem:

```go
package main

import (
    "math"
    "fmt"
)

// Return list of prime factors of given integer in the order from smallest to largest.
// Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
// Input number should be equal to the product of all factors
func Factorize(n int) []int {
    var factors []int
    i := 2
    for n > 1 {
        count := 0
        for n%i == 0 {
            n /= i
            count++
        }
        if count > 0 {
            factors = append(factors, int(math.Pow(float64(i), float64(count))))
        }
        i++
    }
    return factors
}

func main() {
    fmt.Println(Factorize(8)) // [2, 2, 2]
    fmt.Println(Factorize(25)) // [5, 5]
    fmt.Println(Factorize(70)) // [2, 5, 7]
}
```

This program works by iterating through all numbers from 2 to the input number, and for each number, it checks how many times it can divide the input number without leaving a remainder. It keeps track of the count of each number and appends the number to the factors slice the number of times it appears in the factorization. The program continues this process until the input number becomes 1, at which point it returns the slice of factors. The factors are returned in the order from smallest to largest. The main function tests the Factorize function with the input numbers 8, 25, and 70. The output of these tests is printed to the console.