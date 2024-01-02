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
    // write your code here
    sort.Ints(x + 1, lst...)
    
    var results = make([][2]int,[])
    for _, x := range lst {
        if len(x) != 0 {
            results = append(results, [2]int{0, len(x)-1})
        }
        else {
            break
        }
    }
    
    sort.Ints(len(lst[0]) - x+1, results...)
    
    return results
}
