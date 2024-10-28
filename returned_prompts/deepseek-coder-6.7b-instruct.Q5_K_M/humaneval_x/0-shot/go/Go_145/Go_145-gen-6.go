Here's the solution to your problem:

```go
func OrderByPoints(nums []int) []int {
    sort.Slice(nums, func(i, j int) bool {
        sumI := sumOfDigits(nums[i])
        sumJ := sumOfDigits(nums[j])
        if sumI == sumJ {
            return i < j
        }
        return sumI < sumJ
    })
    return nums
}

func sumOfDigits(num int) int {
    sum := 0
    for num != 0 {
        digit := num % 10
        sum += digit
        num /= 10
    }
    return sum
}
```

This solution uses Go's built-in sort package to sort the slice of integers. The sort function is given a comparison function that first compares the sum of the digits of two integers. If their digit sums are equal, it then compares their original indices.

The function sumOfDigits calculates the sum of the digits of an integer by continuously dividing the number by 10 and adding the remainder. This remainder is the last digit of the number.
```
```








































































































































































































































