```go
package main

import "fmt"

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


This code defines a function `IncrList` that takes a slice of integers as input, and returns a new slice with each element incremented by 1. It does this by creating a new slice of the same length, and then iterating over the input slice, incrementing each element and adding it to the new slice.

In the `main` function, we test the `IncrList` function with two different input slices, and print the results using `fmt.Println`. The output is as expected: the first slice is incremented by 1, and the second slice is also incremented by 1.