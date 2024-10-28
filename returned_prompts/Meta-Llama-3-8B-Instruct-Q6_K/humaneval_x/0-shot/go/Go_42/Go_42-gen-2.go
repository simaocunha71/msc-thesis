```go
package main

import (
    "fmt"
)

func IncrList(l []int) []int {
    result := make([]int, len(l))
    for i, v := range l {
        result[i] = v + 1
    }
    return result
}

func main() {
    fmt.Println(IncrList([]int{1, 2, 3}))  // [2, 3, 4]
    fmt.Println(IncrList([]int{5, 3, 5, 2, 3, 3, 9, 0, 123}))  // [6, 4, 6, 3, 4, 4, 10, 1, 124]
}
```

This program defines a function `IncrList` that takes a slice of integers as input and returns a new slice with each element incremented by 1. The function uses a loop to iterate over the input slice and creates a new slice with the incremented values.

In the `main` function, we call `IncrList` with two different input slices and print the results. The output shows that the function correctly increments each element in the input slice.