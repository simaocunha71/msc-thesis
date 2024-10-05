Here is the solution in Golang:
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
Explanation:
The function `GetRow` iterates over the 2D list `lst` and checks each element to see if it is equal to `x`. If it is, it adds a new tuple to the result slice with the row and column indices. After all elements have been checked, it sorts the result slice in ascending order based on the row index, and then in descending order based on the column index. The sorted result is then returned. 

The time complexity of this solution is O(n*m), where n is the number of rows and m is the maximum number of columns in the list, because we need to iterate over all elements in the list. The space complexity is also O(n*m), because we need to store all elements that are equal to `x` in the result slice. 

This solution assumes that the input list `lst` is not empty and that `x` is an integer. It also assumes that the list `lst` does not contain any duplicate rows. If the list can contain duplicate rows, and you want to keep only the first occurrence of each row, you can modify the solution to use a map to keep track of the rows that have already been processed. 

If the list `lst` can be empty, you should add a check at the beginning of the function to return an empty slice if `lst` is empty. 

If `x` is not an integer, you should add a check at the beginning of the function to return an empty slice if `x` is not an integer. 

If the list `lst` can contain duplicate rows, and you want to keep all occurrences of each row, you can modify the solution to use a slice of slices to keep track of the rows that have already been processed. 

If the list `