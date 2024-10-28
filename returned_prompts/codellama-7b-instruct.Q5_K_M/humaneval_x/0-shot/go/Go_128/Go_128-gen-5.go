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
    var sum float64 = 0
    var product float64 = 1
    for _, i := range arr {
        sum += math.Abs(float64(i))
        if i > 0 {
            product *= 1
        } else if i < 0 {
            product *= -1
        } else {
            product *= 0
        }
    }
    return product * sum
}
