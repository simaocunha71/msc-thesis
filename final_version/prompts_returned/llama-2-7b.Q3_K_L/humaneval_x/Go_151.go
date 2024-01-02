import (
    "math"
)

// Given a list of numbers, return the sum of squares of the numbers
// in the list that are odd. Ignore numbers that are negative or not integers.
// 
// DoubleTheDifference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
// DoubleTheDifference([-1, -2, 0]) == 0
// DoubleTheDifference([9, -2]) == 81
// DoubleTheDifference([0]) == 0
// 
// If the input list is empty, return 0.
func DoubleTheDifference(lst []float64) int {
    if len(lst) <= 0 {
        return 0
    }
    
    nums, sqrs := make([]int, len(lst)), make([]int, len(lst))
    i := 0
    for ; i < len(lst); i++ {
        if lst[i] == float64(-1) || lst[i] == float64(0) {
            break
        } else {
            sqrs[i] = math.Sqrt((lst[i]*lst[i]) + 1)
        }
    }
    
    for ; i < len(sqrs); i++ {
        nums[i] = lst[i] * (2-int(float64(lst[i]*lst[i]))) / sqrs[i]
    }
    
    total := 0.0
    for _, n := range nums {
        total += n
    }
    return int(total)
}