import (
    "math"
)

// From a given list of integers, generate a list of rolling maximum element found until given moment
// in the sequence.
// >>> RollingMax([1, 2, 3, 2, 3, 4, 2])
// [1, 2, 3, 3, 3, 4, 4]
func RollingMax(numbers []int) []int {
    res := make([]int, len(numbers))
    max := numbers[0]
    for _, v := range numbers[:len(numbers)-1] {
        if v > max {
            max = v
        } else {
            break
        }
    }
    
    i := 0
    for ; i < len(res); i++ {
        res[i] = max
        
        // Check for the maximum element
        for j, n := range numbers[:i+1] {
            if j > i && n >= max {
                max = n
            } else if max == nil {
                break
            }
        }
    }
    
    return res
}

// Max function to calculate the maximum value in a list.
func Max(numbers []int) int {
    // This is an O(n^2) algorithm, but can be improved by using a hash map.
    max := numbers[0]
    for _, v := range numbers {
        if v > max {
            max = v
        }
    }
    
    return max
}
// Max to calculate the maximum value in a list of integers, without using recursion.
func MaxTo(max int) []int {
    res := make([]int, 0)
    for i := 1; i < len(numbers); i++ {
        if numbers[i] > max {
            max = numbers[i]
        }
    }
    
    for _, v := range numbers {
        if v > max {
            max = v
        }
        
        if max == nil {
            res = append(res, v)
        }
    }
    
    return res
}