import (
    "sort"
    "math"
)

// You are given a 2 dimensional data, as a nested lists,
// which is similar to matrix, however, unlike matrices,
// each row may contain a different number of columns.
// Given lst, and integer x, find integers x in the list,
// and return list of tuples, [(x1, y1), (x2, y2) ...] such that
// each tuple is a coordinate - (row, columns), starting with 0.
// Sort coordinates initially by rows in ascending order.
// Also, sort coordinates of the row by columns in descending order.
// 
// Examples:
// GetRow([
// [1,2,3,4,5,6],
// [1,2,3,4,1,6],
// [1,2,3,4,5,1]
// ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
// GetRow([], 1) == []
// GetRow([[], [1], [1, 2, 3]], 3) == [(2, 2)]
func GetRow(lst [][]int, x int) [][2]int {
    // Your code here
    // 1. first sort the list by rows
    // 2. then sort each row by columns in descending order
    // 3. finally find the x
    // 4. return the list of tuples
    // if there is no x, return []
    // if lst is empty return []
    if lst == nil || len(lst) == 0 {
        return [][]int{}
    }
    // sort the rows
    sort.SliceStable(lst, func(i, j int) bool {
        return len(lst[i]) < len(lst[j])
    })
    // sort the columns
    for i := 0; i < len(lst); i++ {
        sort.SliceStable(lst[i], func(j, k int) bool {
            return lst[i][j] > lst[i][k]
        })
    }