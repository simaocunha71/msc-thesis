Here is the solution:
```go
import (
    "math"
    "math/cmplx"
    "fmt"
)

func SumSquares(lst []float64) int {
    var sum int
    for _, num := range lst {
        // Round each element in the list to the upper int(Ceiling) first
        ceiling := int(math.Ceil(num))
        sum += ceiling * ceiling
    }
    return sum
}

func main() {
    fmt.Println(SumSquares([]float64{1, 2, 3})) // 14
    fmt.Println(SumSquares([]float64{1, 4, 9})) // 98
    fmt.Println(SumSquares([]float64{1, 3, 5, 7})) // 84
    fmt.Println(SumSquares([]float64{1.4, 4.2, 0})) // 29
    fmt.Println(SumSquares([]float64{-2.4, 1, 1})) // 6
}
```
The `SumSquares` function takes a slice of float64 as input, and returns the sum of the squared numbers in the list, after rounding each element to the upper integer using `math.Ceil`. The `main` function demonstrates the usage of the `SumSquares` function with different input lists. The output is the sum of the squared numbers in the list, after rounding each element to the upper integer.