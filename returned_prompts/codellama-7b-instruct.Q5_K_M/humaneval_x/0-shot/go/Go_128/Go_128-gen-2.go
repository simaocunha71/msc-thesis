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
    var signs []int
    var sum int
    for _, v := range arr {
        signs = append(signs, 1)
        if v < 0 {
            signs[len(signs)-1] = -1
        } else if v == 0 {
            signs[len(signs)-1] = 0
        }
        sum += int(math.Abs(float64(v)))
    }
    result := 1
    for i := 0; i < len(signs); i++ {
        result *= signs[i]
    }
    return sum * result
}

