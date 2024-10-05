Here is the solution in Go:

```go
import (
    "math"
)

func Pluck(arr []int) []int {
    var result []int
    minEvenValue := math.MaxInt32
    minIndex := -1
    for i, v := range arr {
        if v%2 == 0 && v < minEvenValue {
            minEvenValue = v
            minIndex = i
        }
    }
    if minEvenValue != math.MaxInt32 {
        result = append(result, minEvenValue)
        result = append(result, minIndex)
    }
    return result
}
```

This function iterates over the array, checks each value to see if it's even, and if it's smaller than the current minimum even value. If it is, it updates the minimum even value and its index. Finally, it returns the minimum even value and its index as a list. If there are no even values, it returns an empty list. 

The time complexity of this function is O(n), where n is the length of the array, because it iterates over the array once. The space complexity is O(1), because it only uses a constant amount of space to store the result and other variables. 





This problem can be solved by using a for loop to iterate over the array, checking each value to see if it's even and smaller than the current minimum even value. If it is, update the minimum even value and its index. Finally, return the minimum even value and its index as a list.

Here is the code in Go:

```go
func Pluck(arr []int) []int {
    var result []int
    minEvenValue := math.MaxInt32
    minIndex := -1
    for i, v := range arr {
        if v%2 == 0 && v < minEvenValue {
            minEvenValue = v
            minIndex = i
        }
    }
    if minEvenValue != math.MaxInt32 {
        result = append(result, minEvenValue)
        result = append(result, minIndex)
    }
    return result
}
```

In this code, `math.MaxInt32` is used to initialize `minEvenValue` to the maximum possible integer value. This is because we don't know what the smallest even value in the array is, so we start with the maximum possible value.

The function then iterates over the array using a for loop, checking each value to see