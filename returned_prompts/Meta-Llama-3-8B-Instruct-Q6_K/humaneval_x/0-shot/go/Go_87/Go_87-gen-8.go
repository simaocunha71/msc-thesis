Here is the solution in Go:

```go
import (
    "sort"
)

func GetRow(lst [][]int, x int) [][2]int {
    var result [][2]int
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


This function first iterates over each row in the input list `lst`. For each row, it checks each element to see if it's equal to `x`. If it is, it appends the coordinates (i, j) to the result slice. After finding all the coordinates, it sorts the result slice. The sorting function checks if the rows are equal. If they are, it sorts the columns in descending order. If the rows are not equal, it sorts the rows in ascending order. Finally, it returns the sorted result slice.