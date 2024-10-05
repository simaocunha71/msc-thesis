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
        if num < 0 {
            sign *= -1
        }
        sum += math.Abs(float64(num))
    }
    return sum * float64(sign)
}
```

The function `ProdSigns` takes an array of integers as input and returns the sum of the magnitudes of the integers multiplied by the product of the signs of the integers. If the input array is empty, it returns `nil`.

Here's a breakdown of the code:

1. We check if the length of the input array is 0. If it is, we return `nil`.
2. We initialize two variables: `sign` to 1 and `sum` to 0. `sign` will keep track of the product of the signs of the integers, and `sum` will keep track of the sum of the magnitudes of the integers.
3. We iterate through the input array using a `for` loop. For each integer `num` in the array, we check if it's negative. If it is, we multiply `sign` by -1 to reflect the negative sign.
4. We add the magnitude of `num` to `sum` using `math.Abs`.
5. Finally, we return the product of `sum` and `sign`. This is the result of multiplying the sum of the magnitudes by the product of the signs.

Note that we use `math.Abs` to get the magnitude of each integer, and we convert the integer to a float64 before multiplying it by the sign. This is because `math.Abs` returns a float64, and we need to multiply it by the sign, which is also a float64. If we didn't convert the integer to a float64, we would get an error when trying to multiply an integer by a float64.