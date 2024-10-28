Here is the Go code for the problem:

```go
import (
    "math"
)

func SumSquares(lst []int) int {
    var sum int
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

This function iterates over the input list using a range loop. For each element, it checks the index to see if it's a multiple of 3 or 4. If the index is a multiple of 3, it squares the element. If the index is a multiple of 4 but not a multiple of 3, it cubes the element. If the index is neither a multiple of 3 nor 4, it simply adds the element to the sum. The function returns the total sum. 

For example, for the input list [1,2,3], the output will be 6, because the function squares the element at index 0 (1), adds the element at index 1 (2), and cubes the element at index 2 (3). The sum is then 1 + 2 + 27 = 6. 

Note that the math.Pow function is used to calculate the square or cube of a number. The float64 type is used to avoid integer division. The int function is used to convert the result to an integer. 