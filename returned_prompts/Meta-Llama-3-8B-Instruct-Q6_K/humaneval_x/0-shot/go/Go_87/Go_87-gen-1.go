```go
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


This code defines a function GetRow that takes a 2D list (or matrix) and an integer x as input. It iterates through each row of the matrix, and for each row, it iterates through each element. If the element is equal to x, it appends a tuple containing the row and column indices to the result list.

After populating the result list, it sorts the list based on the row indices in ascending order, and if two rows have the same index, it sorts them based on the column indices in descending order.

The function returns the sorted result list. The examples provided in the problem description are handled correctly by this code. For instance, GetRow([[1,2,3,4,5,6],[1,2,3,4,1,6],[1,2,3,4,5,1]], 1) returns [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]. If the input is [] and 1, it returns an empty list. If the input is [[], [1], [1, 2, 3]] and 3, it returns [(2, 2)].