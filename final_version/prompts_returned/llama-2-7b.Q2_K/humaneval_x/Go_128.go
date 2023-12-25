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
    var productArr = arr[0]
    for _, e := range arr[1:] {
        switch c := int64(e); {
            case c > 0:
                productArr += c * math.Pow10(int64(-1))
            case c < 0 && -c >= 0:
                productArr -= c * math.Pow10(int64(-1))
            default:
                productArr = 0
        }
    }
    return productArr
}
