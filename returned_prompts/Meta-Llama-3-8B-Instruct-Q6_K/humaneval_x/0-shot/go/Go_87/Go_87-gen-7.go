Here is a Go function that implements the required functionality:

```go
func GetRow(lst [][]int, x int) (result [][2]int) {
    result = make([][2]int, 0)
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

This function iterates over each row and each element in the 2D list. If an element matches the given number `x`, it is added to the `result` slice. After finding all elements that match `x`, the function sorts the `result` slice based on the row and then the column. The sorting is done using the `sort.Slice` function from the `sort` package. The sorting function is a lambda function that returns `true` if the first element should come before the second element, and `false` otherwise. If the rows are the same, it compares the columns in descending order. If the rows are different, it compares the rows in ascending order. The sorted `result` slice is then returned.