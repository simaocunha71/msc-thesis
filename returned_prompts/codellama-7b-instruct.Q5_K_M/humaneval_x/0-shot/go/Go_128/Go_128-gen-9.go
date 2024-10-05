import (
    "math"
)

// You are given an array arr of integers and you need to return
// sum of magnitudes of integers multiplied by product of all signs
// of each number in the array, represented by 1, -1 or 0.
// Note: return nil for empty arr.
// 
// Example:
// >>> ProdSigns([1, 2, 2, -4]) == -9
// >>> ProdSigns([0, 1]) == 0
// >>> ProdSigns([]) == nil
func ProdSigns(arr []int) interface{} {
    if len(arr) == 0 {
        return nil
    }
    res := 0
    for _, v := range arr {
        res += int(math.Abs(float64(v)))
    }
    sign := 1
    for _, v := range arr {
        if v < 0 {
            sign *= -1
        }
    }
    return res * sign
}
