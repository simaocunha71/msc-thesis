Here is a solution for the problem using Kadane's algorithm:
```go
import (
    "math"
)

func Minsubarraysum(nums []int) int {
    if len(nums) == 0 {
        return 0
    }
    minSum := nums[0]
    currentSum := nums[0]
    for i := 1; i < len(nums); i++ {
        currentSum = math.Max(nums[i], currentSum+nums[i])
        minSum = math.Min(minSum, currentSum)
    }
    return minSum
}
```
Explanation:
Kadane's algorithm is a dynamic programming algorithm used to find the maximum sum of a subarray within an array. It is a simple, efficient and widely used algorithm. In this problem, we are asked to find the minimum sum of a non-empty subarray, so we need to modify the algorithm to find the minimum sum. We keep track of the minimum sum and the current sum of the subarray. For each element in the array, we calculate the current sum by taking the maximum of the current sum and the sum of the current element and the previous current sum. We update the minimum sum if the current sum is less than the minimum sum. Finally, we return the minimum sum. If the array is empty, we return 0.