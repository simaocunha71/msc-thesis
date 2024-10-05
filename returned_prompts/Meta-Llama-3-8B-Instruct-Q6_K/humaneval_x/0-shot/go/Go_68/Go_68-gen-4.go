Here is a Go function that implements the Pluck operation as described:

```go
package main

import (
    "fmt"
    "math"
)

func Pluck(arr []int) []int {
    var result []int
    minEvenValue := math.MaxInt
    minIndex := -1
    for i, v := range arr {
        if v%2 == 0 && v < minEvenValue {
            minEvenValue = v
            minIndex = i
        }
    }
    if minIndex != -1 {
        result = []int{minEvenValue, minIndex}
    }
    return result
}

func main() {
    fmt.Println(Pluck([]int{4, 2, 3}))  // Output: [2 1]
    fmt.Println(Pluck([]int{1, 2, 3}))  // Output: [2 1]
    fmt.Println(Pluck([]int{}))        // Output: []
    fmt.Println(Pluck([]int{5, 0, 3, 0, 4, 2}))  // Output: [0 1]
}
```

This function iterates over the array, checks each node for even value, and updates the minimum even value and its index if a smaller even value is found. If a minimum even value is found, it returns a list containing the minimum even value and its index. If no even value is found, it returns an empty list. The time complexity is O(n) where n is the length of the array. The space complexity is O(1) as it only uses a constant amount of space.