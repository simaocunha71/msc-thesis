You can solve this problem by using the built-in functions max, min, and len from the standard library. Here is a possible solution:

```go
func LargestSmallestIntegers(lst []int) [2]interface{} {
    if len(lst) == 0 {
        return [2]interface{}{nil, nil}
    }

    negatives := make([]int, 0)
    positives := make([]int, 0)

    for _, num := range lst {
        if num < 0 {
            negatives = append(negatives, num)
        } else if num > 0 {
            positives = append(positives, num)
        }
    }

    if len(negatives) == 0 {
        return [2]interface{}{nil, min(positives)}
    }

    if len(positives) == 0 {
        return [2]interface{}{max(negatives), nil}
    }

    return [2]interface{}{max(negatives), min(positives)}
}

func max(nums []int) int {
    if len(nums) == 0 {
        return 0
    }

    max := nums[0]
    for _, num := range nums {
        if num > max {
            max = num
        }
    }
    return max
}

func min(nums []int) int {
    if len(nums) == 0 {
        return 0
    }

    min := nums[0]
    for _, num := range nums {
        if num < min {
            min = num
        }
    }
    return min
}
```

This solution first checks if the list is empty and returns `(nil, nil)` if it is. Then, it iterates through the list and separates the numbers into two different slices: `negatives` for negative numbers and `positives` for positive numbers. After that, it checks if there are any negative or positive numbers in the list and returns the appropriate value. Finally, it returns the maximum negative number and the minimum positive number.