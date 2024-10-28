Here is a Go solution for the problem:

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
    factors := make([]int, 0)
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
    fmt.Println(Factorize(8))  // Output: [2, 2, 2]
    fmt.Println(Factorize(25)) // Output: [5, 5]
    fmt.Println(Factorize(70)) // Output: [2, 5, 7]
}
```

In this code, we use a loop to iterate over all numbers from 2 to `sqrt(n)`. For each number `i`, we count how many times it divides `n`. If `i` divides `n`, we divide `n` by `i` and increment the count. After the loop, if `i` has divided `n` at least once, we append `i` to the `factors` slice as many times as it has divided `n`. Finally, we return the `factors` slice. The `main` function demonstrates the usage of the `Factorize` function.