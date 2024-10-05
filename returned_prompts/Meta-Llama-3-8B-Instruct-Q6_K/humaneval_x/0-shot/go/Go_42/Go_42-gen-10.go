```go
package main

import (
    "fmt"
    "strconv"
)

func IncrList(l []int) []int {
    var result []int
    for _, v := range l {
        result = append(result, v+1)
    }
    return result
}

func main() {
    fmt.Println(IncrList([]int{1, 2, 3}))  // [2, 3, 4]
    fmt.Println(IncrList([]int{5, 3, 5, 2, 3, 3, 9, 0, 123}))  // [6, 4, 6, 3, 4, 4, 10, 1, 124]
}
```


Explanation:
This program defines a function `IncrList` that takes a slice of integers as input and returns a new slice with each element incremented by 1.

Inside the function, we create an empty slice `result` to store the incremented values. We then iterate over the input slice `l` using a range loop. For each element `v` in the input slice, we append the incremented value `v+1` to the `result` slice.

Finally, we return the `result` slice, which contains the incremented values.

In the `main` function, we test the `IncrList` function with two different input slices and print the results. The output shows the expected incremented values.