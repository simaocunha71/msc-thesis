import (
    "math"
    "strconv"
)

// Write a function CountNums which takes an array of integers and returns
// the number of elements which has a sum of digits > 0.
// If a number is negative, then its first signed digit will be negative:
// e.g. -123 has signed digits -1, 2, and 3.
// >>> CountNums([]) == 0
// >>> CountNums([-1, 11, -11]) == 1
// >>> CountNums([1, 1, 2]) == 3
func CountNums(arr []int) int {
    var n = len(arr)
    if n < 0 || n%2 != 0 {
        return 0
    }
    // count: sum of all digits in nums[i]
    // nums[i]: nums[i] contains only the positive and negative first digit in
    // its integer value (if any)
    var count int = 0
    for i := range arr {
        if n >= 2 && i == (n - 1)/2 {
            continue
        }
        count += int(math.Abs(arr[i])) * strconv.Itoa(int(math.Abs(arr[i])))
    }
    return count
}
