Here is the solution in Go:
```go
import (
    "math"
)

func Pluck(arr []int) []int {
    var result []int
    minEvenValue := math.MaxInt32
    minEvenIndex := -1

    for i, v := range arr {
        if v%2 == 0 && v < minEvenValue {
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
This function iterates over the array, keeping track of the smallest even value and its index. If no even values are found, it returns an empty list. Otherwise, it returns a list containing the smallest even value and its index. This solution has a time complexity of O(n), where n is the length of the input array.