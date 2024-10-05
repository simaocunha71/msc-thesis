Here is the solution to the problem:

```go
import (
    "math"
)

func Factorize(n int) []int {
    factors := make([]int, 0)
    i := 2
    for i <= math.Sqrt(float64(n)) {
        count := 0
        for n%i == 0 {
            count++
            n /= i
        }
        if count > 0 {
            factors = append(factors, int(i))
            for count > 0 {
                count--
                factors = append(factors, int(i))
            }
        }
        i++
    }
    if n > 1 {
        factors = append(factors, n)
    }
    return factors
}
```

This function takes an integer `n` as input and returns a slice of integers representing the prime factors of `n`. The factors are listed in the order from smallest to largest, and each factor is listed the number of times it appears in the factorization of `n`. If `n` is a prime number, the function returns a slice containing only `n`. If `n` is equal to 1, the function returns an empty slice. The function uses a loop to iterate over all integers from 2 to the square root of `n`, and for each integer `i`, it checks if `n` is divisible by `i`. If `n` is divisible by `i`, it means that `i` is a factor of `n`, and the function appends `i` to the slice of factors the number of times it appears in the factorization of `n`. Finally, the function returns the slice of factors.