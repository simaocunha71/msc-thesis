Here is the solution:
```go
import (
    "math"
)

func SumSquares(lst []int) int {
    sum := 0
    for i, v := range lst {
        if i%3 == 0 {
            sum += math.Pow(float64(v), 2)
        } else if i%4 == 0 && i%3 != 0 {
            sum += math.Pow(float64(v), 3)
        } else {
            sum += v
        }
    }
    return int(sum)
}
```
This function iterates over the input list using a range-based for loop. For each element, it checks if the index is a multiple of 3 or 4, and applies the corresponding transformation (squaring or cubing). If the index is not a multiple of 3 or 4, the element is left unchanged. The transformed elements are added to the sum, which is returned at the end. The `math.Pow` function is used to compute the square or cube of a number. The `int` conversion is used to convert the sum to an integer, as the sum is initially a float64.