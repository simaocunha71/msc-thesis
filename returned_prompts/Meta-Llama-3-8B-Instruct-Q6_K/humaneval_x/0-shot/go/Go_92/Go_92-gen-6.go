```
package main

import (
    "fmt"
    "math"
)

func AnyInt(x, y, z interface{}) bool {
    // Convert the input to float64
    fx, fy, fz := 0.0, 0.0, 0.0
    switch x.(type) {
        case int:
            fx = float64(x.(int))
        case float64:
            fx = x.(float64)
        default:
            return false
    }
    switch y.(type) {
        case int:
            fy = float64(y.(int))
        case float64:
            fy = y.(float64)
        default:
            return false
    }
    switch z.(type) {
        case int:
            fz = float64(z.(int))
        case float64:
            fz = z.(float64)
        default:
            return false
    }

    // Check if any of the numbers is equal to the sum of the other two
    if math.IsNaN(fx) || math.IsNaN(fy) || math.IsNaN(fz) {
        return false
    }
    if fx+fy == fz || fx+fz == fy || fy+fz == fx {
        return true
    }
    return false
}

func main() {
    fmt.Println(AnyInt(5, 2, 7)) // true
    fmt.Println(AnyInt(3, 2, 2)) // false
    fmt.Println(AnyInt(3, -2, 1)) // true
    fmt.Println(AnyInt(3.6, -2.2, 2)) // false
}
```


This solution first converts the input to float64 to ensure that all types of numbers can be compared. Then it checks if any of the numbers is equal to the sum of the other two. If a number is NaN (Not a Number), the function returns false. If no such number is found, the function returns false. Otherwise, it returns true.