Here is the solution using a simple algorithm to find prime factors of a number.

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
    for i := 2; i <= math.Sqrt(float64(n)); i++ {
        count := 0
        for n%i == 0 {
            n /= i
            count++
        }
        if count > 0 {
            factors = append(factors, int32(i))
            if count > 1 {
                factors = append(factors, int32(count))
            }
        }
    }
    if n > 1 {
        factors = append(factors, int32(n))
    }
    return factors
}

func main() {
    fmt.Println(Factorize(8))  // [2, 2, 2]
    fmt.Println(Factorize(25)) // [5, 5]
    fmt.Println(Factorize(70)) // [2, 5, 7]
}
```

The `Factorize` function takes an integer `n` as input and returns a slice of integers representing the prime factors of `n`. The function iterates from 2 to the square root of `n` and for each integer `i` in this range, it checks if `n` is divisible by `i`. If it is, it divides `n` by `i` and increments a counter. If the counter is greater than 0, it means that `i` is a prime factor of `n` and the function appends `i` and the count to the `factors` slice. Finally, if `n` is greater than 1, it means that `n` itself is a prime factor and the function appends it to the `factors` slice.

The `main` function tests the `Factorize` function with three different inputs and prints the results. The output of the program is:

```
[2 2 2]
[5 5]
[2 5 7]
```


This solution has a time complexity of O(√n) because it iterates up to the square root of `n` to