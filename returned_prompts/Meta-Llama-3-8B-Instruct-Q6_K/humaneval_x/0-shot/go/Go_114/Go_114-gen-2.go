```go
import (
    "math"
)

func Minsubarraysum(nums []int) int {
    minSum := math.MaxInt32
    currentSum := 0
    for _, num := range nums {
        currentSum += num
        minSum = int(math.Min(float64(minSum), float64(currentSum)))
        if currentSum > 0 {
            currentSum = 0
        }
    }
    return minSum
}
```

Explanation:
The problem is asking to find the minimum sum of any non-empty sub-array of the given array. We can achieve this by maintaining a running sum of the sub-array and updating the minimum sum if the current sum is less than the minimum sum found so far.

We initialize the minimum sum as `math.MaxInt32` and the current sum as 0. Then, we iterate over the array. For each number, we add it to the current sum and update the minimum sum if the current sum is less than the minimum sum found so far. If the current sum becomes positive, we reset it to 0.

Finally, we return the minimum sum found. This approach ensures that we consider all non-empty sub-arrays and find the minimum sum.

In the example, the input array is `[2, 3, 4, 1, 2, 4]`. The minimum sum of any non-empty sub-array is 1, which is obtained by taking the sub-array `[1]`.

In the second example, the input array is `[-1, -2, -3]`. The minimum sum of any non-empty sub-array is -6, which is obtained by taking the sub-array `[-1, -2, -3]`.