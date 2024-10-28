Here is the solution:

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
        min = int(math.Min(float64(min), float64(sum)))
        if sum < 0 {
            sum = 0
        }
    }
    return min
}
```

Explanation:
We iterate over the array, keeping a running sum of the elements. If the sum becomes negative, we reset it to 0. We also keep track of the minimum sum seen so far. At the end, the minimum sum is the result. If the array is empty, we return 0. If the array is not empty, we return the minimum sum. 

The time complexity is O(n), where n is the length of the array, and the space complexity is O(1). 

Note: This solution assumes that the input array is not null. If the input array can be null, you should add a check for null at the beginning of the function and return 0 or a default value if the array is null. 

Also, this solution uses the math package for the math.Min function. If you don't want to use the math package, you can implement the min function yourself. 

Finally, this solution assumes that the input array contains only integers. If the array can contain other types of numbers, you should add a type check or conversion in the function. 