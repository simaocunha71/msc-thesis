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
    sort.Ints(lst)
    return lst[1]
}

