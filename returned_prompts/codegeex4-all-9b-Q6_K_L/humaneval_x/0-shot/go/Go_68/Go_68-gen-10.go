```go
package main

import (
	"fmt"
)

func Pluck(arr []int) []int {
    if len(arr) == 0 {
        return []int{}
    }

    minEven := math.MaxInt64
    minIndex := -1

    for i, num := range arr {
        if num%2 == 0 && num < minEven {
            minEven = num
            minIndex = i
        }
    }

    if minIndex == -1 {
        return []int{}
    }

    return []int{minEven, minIndex}
}

func main() {
    fmt.Println(Pluck([]int{4, 2, 3}))       // Output: [2, 1]
    fmt.Println(Pluck([]int{1, 2, 3}))       // Output: [2, 1]
    fmt.Println(Pluck([]int{}))             // Output: []
    fmt.Println(Pluck([]int{5, 0, 3, 0, 4, 2})) // Output: [0, 1]
}
```
