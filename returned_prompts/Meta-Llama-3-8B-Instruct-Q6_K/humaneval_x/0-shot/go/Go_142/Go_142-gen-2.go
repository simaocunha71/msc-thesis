Here is the solution in Go:
```go
import (
    "math"
)

func SumSquares(lst []int) int {
    sum := 0
    for i, v := range lst {
        if i%3 == 0 {
            sum += int(math.Pow(float64(v), 2))
        } else if i%4 == 0 && i%3 != 0 {
            sum += int(math.Pow(float64(v), 3))
        } else {
            sum += v
        }
    }
    return sum
}
```


This function iterates over the input list, checks the index of each element, and applies the corresponding transformation (squaring or cubing) if the index is a multiple of 3 or 4 respectively. If the index is not a multiple of 3 or 4, it simply adds the element to the sum. The function finally returns the sum of all elements.