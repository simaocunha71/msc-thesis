```go
import (
    "math"
)

func Minsubarraysum(nums []int) int {
    if len(nums) == 0 {
        return 0
    }
    minSum := math.MaxInt64
    currentSum := 0
    for _, num := range nums {
        currentSum += num
        minSum = min(minSum, currentSum)
        if currentSum > 0 {
            currentSum = 0
        }
    }
    return minSum
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
```


The problem asks you to find the minimum sum of any non-empty sub-array of the given array of integers.
The problem is a bit tricky because you need to find the minimum sum of any non-empty sub-array.
For example, if the array is [2, 3, 4, 1, 2, 4], the minimum sum of any non-empty sub-array is 1, which is the sum of the sub-array [1].

Here is the solution:
```go
import (
    "math"
)

func Minsubarraysum(nums []int) int {
    if len(nums) == 0 {
        return 0
    }
    minSum := math.MaxInt64
    currentSum := 0
    for _, num := range nums {
        currentSum += num
        minSum = min(minSum, currentSum)
        if currentSum > 0 {
            currentSum = 0
        }
    }
    return minSum
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
```
The function `Minsubarraysum` takes an array of integers as input and returns the minimum sum of any non-empty sub-array.
The function first checks if the input array is empty. If it is, the function returns 0.
Then, the function initializes two variables: `minSum` to store the minimum sum of any non-empty sub-array, and `currentSum` to store the sum of the current sub-array.
The function then iterates over the input array, adding each element to `currentSum` and updating `minSum` if `currentSum` is less than `minSum`.
If `currentSum` becomes greater than 0, the function resets `currentSum` to 0.
Finally, the function returns