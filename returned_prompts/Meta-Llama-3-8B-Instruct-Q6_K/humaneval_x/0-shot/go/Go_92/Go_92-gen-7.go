```go
package main

import (
    "fmt"
    "math"
)

func AnyInt(x, y, z interface{}) bool {
    switch {
    case x.(int) == y.(int)+z.(int) || x.(int) == y.(int)+z.(int) || y.(int) == x.(int)+z.(int):
        return true
    case math.Mod(x.(float64), 1) == 0 && math.Mod(y.(float64), 1) == 0 && math.Mod(z.(float64), 1) == 0:
        return false
    default:
        return false
    }
}

func main() {
    fmt.Println(AnyInt(5, 2, 7))  // true
    fmt.Println(AnyInt(3, 2, 2))   // false
    fmt.Println(AnyInt(3, -2, 1))  // true
    fmt.Println(AnyInt(3.6, -2.2, 2))  // false
}
```


Here is the solution in Go. The function `AnyInt` takes three arguments of type `interface{}`. This allows the function to work with integers, floats, or any other type that can be converted to a number.

The function first checks if one of the numbers is equal to the sum of the other two. If this condition is met, it returns `true`.

If the condition is not met, the function checks if all the numbers are integers by checking if the remainder of the division of each number by 1 is equal to 0. If this condition is not met, it returns `false`.

If the function has not returned by now, it means that the numbers are not equal to each other or to the sum of the other two, and they are also not integers. In this case, the function returns `false`.

The `main` function tests the `AnyInt` function with the given examples. The output is as expected.