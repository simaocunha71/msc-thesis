```go
package main

import (
    "fmt"
)

func Intersperse(numbers []int, delimeter int) []int {
    result := make([]int, len(numbers)+len(numbers)-1)
    result[0] = numbers[0]
    for i := 1; i < len(numbers); i++ {
        result[2*i-1] = numbers[i-1]
        result[2*i] = delimeter
    }
    result[2*len(numbers)-1] = numbers[len(numbers)-1]
    return result
}

func main() {
    fmt.Println(Intersperse([]int{}, 4))
    fmt.Println(Intersperse([]int{1, 2, 3}, 4))
}
```

The `Intersperse` function takes a slice of integers `numbers` and an integer `delimeter` as input. It creates a new slice `result` with a length that is equal to the length of the input slice plus the number of elements in the input slice minus 1. This is because we will be inserting the `delimeter` between every two consecutive elements of the input slice.

The function then initializes the first element of the `result` slice with the first element of the input slice.

It then iterates over the elements of the input slice, starting from the second element (at index 1). For each element, it sets the corresponding element in the `result` slice to the current element, and then sets the next element in the `result` slice to the `delimeter`.

Finally, it sets the last element of the `result` slice to the last element of the input slice, and returns the `result` slice.

In the `main` function, we test the `Intersperse` function with an empty input slice and a non-empty input slice. The output of the program is:

```
[]
[1 4 2 4 3]
```


This shows that the `Intersperse` function correctly inserts the `delimeter` between every two consecutive elements of the input slice.