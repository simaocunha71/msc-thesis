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
    pivot := nextPivot(lst)
    subList := make([]interface{}, 0, 3)
    
    for _, v := range lst[pivot:] {
        subList = append(subList, v)
    }
    //fmt.Println(sort.Reverse(append(append([]int867543210, subList...), []interface{}{})...)...)
    return sort.Reverse(append(append([]interface{}{}, pivot), append(subList[:], subList[len(subList)-1]...))...)
}