Here is the solution:

```go
import (
    "sort"
)

func GetRow(lst [][]int, x int) (result [][]int) {
    var coordinates []struct {
        row, col int
    }
    for i, row := range lst {
        for _, v := range row {
            if v == x {
                coordinates = append(coordinates, struct {
                    row, col int
                }{i, len(row) - 1})
            }
        }
    }
    sort.Slice(coordinates, func(i, j int) bool {
        if coordinates[i].row != coordinates[j].row {
            return coordinates[i].row < coordinates[j].row
        }
        return coordinates[i].col > coordinates[j].col
    })
    for _, coord := range coordinates {
        result = append(result, []int{coord.row, coord.col})
    }
    return
}
```

The function `GetRow` iterates over the given 2D list `lst` and finds all the coordinates where the value is equal to `x`. It stores these coordinates in a slice of structs. Then it sorts this slice based on the row and column numbers. Finally, it constructs the result by converting the slice of structs into a slice of slices of integers and returns it. 

This function handles the edge cases where `lst` is empty or `x` is not found in `lst`. 

The time complexity of this function is O(n*m), where n is the number of rows in `lst` and m is the maximum number of columns in `lst`. This is because in the worst case, we need to iterate over all the elements in `lst`. The space complexity is also O(n*m), as we need to store all the coordinates in the slice `coordinates`.  If the value `x` is not found in `lst`, the function returns an empty slice.  If `lst` is empty, the function also returns an empty slice.  If `x` is found in `lst`, the function returns a non-empty slice of coordinates. 

The function is case-sensitive, i.e., it treats 1 and '1' as different values. It also treats 1 and 1.0 as different values. 

The function does not modify the original list `lst`. It only returns a new list of coordinates. 

The function is designed to handle the case where `lst` is a slice of slices of integers, and `x` is an integer. It can be easily