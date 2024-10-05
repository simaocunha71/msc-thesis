Here is a simple implementation of the problem in Go:

```go
import (
    "math"
)

func Minsubarraysum(nums []int) int {
    if len(nums) == 0 {
        return 0
    }
    min := math.MaxInt64
    sum := 0
    for _, num := range nums {
        sum += num
        min = minInt(min, sum)
    }
    return min
}

func minInt(a, b int) int {
    if a < b {
        return a
    }
    return b
}
```

In this solution, we initialize `min` to the maximum possible integer value and `sum` to 0. Then, we iterate over the array. For each number, we add it to `sum` and update `min` if `sum` is smaller. At the end, `min` will be the smallest sum of any non-empty subarray. If the array is empty, we return 0. 

The time complexity of this solution is O(n), where n is the length of the input array, because we only iterate over the array once. The space complexity is O(1), because we only use a constant amount of space to store the variables. 

The `minInt` function is used to find the minimum between two integers. It's a simple function that returns the smaller of the two input values. 

This solution assumes that the input array is not null and that it contains at least one element. If these assumptions are not valid, you should add error checking code to handle these cases. 

For example, you could add a check at the beginning of the function to return 0 if the input array is empty, and you could add a check before the loop to return the sum of the entire array if the array contains only one element. 

Here is the modified code with error checking:

```go
func Minsubarraysum(nums []int) int {
    if len(nums) == 0 {
        return 0
    }
    if len(nums) == 1 {
        return nums[0]
    }
    min := math.MaxInt64
    sum := 0
    for _, num := range nums {
        sum += num
        min = minInt(min, sum)
    }
    return min
}

func minInt(a, b int) int {
    if a < b {
        return a
    }
    return b
}
``` 





