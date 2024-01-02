import (
    "math"
    "sort"
)

// You are given a list of integers.
// Write a function NextSmallest() that returns the 2nd smallest element of the list.
// Return nil if there is no such element.
// 
// NextSmallest([1, 2, 3, 4, 5]) == 2
// NextSmallest([5, 1, 4, 3, 2]) == 2
// NextSmallest([]) == nil
// NextSmallest([1, 1]) == nil
func NextSmallest(lst []int) interface{} {
    if len(lst) < 2 {
        return nil
    }
    
    pivot := (len(lst)-1)/2
    leftSize := len(lst) - (pivot + 1)
    rightSize := len(lst) - pivot
    var swap int = 0
    for i, _ := range lst {
        if i < pivot+leftSize {
            // exchange
            swap = i
            break
        } else if i > pivot {
            swap++
        }
    }
    
    // swap the element which has a smaller value with pivot
    lst[swap] = lst[pivot]
    return pivot
}