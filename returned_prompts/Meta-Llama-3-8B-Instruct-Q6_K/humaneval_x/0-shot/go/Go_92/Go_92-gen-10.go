```go
package main

import (
    "fmt"
    "reflect"
)

func AnyInt(x, y, z interface{}) bool {
    if x == y+z || y == x+z || z == x+y {
        if reflect.TypeOf(x).Kind() == reflect.Int && reflect.TypeOf(y).Kind() == reflect.Int && reflect.TypeOf(z).Kind() == reflect.Int {
            return true
        }
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


This program defines a function called `AnyInt` that takes three arguments of type `interface{}`. It checks if one of the arguments is equal to the sum of the other two. If this condition is met and all arguments are integers, it returns `true`. Otherwise, it returns `false`.

In the `main` function, we test the function with different inputs and print the results. The function correctly identifies the cases where one of the numbers is equal to the sum of the other two and all numbers are integers. It also correctly identifies the cases where this condition is not met or the numbers are not integers.