Here is the solution in Go:

```go
import (
    "math"
)

func Minsubarraysum(nums []int) int {
    if len(nums) == 0 {
        return 0
    }
    sum := nums[0]
    minSum := nums[0]
    for i := 1; i < len(nums); i++ {
        sum += nums[i]
        minSum = math.Min(float64(minSum), float64(sum))
        if sum < 0 {
            sum = 0
        }
    }
    return int(minSum)
}
```

In this solution, we initialize `sum` and `minSum` to the first element of the array. Then, we iterate over the array, adding each element to `sum`. We update `minSum` to be the minimum of the current `minSum` and `sum`. If `sum` becomes negative, we reset it to 0. Finally, we return `minSum` as the minimum sum of any non-empty subarray.

For example, given the array `[2, 3, 4, 1, 2, 4]`, the function will return `1`, which is the minimum sum of the subarray `[1]`. Given the array `[-1, -2, -3]`, the function will return `-6`, which is the minimum sum of the subarray `[-1, -2, -3]`. If the input array is empty, the function will return `0`.