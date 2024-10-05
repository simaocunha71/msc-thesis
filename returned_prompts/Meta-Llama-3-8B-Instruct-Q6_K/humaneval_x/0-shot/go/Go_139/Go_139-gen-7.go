```go
package main

import (
    "fmt"
)

func SpecialFactorial(n int) int {
    result := 1
    for i := 1; i <= n; i++ {
        for j := i; j > 0; j-- {
            result *= int(float64(j))
        }
    }
    return result
}

func main() {
    fmt.Println(SpecialFactorial(4))  // Output: 288
}
```

Explanation:
The code defines a function `SpecialFactorial(n int)` that calculates the Brazilian factorial of a given integer `n`. The Brazilian factorial is defined as the product of all factorials from `n` down to `1`.

In the function, we initialize a variable `result` to `1` and then use two nested loops to calculate the product of all factorials. The outer loop iterates from `1` to `n`, and the inner loop iterates from `i` down to `1` for each iteration of the outer loop. In each iteration of the inner loop, we multiply the `result` by the current value `j`.

Finally, we return the calculated result.

In the `main` function, we call `SpecialFactorial(4)` and print the result, which is `288`. This is the correct result for the Brazilian factorial of `4`.