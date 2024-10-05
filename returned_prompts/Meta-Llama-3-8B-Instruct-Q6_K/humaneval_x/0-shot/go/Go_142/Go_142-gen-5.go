Here is the Go function that meets the requirements:
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


Explanation:
The function `SumSquares` iterates over the list `lst` using a range-based for loop. For each element `v` at index `i`, it checks the conditions specified in the problem statement:
- If `i` is a multiple of 3, it squares `v` and adds it to the sum.
- If `i` is a multiple of 4 and not a multiple of 3, it cubes `v` and adds it to the sum.
- If `i` is not a multiple of 3 or 4, it simply adds `v` to the sum.

The `math.Pow` function is used to calculate the square and cube of each element. The `int` function is used to convert the result to an integer. The sum is returned at the end of the function. 