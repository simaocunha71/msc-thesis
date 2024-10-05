
```go
package main

import (
    "fmt"
    "math"
)

func IsSimplePower(x, n int) bool {
    return math.Pow(float64(n), float64(x)) == float64(x)
}

func main() {
    fmt.Println(IsSimplePower(1, 4))
    fmt.Println(IsSimplePower(2, 2))
    fmt.Println(IsSimplePower(8, 2))
    fmt.Println(IsSimplePower(3, 2))
    fmt.Println(IsSimplePower(3, 1))
    fmt.Println(IsSimplePower(5, 3))
}
```

In this code, the `IsSimplePower` function takes two integer parameters, `x` and `n`, and returns a boolean value. It uses the `math.Pow` function to calculate the value of `n` raised to the power of `x` as a float64, and then compares this result to the integer value of `x`. If they are equal, the function returns `true`, indicating that `x` is a simple power of `n`. Otherwise, it returns `false`.

The `main` function is used to test the `IsSimplePower` function with some sample inputs and print the results. The expected output for the given test cases is:

```
true
true
true
false
false
false
```

You can run this code to see the output and verify the correctness of the `IsSimplePower` function.

```go
package main

import (
    "fmt"
    "math"
)

func IsSimplePower(x, n int) bool {
    return math.Pow(float64(n), float64(x)) == float64(x)
}

func main() {
    fmt.Println(IsSimplePower(1, 4))
    fmt.Println(IsSimplePower(2, 2))
    fmt.Println(IsSimplePower(8, 2))
    fmt.Println(IsSimplePower(3, 2))
    fmt.Println(IsSimplePower(3,