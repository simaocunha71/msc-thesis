Here is a possible solution in Go:

```go
package main

import "fmt"

func LargestPrimeFactor(n int) int {
    for i := 2; i <= n; i++ {
        if n%i == 0 {
            for n%i == 0 {
                n /= i
            }
            if i > LargestPrimeFactor(n) {
                return i
            }
        }
    }
    return n
}

func main() {
    fmt.Println(LargestPrimeFactor(13195)) // 29
    fmt.Println(LargestPrimeFactor(2048)) // 2
}
```

In the above code, the `LargestPrimeFactor` function is a recursive function that finds the largest prime factor of a given integer `n`. It starts by initializing a loop that iterates from 2 to `n`. For each `i` in the loop, it checks if `n` is divisible by `i`. If `n` is divisible by `i`, it divides `n` by `i` and continues to do so until `n` is no longer divisible by `i`. Then, it checks if `i` is greater than the largest prime factor of the remaining `n`. If `i` is greater, it returns `i` as the largest prime factor. If `i` is not greater, it continues the loop with the next `i`. If `n` is not divisible by any `i` in the loop, it returns `n` as the largest prime factor.

The `main` function is used to test the `LargestPrimeFactor` function with the given test cases.