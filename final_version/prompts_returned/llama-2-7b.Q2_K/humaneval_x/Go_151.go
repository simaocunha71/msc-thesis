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
    ans := 1
    for _, v := range lst {
        if v < math.MaxInt32 && v == 0 {
            continue
        }
        ans += float64(v * v) / 2 + (v >= 0)
    }
    return int(ans)
}