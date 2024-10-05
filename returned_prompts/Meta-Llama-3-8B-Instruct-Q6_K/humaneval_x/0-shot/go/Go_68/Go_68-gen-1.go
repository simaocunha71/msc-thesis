Here is the solution in Go:
```go
import (
    "math"
)

func Pluck(arr []int) []int {
    var result []int
    var minEvenValue int = math.MaxInt32
    var minEvenIndex int = -1

    for i, v := range arr {
        if v % 2 == 0 && v < minEvenValue {
            minEvenValue = v
            minEvenIndex = i
        }
    }

    if minEvenValue != math.MaxInt32 {
        result = []int{minEvenValue, minEvenIndex}
    } else {
        result = []int{}
    }

    return result
}
```
Explanation:

1. Initialize the result slice and the minimum even value and its index to `math.MaxInt32` and `-1` respectively.
2. Iterate over the input array using a range loop.
3. For each element, check if it's even (using the modulo operator `% 2 == 0`) and if it's smaller than the current minimum even value.
4. If it is, update the minimum even value and its index.
5. After the loop, check if the minimum even value is still `math.MaxInt32`. If it is, the array had no even values, so return an empty slice. Otherwise, return a slice containing the minimum even value and its index.

This solution has a time complexity of O(n), where n is the length of the input array, as it iterates over the array once. The space complexity is O(1), as it only uses a constant amount of space to store the result and the minimum even value and its index.