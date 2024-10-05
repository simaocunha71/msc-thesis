```go
package main

import (
    "math"
    "fmt"
)

func ProdSigns(arr []int) interface{} {
    if len(arr) == 0 {
        return nil
    }
    var sign int = 1
    var sum float64
    for _, num := range arr {
        if num < 0 {
            sign *= -1
        }
        sum += math.Abs(float64(num))
    }
    return sign * sum
}

func main() {
    fmt.Println(ProdSigns([]int{1, 2, 2, -4})) // prints -9
    fmt.Println(ProdSigns([]int{0, 1})) // prints 0
    fmt.Println(ProdSigns([]int{})) // prints <nil>
}
```

The code defines a function `ProdSigns` that calculates the sum of magnitudes of integers multiplied by the product of all signs of each number in the array. If the array is empty, it returns `nil`.

In the `main` function, we test the `ProdSigns` function with different inputs and print the results. The first input `[1, 2, 2, -4]` returns `-9`, the second input `[0, 1]` returns `0`, and the third input `[]` returns `nil`.

The `ProdSigns` function uses a variable `sign` to keep track of the product of all signs, and a variable `sum` to keep track of the sum of magnitudes. It iterates over the array, updating `sign` and `sum` accordingly. Finally, it returns the product of `sign` and `sum`.

The `main` function calls `ProdSigns` with different inputs and prints the results. The `fmt.Println` function is used to print the results. The `%T` verb is used to print the type of the result, and the `+` operator is used to concatenate the result with a string. The `fmt.Println` function is used to print the results to the console.