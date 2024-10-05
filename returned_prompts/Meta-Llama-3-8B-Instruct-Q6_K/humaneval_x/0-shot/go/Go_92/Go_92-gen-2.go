```go
package main

import (
    "fmt"
    "math"
)

func AnyInt(x, y, z interface{}) bool {
    // Convert the interface{} to int
    xInt, ok := x.(int)
    if !ok {
        return false
    }
    yInt, ok := y.(int)
    if !ok {
        return false
    }
    zInt, ok := z.(int)
    if !ok {
        return false
    }

    // Check if one of the numbers is equal to the sum of the other two
    if xInt+yInt == zInt || xInt+zInt == yInt || yInt+zInt == xInt {
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

1.  We define a function `AnyInt` that takes three arguments `x`, `y`, and `z` of type `interface{}`.
2.  We use type assertions to convert the `interface{}` to `int`. If the conversion fails, we return `false`.
3.  We then check if one of the numbers is equal to the sum of the other two using simple arithmetic operations. If the condition is true, we return `true`.
4.  If none of the above conditions are met, we return `false`.

In the `main` function, we test the `AnyInt` function with various input combinations. The output should be `true` for the first two cases and `false` for the last two cases.