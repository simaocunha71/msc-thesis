
```go
func Intersperse(numbers []int, delimeter int) []int {
    result := make([]int, len(numbers)*2-1)
    for i, n := range numbers {
        result[i*2] = n
        result[i*2+1] = delimeter
    }
    return result
}
```

The `Intersperse` function takes in a slice of integers and a delimeter integer and returns a new slice of integers. 

To achieve the desired result, we initialize a new slice called `result` with a length of `len(numbers)*2-1`, which is the length of the new slice we want to create. 

Then, we iterate over each element in the `numbers` slice using a `for` loop and the `range` keyword. For each element, we assign it to the `n` variable. 

Inside the loop, we assign the value of `n` to the `i`th index of the `result` slice (`result[i*2]`) and the delimeter to the `i`th index plus one (`result[i*2+1]`). This effectively inserts the delimeter between each element of the `numbers` slice. 

Finally, we return the `result` slice, which now contains the `numbers` slice with the delimeter inserted between each element.

For example, if we call `Intersperse([]int{1, 2, 3}, 4)`, the function will return `[1, 4, 2, 4, 3]`, as expected.

```go
package main

import "fmt"

func main() {
    fmt.Println(Intersperse([]int{1, 2, 3}, 4))
}
```

This code snippet demonstrates the usage of the `Intersperse` function. It creates a new slice `[]int{1, 2, 3}` and passes it along with the delimeter `4` to the `Intersperse` function. The result is printed using `fmt.Println`, which outputs `[1, 4, 2, 4, 3]`.

I