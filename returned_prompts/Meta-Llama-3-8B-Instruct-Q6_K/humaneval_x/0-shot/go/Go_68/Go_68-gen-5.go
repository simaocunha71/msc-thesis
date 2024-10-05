Here is a solution in Go that uses a simple loop to iterate over the array and find the smallest even value, and its index.

```go
import (
    "math"
)

func Pluck(arr []int) []int {
    var result []int
    smallestEvenValue := math.MaxInt64
    smallestEvenIndex := -1

    for i, v := range arr {
        if v%2 == 0 && v < smallestEvenValue {
            smallestEvenValue = v
            smallestEvenIndex = i
        }
    }

    if smallestEvenValue != math.MaxInt64 {
        result = []int{smallestEvenValue, smallestEvenIndex}
    } else {
        result = []int{}
    }

    return result
}
```

You can test the function with the provided examples:

```go
fmt.Println(Pluck([]int{4, 2, 3})) // Output: [2, 1]
fmt.Println(Pluck([]int{1, 2, 3})) // Output: [2, 1]
fmt.Println(Pluck([]int{}))        // Output: []
fmt.Println(Pluck([]int{5, 0, 3, 0, 4, 2})) // Output: [0, 1]
```

This solution has a time complexity of O(n), where n is the length of the input array, because it makes a single pass over the array. The space complexity is O(1), because it uses a constant amount of space to store the result and the variables. 