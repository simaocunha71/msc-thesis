```go
package main

import (
    "fmt"
    "sort"
)

func RescaleToUnit(numbers []float64) []float64 {
    if len(numbers) < 2 {
        panic("list must have at least two elements")
    }
    sort.Float64s(numbers)
    min := numbers[0]
    max := numbers[len(numbers)-1]
    result := make([]float64, len(numbers))
    for i, num := range numbers {
        result[i] = (num - min) / (max - min)
    }
    return result
}

func main() {
    fmt.Println(RescaleToUnit([]float64{1.0, 2.0, 3.0, 4.0, 5.0}))
}
```
In this code, we first sort the input list of numbers. Then we find the minimum and maximum values in the list. We create a new list where each element is the corresponding element from the input list, but scaled so that the minimum element is 0 and the maximum element is 1. We use the formula `(num - min) / (max - min)` to achieve this. This formula subtracts the minimum value from the number, then divides the result by the range of the numbers (i.e., the difference between the maximum and minimum values). This effectively maps the range of the numbers to the interval [0, 1]. We then return this new list. In the main function, we test this function with the input list `[1.0, 2.0, 3.0, 4.0, 5.0]` and print the result. The output is `[0.0, 0.25, 0.5, 0.75, 1.0]`, which is the expected result. 

This function assumes that the input list has at least two elements. If the input list has less than two elements, the function panics. If you want to handle this case differently, you can modify the function accordingly. 

Note that this function modifies the input list. If you want to preserve the original list, you can create a copy of the list before modifying it. You can use the `copy` function to create a copy of the list, like this: `numbersCopy := make([]float64, len(numbers)); copy(numbersCopy, numbers)`. Then you can modify `numbersCopy` instead of `numbers`. 

Also note that this function uses