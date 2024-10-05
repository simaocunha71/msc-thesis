Here is the solution in Go:

```go
package main

import (
    "math"
    "strconv"
    "strings"
)

func ClosestInteger(value string) int {
    num, _ := strconv.ParseFloat(value, 64)
    if math.Abs(float64(int(num))) < math.Abs(float64(num)) {
        return int(num)
    } else {
        return int(math.Ceil(float64(num)))
    }
}

func main() {
    print(ClosestInteger("10"))  // 10
    print(ClosestInteger("15.3"))  // 15
    print(ClosestInteger("14.5"))  // 15
    print(ClosestInteger("-14.5"))  // -15
}
```

This solution first converts the input string to a float64 using `strconv.ParseFloat`. It then checks if the absolute value of the integer part of the number is less than the absolute value of the fractional part. If it is, it means the number is equidistant from two integers, and the integer part is the closest. Otherwise, it rounds the number away from zero by using `math.Ceil` to round up to the nearest integer. Finally, it converts the float64 to an int using `int()`. The result is the closest integer to the input value.