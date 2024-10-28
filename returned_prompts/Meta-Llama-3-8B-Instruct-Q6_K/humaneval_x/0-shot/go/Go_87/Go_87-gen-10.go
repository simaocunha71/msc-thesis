Here is a solution using Go. The idea is to iterate over each row in the list, and for each row, iterate over each element. If the element is equal to x, add the coordinates to the result slice.

```go
import (
    "sort"
)

func GetRow(lst [][]int, x int) [][2]int {
    result := make([][2]int, 0)
    for i, row := range lst {
        for j, v := range row {
            if v == x {
                result = append(result, [2]int{i, j})
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
```

In this code, we first initialize an empty slice `result` to store the coordinates of the elements equal to x. Then, we iterate over each row in the list, and for each row, we iterate over each element. If the element is equal to x, we add the coordinates (i, j) to the `result` slice.

After that, we sort the `result` slice. The sorting function is a lambda function that takes two indices i and j as arguments. If the rows of the two coordinates are different, it compares the rows. If the rows are the same, it compares the columns in descending order.

Finally, we return the sorted `result` slice. The time complexity of this solution is O(n * m), where n is the number of rows and m is the maximum number of columns in the list. The space complexity is O(k), where k is the number of elements equal to x. 