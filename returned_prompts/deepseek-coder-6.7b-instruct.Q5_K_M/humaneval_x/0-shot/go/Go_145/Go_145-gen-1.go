```go
func OrderByPoints(nums []int) []int {
    sort.Slice(nums, func(i, j int) bool {
        sumI := sumDigits(nums[i])
        sumJ := sumDigits(nums[j])
        if sumI == sumJ {
            return i < j
        }
        return sumI < sumJ
    })
    return nums
}

func sumDigits(num int) int {
    sum := 0
    for num != 0 {
        digit := num % 10
        sum += digit
        num /= 10
    }
    return sum
}
```

Explanation:
This solution uses Go's built-in sort.Slice function with a custom comparison function. 
The comparison function first computes the sum of the digits for each number (using the sumDigits helper function), 
then compares these sums. If the sums are equal, it falls back to comparing the original indices of the numbers.

The sort.Slice function sorts the slice in-place, so the original nums slice is modified and returned. 

This solution has a time complexity of O(n log n) due to the sorting operation.

The sumDigits function works by repeatedly taking the last digit of the number and adding it to the sum, 
then removing the last digit from the number until there are no more digits left. 
This is done using integer division and modulus operations, which are O(log n) operations for each number. 
So the total time complexity of sumDigits is O(n log n).

The overall time complexity of OrderByPoints is therefore O(n log n).

The space complexity is O(1), as no additional space is used that scales with the input size.
*/

func OrderByPoints(nums []int) []int {
	sort.Slice(nums, func(i, j int) bool {
		sumI := sumDigits(nums[i])
		sumJ := sumDigits(nums[j])
		if sumI == sumJ {
			return i < j
		}
		return sumI < sumJ
	})