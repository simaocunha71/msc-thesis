Here is a Go solution for the problem:

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
        sign *= math.Signum(float64(num))
        sum += math.Abs(float64(num))
    }
    return sign * sum
}
```

In this solution, we first check if the array is empty. If it is, we return `nil`. Then we initialize two variables, `sign` and `sum`. `sign` will store the product of the signs of all numbers in the array, and `sum` will store the sum of the magnitudes of all numbers in the array. We then iterate over the array, multiplying `sign` by the sign of the current number and adding the magnitude of the current number to `sum`. Finally, we return the product of `sign` and `sum`. The `math.Signum` function is used to get the sign of a number, and the `math.Abs` function is used to get the magnitude of a number. The `math.Signum` function returns 1 for positive numbers, -1 for negative numbers, and 0 for zero. The `math.Abs` function returns the absolute value of a number. The product of the signs of all numbers in the array is calculated by multiplying the signs of each number. The sum of the magnitudes of all numbers in the array is calculated by adding the magnitudes of each number. The product of the signs of all numbers in the array and the sum of the magnitudes of all numbers in the array is returned as the result. The `interface{}` return type is used to allow the function to return either an integer value or `nil` when the input array is empty.