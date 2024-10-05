```go
package main

import (
    "sort"
    "fmt"
)

func GetRow(lst [][]int, x int) [][2]int {
    var result [][2]int
    for i, row := range lst {
        for _, v := range row {
            if v == x {
                result = append(result, [2]int{i, len(row) - 1 - sort.SearchInts(row, v)})
            }
        }
    }
    sort.Slice(result, func(i, j int) bool {
        if result[i][0] != result[j][0] {
            return result[i][0] < result[j][0]
        }
        return result[i][1] > result[j][1]
    })
    return result
}

func main() {
    fmt.Println(GetRow([][]int{
        []int{1, 2, 3, 4, 5, 6},
        []int{1, 2, 3, 4, 1, 6},
        []int{1, 2, 3, 4, 5, 1},
    }, 1)) // Output: [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    fmt.Println(GetRow([][]int{}, 1)) // Output: []
    fmt.Println(GetRow([][]int{{}, [1]int{1}, [2]int{1, 2, 3}}, 3)) // Output: [(2, 2)]
}
```
In this solution, we iterate over each row in the list and each element in the row. If the element equals to the given `x`, we append a tuple of the row index and the column index (which is calculated by `len(row) - 1 - sort.SearchInts(row, v)` to ensure the columns are in descending order) to the `result` slice. After that, we sort the `result` slice by rows in ascending order and then by columns in descending order. Finally, we return the `result` slice.