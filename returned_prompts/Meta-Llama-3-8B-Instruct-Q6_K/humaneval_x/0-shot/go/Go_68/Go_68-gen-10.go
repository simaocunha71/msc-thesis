Here is the Go solution:

```go
import (
    "math"
)

func Pluck(arr []int) []int {
    var smallestEven int
    var smallestIndex int
    var found bool

    for i, v := range arr {
        if v%2 == 0 {
            if !found || v < smallestEven {
                smallestEven = v
                smallestIndex = i
                found = true
            }
        }
    }

    if found {
        return []int{smallestEven, smallestIndex}
    }
    return []int{}
}
```

This function iterates over the array, checks each node's value if it's even and if it's smaller than the current smallest even value, updates the smallest even value and its index. If no even value is found, it returns an empty list. If an even value is found, it returns the smallest even value and its index. 

The time complexity is O(n), where n is the length of the array, as we are iterating over the array once. The space complexity is O(1), as we are using a constant amount of space to store the smallest even value and its index. 