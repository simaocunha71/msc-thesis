The problem is asking to find the minimum sum of any non-empty sub-array in the given array. A sub-array is a contiguous part of the array.

The solution uses the concept of Kadane's algorithm, which is used to find the maximum sum of a sub-array. We can modify it to find the minimum sum by keeping track of the minimum sum and the current sum.

Here is the code:

```go
import (
    "math"
)

func Minsubarraysum(nums []int) int {
    min := math.MaxInt32
    sum := 0
    for _, num := range nums {
        sum += num
        min = int(math.Min(float64(min), float64(sum)))
        if sum < 0 {
            sum = 0
        }
    }
    return min
}
```

The code initializes the minimum sum to the maximum possible value and the current sum to 0. Then, it iterates over the array. For each number, it adds the number to the current sum and updates the minimum sum if the current sum is less than the minimum sum. If the current sum becomes negative, it resets the current sum to 0. Finally, it returns the minimum sum.

For example, if the input array is `[2, 3, 4, 1, 2, 4]`, the minimum sum of any non-empty sub-array is 1, which is the sum of the sub-array `[1]`. If the input array is `[-1, -2, -3]`, the minimum sum of any non-empty sub-array is -6, which is the sum of the sub-array `[-1, -2, -3]`.