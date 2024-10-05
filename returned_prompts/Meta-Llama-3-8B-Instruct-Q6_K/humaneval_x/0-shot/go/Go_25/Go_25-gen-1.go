Here is the solution:
```go
import (
    "math"
)

func Factorize(n int) []int {
    var factors []int
    for i := 2; i <= math.Sqrt(float64(n)); i++ {
        count := 0
        for n%i == 0 {
            n = n / i
            count++
        }
        if count > 0 {
            factors = append(factors, int(math.Pow(float64(i), float64(count))))
        }
    }
    if n > 1 {
        factors = append(factors, n)
    }
    return factors
}
```
This function works by iterating through all numbers from 2 to the square root of the input number `n`. For each number `i`, it checks how many times `i` divides `n` and appends the result to the `factors` slice. Finally, if `n` is still greater than 1, it means that `n` is a prime number, so we append it to the `factors` slice.

For example, when `n` is 8, the function will iterate through 2, 3, and 4, and find that 2 divides 8 three times, so it appends [2, 2, 2] to the `factors` slice. When `n` is 25, the function will iterate through 2, 3, 4, ..., 5, and find that 5 divides 25 twice, so it appends [5, 5] to the `factors` slice. When `n` is 70, the function will iterate through 2, 3, 4, ..., 7, and find that 2 divides 70 once, 5 divides 70 once, and 7 divides 70 once, so it appends [2, 5, 7] to the `factors` slice.