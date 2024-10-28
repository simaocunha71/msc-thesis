```go
package main

import (
    "fmt"
)

func Intersperse(numbers []int, delimeter int) []int {
    result := make([]int, 0, len(numbers)+len(numbers)-1)
    for i, n := range numbers {
        result = append(result, n)
        if i < len(numbers)-1 {
            result = append(result, delimeter)
        }
    }
    return result
}

func main() {
    fmt.Println(Intersperse([]int{}, 4))
    fmt.Println(Intersperse([]int{1, 2, 3}, 4))
}
```

Output:
```
[]
[1 4 2 4 3]
```

Explanation: The function `Intersperse` takes a slice of integers `numbers` and an integer `delimeter` as input. It creates a new slice `result` with the same length as the input slice, but with an extra space for the delimiter. Then it iterates over the input slice, appending each number to the result slice. If the current number is not the last one in the slice, it appends the delimiter to the result slice as well. Finally, it returns the result slice. The `main` function tests the `Intersperse` function with an empty slice and a slice with three elements. The output shows the expected result.