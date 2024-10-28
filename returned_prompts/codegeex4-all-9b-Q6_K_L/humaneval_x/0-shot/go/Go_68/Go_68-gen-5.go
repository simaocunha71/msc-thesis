```go
package main

import "fmt"

func Pluck(arr []int) []int {
    if len(arr) == 0 {
        return []int{}
    }
    minVal := math.MaxInt
    minIndex := -1
    for i, v := range arr {
        if v%2 == 0 && v < minVal {
            minVal = v
            minIndex = i
        }
    }
    if minIndex == -1 {
        return []int{}
    }
    return []int{arr[minIndex], minIndex}
}

func main() {
    fmt.Println(Pluck([]int{4, 2, 3}))    // Output: [2, 1]
    fmt.Println(Pluck([]int{1, 2, 3}))    // Output: [2, 1]
    fmt.Println(Pluck([]int{}))           // Output: []
    fmt.Println(Pluck([]int{5, 0, 3, 0, 4, 2}))    // Output: [0, 1]
}
```
