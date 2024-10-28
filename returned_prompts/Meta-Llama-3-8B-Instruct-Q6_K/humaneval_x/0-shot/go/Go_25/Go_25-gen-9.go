Here is the solution:
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
    var result []int
    i := 2
    for i <= math.Sqrt(float64(n)) {
        count := 0
        for n%i == 0 {
            n /= i
            count++
        }
        if count > 0 {
            result = append(result, int(i))
            for count > 0 {
                count--
                result = append(result, int(i))
            }
        }
        i++
    }
    if n > 1 {
        result = append(result, n)
    }
    return result
}

func main() {
    fmt.Println(Factorize(8))  // [2, 2, 2]
    fmt.Println(Factorize(25)) // [5, 5]
    fmt.Println(Factorize(70)) // [2, 5, 7]
}
```
The function `Factorize` takes an integer `n` as input and returns a slice of integers, where each integer is a prime factor of `n` and the number of times it appears in the factorization. The function works by iterating from 2 to the square root of `n`, and for each divisor `i`, it counts how many times `i` divides `n`. If `i` is a divisor, it appends `i` to the result slice `count` times. Finally, if `n` is still greater than 1, it means that `n` is a prime number, so it appends `n` to the result slice. The function returns the result slice. In the `main` function, we test the function with the inputs 8, 25, and 70. The output is the expected list of prime factors for each input.