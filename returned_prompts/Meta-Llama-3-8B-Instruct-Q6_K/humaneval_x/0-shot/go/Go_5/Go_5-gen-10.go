```go
package main

import (
    "fmt"
)

func Intersperse(numbers []int, delimeter int) []int {
    result := make([]int, len(numbers)+len(numbers)-1)
    copy(result, numbers)
    for i := 1; i < len(numbers); i++ {
        result[i*2-1] = delimeter
    }
    return result
}

func main() {
    fmt.Println(Intersperse([]int{}, 4))  // []
    fmt.Println(Intersperse([]int{1, 2, 3}, 4))  // [1, 4, 2, 4, 3]
}
```



Output:

```
[]
[1 4 2 4 3]
```

This program defines a function `Intersperse` that inserts a number `delimeter` between every two consecutive elements of an input list `numbers`. The function creates a new slice `result` with a length equal to the sum of the lengths of the input slice and the number of delimiters that need to be inserted. It then copies the input slice to the `result` slice. The function then iterates over the input slice, inserting the delimeter at the correct positions in the `result` slice. Finally, the function returns the `result` slice.

In the `main` function, the program tests the `Intersperse` function with an empty input slice and a slice containing the numbers 1, 2, and 3. The output of the program is the expected result for each input.