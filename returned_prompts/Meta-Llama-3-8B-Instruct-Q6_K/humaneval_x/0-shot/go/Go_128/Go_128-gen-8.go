Here is the solution in Go:
```go
import (
    "math"
)

func ProdSigns(arr []int) interface{} {
    if len(arr) == 0 {
        return nil
    }
    var sign int
    var sum float64
    for _, num := range arr {
        sign *= int(math.Signfloat64(float64(num)))
        sum += math.Abs(float64(num))
    }
    return sum * float64(sign)
}
```
Here's an explanation of the solution:

We first check if the array is empty, and if so, return nil.

We then initialize two variables: `sign` to keep track of the product of all signs, and `sum` to keep track of the sum of magnitudes of integers.

We iterate over the array, and for each number, we multiply `sign` by the sign of the number (using `math.Signfloat64` to get the sign as an integer), and add the magnitude of the number (using `math.Abs`) to `sum`.

Finally, we return the product of `sum` and `sign` as the result.

Note that we use `float64` to store the sum and the result, since the sum of magnitudes can be a floating-point number. We also use `int` to store the sign, since the product of signs is an integer.