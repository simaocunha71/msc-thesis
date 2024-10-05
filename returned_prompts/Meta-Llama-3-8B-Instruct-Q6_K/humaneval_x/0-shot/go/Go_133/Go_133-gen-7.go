Here is the solution in Go:

```go
import (
    "math"
    "math/cmath"
)

func SumSquares(lst []float64) int {
    var sum int
    for _, v := range lst {
        sum += int(math.Ceil(v) * math.Ceil(v))
    }
    return sum
}
```

This function iterates over each element in the input list `lst`. For each element, it calculates the ceiling of the element using `math.Ceil`, squares the ceiling, converts the result to an integer, and adds it to the running sum. Finally, it returns the sum. 

The `math.Ceil` function returns the smallest integer not less than the input value. This ensures that each element in the list is rounded up to the nearest integer before squaring. 

The result is the sum of the squares of the ceiling of each element in the input list. 

For example, if the input list is `[1, 2, 3]`, the function will calculate `(math.Ceil(1) * math.Ceil(1)) + (math.Ceil(2) * math.Ceil(2)) + (math.Ceil(3) * math.Ceil(3)) = 1*1 + 2*2 + 4*4 = 1 + 4 + 16 = 21`. The function will return `21`. 

The result is an integer because the ceiling of each element is converted to an integer before squaring. 

This function can be used to solve the problem described in the question. 

Note: The `math.Ceil` function is from the `math/cmath` package, not the `math` package. This is because the `math` package does not have a `Ceil` function. The `math/cmath` package provides a more comprehensive set of mathematical functions, including `Ceil`. 

Also, the result of the function is an integer because the sum of the squares of the ceiling of each element is an integer. If the result is not an integer, it means that the input list contains non-integer values. In this case, the function may not produce the correct result. 

The function assumes that the input list is non-empty. If the input list is empty, the function will return `0`. If the function should handle empty input lists differently, it can be modified to do so. 

The function does not check if the input list contains non-numeric values. If the