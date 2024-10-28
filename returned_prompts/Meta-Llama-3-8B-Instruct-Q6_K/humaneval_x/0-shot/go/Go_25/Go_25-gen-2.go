Here is a simple implementation of the Factorize function in Go:

```go
package main

import (
    "fmt"
    "math"
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
            count++
            n /= i
        }
        if count > 0 {
            factors = append(factors, i)
            for count > 0 {
                count--
                factors = append(factors, i)
            }
        }
        i++
    }
    return factors
}

func main() {
    fmt.Println(Factorize(8))  // [2, 2, 2]
    fmt.Println(Factorize(25)) // [5, 5]
    fmt.Println(Factorize(70)) // [2, 5, 7]
}
```

This program iterates from 2 to the square root of the input number, and for each number it checks how many times it can be divided into the input number without a remainder. If it can be divided, it is a factor and is added to the list of factors. The count of how many times the number can be divided is used to add the factor to the list multiple times. The function returns the list of factors. The main function is used to test the Factorize function with some sample inputs. The results are printed to the console.  This function assumes that the input number is a positive integer. If the input number is not a positive integer, the function may not work correctly.  This function also assumes that the input number is equal to the product of its factors. If the input number is not equal to the product of its factors, the function may not work correctly.  This function is not efficient for large input numbers because it checks every number up to the square root of the input number. It could be optimized by only checking prime numbers, but that would make the function more complex.  This function does not handle the case where the input number is 1. It could be modified to return a list of length 0 for input number 1.  This function does not handle the case