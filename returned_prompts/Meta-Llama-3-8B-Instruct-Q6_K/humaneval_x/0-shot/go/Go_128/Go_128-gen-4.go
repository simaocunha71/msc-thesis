Here is the Go code that implements the function `ProdSigns` as per the problem description:

```go
import (
    "math"
)

func ProdSigns(arr []int) interface{} {
    if len(arr) == 0 {
        return nil
    }
    productOfSigns := 1
    sumOfMagnitudes := 0
    for _, num := range arr {
        if num > 0 {
            productOfSigns *= 1
        } else if num < 0 {
            productOfSigns *= -1
        }
        sumOfMagnitudes += math.Abs(float64(num))
    }
    return sumOfMagnitudes * float64(productOfSigns)
}
```
This function calculates the product of signs by iterating over the array and multiplying the product with 1 for positive numbers, -1 for negative numbers, and keeping it unchanged for zero. It also calculates the sum of magnitudes by iterating over the array and adding the absolute value of each number to the sum. Finally, it returns the product of the sum of magnitudes and the product of signs. If the array is empty, the function returns nil.