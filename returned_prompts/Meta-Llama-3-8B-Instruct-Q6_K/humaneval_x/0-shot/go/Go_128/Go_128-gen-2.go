Here is the solution:
```go
import (
    "math"
)

func ProdSigns(arr []int) interface{} {
    if len(arr) == 0 {
        return nil
    }
    var productSign int
    var sum float64
    for _, num := range arr {
        if num == 0 {
            return 0
        }
        productSign *= math.Signum(float64(num))
        sum += math.Abs(float64(num))
    }
    return productSign * sum
}
```
Here's an explanation of the solution:

1. First, we check if the array is empty. If it is, we return `nil`.
2. We initialize two variables: `productSign` to keep track of the product of all signs, and `sum` to keep track of the sum of magnitudes of integers.
3. We iterate over the array. For each number, we check if it's 0. If it is, we return 0, because the product of all signs is undefined for an array containing 0.
4. We multiply `productSign` by the sign of the current number using `math.Signum`. `math.Signum` returns 1 if the number is positive, -1 if the number is negative, and 0 if the number is 0.
5. We add the magnitude of the current number to `sum` using `math.Abs`.
6. After iterating over the array, we return the product of `productSign` and `sum`.

This solution has a time complexity of O(n), where n is the length of the input array, because we iterate over the array once. It has a space complexity of O(1), because we use a constant amount of space to store the variables `productSign` and `sum`.