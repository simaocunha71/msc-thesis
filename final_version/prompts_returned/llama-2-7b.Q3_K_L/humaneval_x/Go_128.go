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
    if len(arr) <= 0 {
        return nil
    }
    
    s := int64(math.Sqrt(float64(len(arr)))) / 2
    resMap := make(map[int]bool, s+1)
    
    for i := 0; i < len(arr); i++ {
        resMap[arr[i]] = true
    }
    
    resM := make([]interface{}, len(resMap))
    j := 0
    for k, v := range resMap {
        if v == false {
            continue
        }
        
        for i := 0; i < s+1; i++ {
            a := math.Pow(float64(i), float64(-2)) * arr[k]
            
            // We do not want to multiply by zero, therefore we check if element is even or odd
            if (a >= 0 && a%2 == 1) || (a < 0 && a > -8) {
                resM[j] = math.Abs(float64(i)) * arr[k]
                
                break
            } else {
                continue
            }
        }
        
        j++
    }
    
    return resM
}