```go
package main

import (
    "fmt"
)

func SpecialFactorial(n int) int {
    result := 1
    for i := 1; i <= n; i++ {
        factorial := 1
        for j := 1; j <= i; j++ {
            factorial *= j
        }
        result *= factorial
    }
    return result
}

func main() {
    fmt.Println(SpecialFactorial(4))  // prints 288
}
```

Explanation:
The function `SpecialFactorial(n int)` calculates the Brazilian factorial of the input integer `n`. It does this by iterating from `1` to `n`, and for each `i`, it calculates the factorial of `i` and multiplies the result with the previous result. The final result is the Brazilian factorial of `n`.

In the `main` function, we call `SpecialFactorial(4)` and print the result, which is `288`. This is the expected output for the Brazilian factorial of `4`.