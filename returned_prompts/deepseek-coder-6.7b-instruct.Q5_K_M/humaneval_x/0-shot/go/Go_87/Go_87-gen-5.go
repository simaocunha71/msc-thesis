    var res [][2]int
    for rowIndex, row := range lst {
        for colIndex, value := range row {
            if value == x {
                res = append(res, [2]int{rowIndex, colIndex})
            }
        }
    }

    sort.Slice(res, func(i, j int) bool {
        if res[i][0] == res[j][0] {
            return res[i][1] > res[j][1]
        }
        return res[i][0] < res[j][0]
    })

    return res
}
```

## Explanation

The function GetRow takes a 2-dimensional list and an integer as input. It iterates over each row and column in the list and checks if the value is equal to the input integer. If it is, it appends the coordinates (row index and column index) to the result list.

After collecting all the coordinates, it sorts the list first by rows in ascending order, then by columns in descending order. This is done using the sort.Slice function, which takes a function that defines how to compare two elements. In this case, it first compares the rows, and if they are equal, it compares the columns.

Finally, it returns the sorted list of coordinates.

## Test cases

```go
func main() {
    fmt.Println(GetRow([][]int{{1,2,3,4,5,6},{1,2,3,4,1,6},{1,2,3,4,5,1}}, 1)) // [(0, 0) (1, 4) (1, 0) (2, 5) (2, 0)]
    fmt.Println(GetRow([][]int{}, 1)) // []
    fmt.Println(GetRow([][]int{{}, {1}, {1, 2, 3}}, 3)) // [(2, 2)]
}
```

## Complexity Analysis

The time complexity of this solution is O(n), where n is the total number of elements in the input list. This is because we are iterating over each element