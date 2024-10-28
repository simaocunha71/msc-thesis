```go
package main

import (
    "fmt"
    "reflect"
)

func IncrList(l []int) []int {
    result := make([]int, len(l))
    for i, v := range l {
        result[i] = v + 1
    }
    return result
}

func main() {
    fmt.Println(IncrList([]int{1, 2, 3})) // [2 3 4]
    fmt.Println(IncrList([]int{5, 3, 5, 2, 3, 3, 9, 0, 123})) // [6 4 6 3 4 4 10 1 124]
}
```



Explanation:

The function `IncrList` takes a slice of integers as input and returns a new slice with the same elements incremented by 1.

Here's a step-by-step breakdown of the implementation:

1. Create a new slice `result` with the same length as the input slice `l`.
2. Iterate over the input slice `l` using a range loop.
3. For each element `v` at index `i`, increment it by 1 and assign the result to the corresponding index `i` in the `result` slice.
4. Return the modified `result` slice.

The `main` function demonstrates the usage of the `IncrList` function with two different input slices, printing the resulting slices to the console.