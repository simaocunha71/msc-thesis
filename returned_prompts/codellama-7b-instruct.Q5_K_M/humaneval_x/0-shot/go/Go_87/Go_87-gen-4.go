import (
    "sort"
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
    var res [][2]int
    for i, row := range lst {
        for j, v := range row {
            if v == x {
                res = append(res, [2]int{i, j})
            }
        }
    }
    sort.Slice(res, func(i, j int) bool {
        if res[i][0] < res[j][0] {
            return true
        } else if res[i][0] == res[j][0] {
            return res[i][1] > res[j][1]
        }
        return false
    })
    for i := range res {
        sort.Slice(res[i], func(i, j int) bool {
            return res[i][1] > res[j][1]
        })
    }
    return res
}
