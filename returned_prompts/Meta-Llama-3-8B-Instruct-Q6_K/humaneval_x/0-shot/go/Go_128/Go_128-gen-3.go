Here is the solution in Go:
```go
import (
    "math"
)

func ProdSigns(arr []int) interface{} {
    if len(arr) == 0 {
        return nil
    }
    sign := 1
    sum := 0
    for _, num := range arr {
        if num < 0 {
            sign *= -1
        }
        sum += math.Abs(float64(num))
    }
    return sign * sum
}
```
Here's an explanation of the solution:

1. We first check if the input array is empty. If it is, we return `nil`.
2. We initialize a variable `sign` to 1, which will store the product of all signs in the array.
3. We initialize a variable `sum` to 0, which will store the sum of the magnitudes of the integers in the array.
4. We iterate through the array, and for each number, we check if it's negative. If it is, we multiply `sign` by -1.
5. We add the absolute value of the number to `sum`.
6. Finally, we return the product of `sign` and `sum`. This gives us the sum of the magnitudes of the integers multiplied by the product of all signs.

Note that we use `math.Abs` to get the absolute value of each number, and we convert the integer to a float64 to allow for the use of `math.Abs`. This is because `math.Abs` only works with floats. We then convert the result back to an integer using the `int` function. Alternatively, we could use the `math.Abs(float64(num))` function directly, which would avoid the need for the intermediate conversion.