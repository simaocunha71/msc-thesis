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
    // 这里的sort是按照降序排好序，所以需要对其进行迭代。

    unique := make([]int, 0)
    for _, i := range x {
        if strconv.IsInt(strconv.Itoa(i)) {
            // 如果是字符串格式，那么不合法
            continue
        }
        if !uniqueContainsDigit(x, unique, i) {
            unique = append(unique, i)
        }
    }

    return unique
}