```go
package main

import (
    "math"
)

func SumSquares(lst []int) int {
    var sum int
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


Explanation:
The function `SumSquares` iterates over the input list `lst` using a range-based loop. For each element `v` at index `i`, it checks the conditions specified in the problem statement:
- If `i` is a multiple of 3, it squares the element `v` and adds it to the sum.
- If `i` is a multiple of 4 and not a multiple of 3, it cubes the element `v` and adds it to the sum.
- Otherwise, it simply adds the original element `v` to the sum.

The `math.Pow` function is used to compute the square and cube of the element. The result is converted back to an integer using the `int` function before returning it. If the input list is empty, the function will return 0 as expected.