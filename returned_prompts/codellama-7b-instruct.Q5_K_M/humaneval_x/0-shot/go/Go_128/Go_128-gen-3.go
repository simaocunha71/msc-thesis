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

    var prod = 1
    var sum = 0

    for _, v := range arr {
        switch v {
        case 0:
            sum += 0
            prod *= 0
        case 1:
            sum += 1
            prod *= 1
        case -1:
            sum += 1
            prod *= -1
        }
    }

    return math.Abs(sum) * prod
}
