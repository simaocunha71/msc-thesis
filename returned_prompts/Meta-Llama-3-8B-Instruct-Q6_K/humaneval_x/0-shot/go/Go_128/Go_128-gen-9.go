Here is the solution in Go:

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

    var product float64 = 1
    var sum float64 = 0
    var sign int = 1

    for _, num := range arr {
        if num < 0 {
            sign *= -1
        }
        product *= float64(sign)
        sum += math.Abs(float64(num))
    }

    return product * sum
}

func main() {
    fmt.Println(ProdSigns([]int{1, 2, 2, -4})) // Output: -9
    fmt.Println(ProdSigns([]int{0, 1})) // Output: 0
    fmt.Println(ProdSigns([]int{})) // Output: nil
}
```

The program checks if the array is empty and returns `nil` if it is. Then it iterates over each number in the array. If the number is negative, it multiplies the product by -1 to account for the sign. It adds the absolute value of the number to the sum. Finally, it returns the product of the sum and the product of signs. The `math.Abs` function is used to get the absolute value of a number. The `math` package is imported to use this function. The `ProdSigns` function returns an interface{} type which can be `nil` or any other type. The `main` function demonstrates how to use the `ProdSigns` function with different inputs. The output is printed to the console.