import (
    "sort"
    "strconv"
)

// Given a list of positive integers x. return a sorted list of all
// elements that hasn't any even digit.
// 
// Note: Returned list should be sorted in increasing order.
// 
// For example:
// >>> UniqueDigits([15, 33, 1422, 1])
// [1, 15, 33]
// >>> UniqueDigits([152, 323, 1422, 10])
// []
func UniqueDigits(x []int) []int {
    var s = make([]int, len(x))
    for _, v := range x {
        s[len(s)-1]++
        if strconv.IsInt(v) && strconv.Itoa(v)[0]%2 == 0 {
            return nil
        } else {
            s = append(s, v)
        }
    }
    reverse := false
    var ret []int
    for _, v := range s {
        if strconv.IsInt(v) && !reverse {
            ret = append(ret, v)
        } else {
            reverse = true
            break
        }
    }
    return reverse ? reversedSort(ret) : ret
}