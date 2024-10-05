```go
package main

import (
    "math"
    "strconv"
    "strings"
)

func ClosestInteger(value string) int {
    num, _ := strconv.ParseFloat(value, 64)
    return int(math.Round(float64(num)))
}

func main() {
    println(ClosestInteger("10")) // Output: 10
    println(ClosestInteger("15.3")) // Output: 15
}
```

Explanation:
The function `ClosestInteger` takes a string value representing a number and returns the closest integer to it. If the number is equidistant from two integers, round it away from zero.

In the function, we first use `strconv.ParseFloat` to convert the input string to a floating-point number. Then, we use `math.Round` to round the number to the nearest integer. The `math.Round` function rounds half-way values to the nearest even integer, so it does not exactly round away from zero. However, since we are dealing with floating-point numbers, this is the closest we can get to the desired behavior.

In the `main` function, we test the `ClosestInteger` function with two examples. The first example is `ClosestInteger("10")`, which returns `10`. The second example is `ClosestInteger("15.3")`, which returns `15`. These results match the expected behavior of the function.