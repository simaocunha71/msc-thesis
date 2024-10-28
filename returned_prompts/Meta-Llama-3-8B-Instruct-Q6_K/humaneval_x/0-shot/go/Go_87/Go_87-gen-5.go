Here is a Go function that solves the problem. It iterates over each row in the 2D list and checks if the value at the current column is equal to the target value. If it is, it adds the coordinates to the result list. The result list is then sorted based on the row index in ascending order and the column index in descending order.

```go
import (
    "sort"
)

func GetRow(lst [][]int, x int) [][2]int {
    result := make([][2]int, 0)
    for i, row := range lst {
        for j, val := range row {
            if val == x {
                result = append(result, [2]int{i, j})
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

This function works by iterating over each element in the 2D list and checking if the value is equal to the target value. If it is, it adds the coordinates to the result list. The result list is then sorted based on the row index in ascending order and the column index in descending order.

The time complexity of this function is O(n*m), where n is the number of rows and m is the maximum number of columns in the 2D list. This is because we are iterating over each element in the 2D list once. The space complexity is O(k), where k is the number of elements in the result list. This is because we are storing the coordinates in a slice.