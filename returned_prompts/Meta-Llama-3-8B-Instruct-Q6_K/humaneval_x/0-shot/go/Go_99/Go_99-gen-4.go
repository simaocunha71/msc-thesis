Here is a solution for the problem:

```go
package main

import (
    "math"
    "strconv"
    "strings"
)

func ClosestInteger(value string) int {
    num, err := strconv.ParseFloat(value, 64)
    if err != nil {
        panic(err)
    }

    intVal := int(math.Round(float64(num)))
    if math.Abs(float64(num)-float64(intVal)) == math.Abs(float64(num)-float64(intVal-1)) {
        if intVal > 0 {
            return intVal - 1
        } else {
            return intVal + 1
        }
    }
    return intVal
}

func main() {
    println(ClosestInteger("10"))  // Output: 10
    println(ClosestInteger("15.3")) // Output: 15
}
```

This program first parses the input string into a floating point number. It then rounds this number to the nearest integer using the `math.Round` function. If the input number is equidistant from two integers, it checks whether the original number is positive or negative. If it's positive, it rounds down (i.e., returns the smaller integer), and if it's negative, it rounds up (i.e., returns the larger integer). Finally, it returns the rounded integer value. The `main` function demonstrates the usage of the `ClosestInteger` function.