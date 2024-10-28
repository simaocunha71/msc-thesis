Here is the Go function that implements the described functionality:

```go
import (
    "sort"
)

func GetRow(lst [][]int, x int) (result [][]int) {
    result = make([][]int, 0)
    for i, row := range lst {
        for j, val := range row {
            if val == x {
                result = append(result, []int{i, j})
            }
        }
    }
    sort.Slice(result, func(i, j int) bool {
        if result[i][0] == result[j][0] {
            return result[i][1] > result[j][1]
        }
        return result[i][0] < result[j][0]
    })
    return result
}
```

This function loops through each row of the input 2D list, and checks each value to see if it matches the target value `x`. If it does, it adds a tuple `(i, j)` to the result list, where `i` is the row index and `j` is the column index. After collecting all the coordinates, it sorts the result list based on the row index and then the column index in descending order. Finally, it returns the sorted result list.