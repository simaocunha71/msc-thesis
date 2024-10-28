You can solve this problem by first creating a helper function that calculates the sum of the digits of a given integer. Then, you can use this helper function to sort the original list of integers based on their digit sum.

Here is the Go code that implements this solution:

```go
import (
    "sort"
    "strconv"
)

// Helper function to calculate the sum of the digits of a given integer
func digitSum(n int) int {
    sum := 0
    for n != 0 {
        digit := n % 10
        sum += digit
        n /= 10
    }
    return sum
}

// Function to sort the list of integers based on the sum of their digits
func OrderByPoints(nums []int) []int {
    sort.Slice(nums, func(i, j int) bool {
        return digitSum(nums[i]) < digitSum(nums[j])
    })
    return nums
}
```

In this code, the `digitSum` function calculates the sum of the digits of a given integer by repeatedly dividing the number by 10 and adding the remainder to the sum.

The `OrderByPoints` function sorts the original list of integers based on the sum of their digits by using the `sort.Slice` function. This function takes a slice of integers and a custom comparison function as arguments. The comparison function compares two integers based on their digit sum using the `digitSum` function.

Finally, the `OrderByPoints` function returns the sorted list of integers.