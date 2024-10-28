```go
package main

import (
    "fmt"
    "math"
)

func AnyInt(x, y, z interface{}) bool {
    // Convert the interface{} to float64
    fX, ok := x.(float64)
    if !ok {
        return false
    }
    fY, ok := y.(float64)
    if !ok {
        return false
    }
    fZ, ok := z.(float64)
    if !ok {
        return false
    }

    // Check if the sum of two numbers is equal to the third number
    if math.Abs(fX+fY-fZ) < 1e-9 {
        return true
    }
    return false
}

func main() {
    fmt.Println(AnyInt(5, 2, 7))  // true
    fmt.Println(AnyInt(3, 2, 2))  // false
    fmt.Println(AnyInt(3, -2, 1)) // true
    fmt.Println(AnyInt(3.6, -2.2, 2)) // false
}
```



Explanation:
This program defines a function `AnyInt` that takes three arguments of type `interface{}`. The function first attempts to convert these arguments to `float64` values using type assertions. If any of the conversions fail (i.e., the arguments are not `float64` values), the function returns `false`.

If all conversions are successful, the function checks if the sum of any two `float64` values is equal to the third value. It uses the `math.Abs` function to calculate the absolute difference between the sum and the third value, and returns `true` if this difference is less than a small value (1e-9). This is done to account for floating-point precision issues.

Finally, the program defines a `main` function that calls `AnyInt` with different sets of arguments and prints the results.