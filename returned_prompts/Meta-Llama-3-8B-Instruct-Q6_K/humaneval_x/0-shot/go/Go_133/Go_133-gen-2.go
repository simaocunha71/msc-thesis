Here is the solution in Go:

```go
import (
    "math"
    "math/cmath"
)

func SumSquares(lst []float64) int {
    var sum int
    for _, num := range lst {
        // round each element in the list to the upper int(Ceiling)
        rounded := math.Ceil(num)
        sum += int(math.Pow(float64(rounded), 2))
    }
    return sum
}
```

This function iterates over the input list, rounds each number to the upper integer using the math.Ceil function, squares the rounded number using the math.Pow function, and adds the result to a running sum. The sum is then returned as an integer. The math.Pow function returns a float64, so we need to convert the result to an int using the int function. If the original number is negative, the rounded number will also be negative, so the squared result will be positive. This is why we don't need to worry about the sign of the original number. The math.Ceil function returns a float64, so we need to convert the result to an int using the int function. The int function truncates the decimal part, so we get the upper integer. For example, math.Ceil(1.4) returns 2.0, and int(2.0) returns 2. Similarly, math.Ceil(-2.4) returns -2.0, and int(-2.0) returns -2. The math.Pow function returns a float64, so we need to convert the result to an int using the int function. The int function truncates the decimal part, so we get the squared result as an integer. For example, math.Pow(2.0, 2.0) returns 4.0, and int(4.0) returns 4. Similarly, math.Pow(-2.0, 2.0) returns 4.0, and int(4.0) returns 4. The sum is then returned as an integer. The function can handle both positive and negative numbers, and the results will be the sum of the squares of the rounded numbers. The function can also handle non-integer numbers, and the results will be the sum of the squares of the rounded numbers. For example, if the input list is [1.4, 4.2, 0], the function will return 29, which is the sum of the squares of the rounded numbers. If the