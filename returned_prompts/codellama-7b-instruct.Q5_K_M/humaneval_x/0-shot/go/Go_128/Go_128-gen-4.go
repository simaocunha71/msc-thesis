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

    var sign = 1
    var sum = 0
    for i := 0; i < len(arr); i++ {
        if arr[i] < 0 {
            sign = -1
        }
        if arr[i] != 0 {
            sum += sign * int(math.Abs(float64(arr[i])))
        }
    }

    return sum
}
