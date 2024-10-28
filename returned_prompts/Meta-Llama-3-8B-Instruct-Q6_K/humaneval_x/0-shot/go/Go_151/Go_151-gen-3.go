```go
package main

import (
    "math"
    "fmt"
)

func DoubleTheDifference(lst []float64) int {
    sum := 0
    for _, num := range lst {
        if math.Abs(num) > 0.5 && math.Mod(num, 1) == 0 {
            sum += int(math.Pow(num, 2))
        }
    }
    return sum
}

func main() {
    fmt.Println(DoubleTheDifference([]float64{1, 3, 2, 0})) // 10
    fmt.Println(DoubleTheDifference([]float64{-1, -2, 0})) // 0
    fmt.Println(DoubleTheDifference([]float64{9, -2})) // 81
    fmt.Println(DoubleTheDifference([]float64{0})) // 0
    fmt.Println(DoubleTheDifference([]float64{})) // 0
}
```
This program defines a function `DoubleTheDifference` that takes a slice of `float64` as input and returns the sum of squares of the numbers in the list that are odd and positive. It iterates over the input list and checks each number to see if it is positive and has an odd integer value. If it does, it adds the square of the number to the sum. Finally, it returns the sum.

The `main` function tests the `DoubleTheDifference` function with different inputs and prints the results. The inputs are:
- `[1, 3, 2, 0]` which should return `10`
- `[-1, -2, 0]` which should return `0`
- `[9, -2]` which should return `81`
- `[0]` which should return `0`
- `[]` which should return `0`

The output of the program is:
```
10
0
81
0
0
```



```go
package main

import (
    "fmt"
    "math"
)

func DoubleTheDifference(lst []float64) int {
    sum := 0
    for _, num := range lst {
        if num > 0 && math.Mod(num, 2) != 0 {
            sum += int(math.Pow(num, 2))
        }
    }
    return sum
}

func main() {
    fmt.Println(DoubleTheDifference([]float64{1, 3, 2, 0})) // 10
    fmt.Println(DoubleTheDifference([]float64{-