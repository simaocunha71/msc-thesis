    var res [][2]int
    for i, row := range lst {
        for j, val := range row {
            if val == x {
                res = append(res, [2]int{i, j})
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

This solution first iterates over the 2d list to find all occurrences of the given integer x. It then sorts these coordinates first by row and then by column in descending order. This is done by using the built-in `sort.Slice` function in Go.

It uses a custom sort function that first compares the rows, and if they are equal, it then compares the columns.

This solution has a time complexity of O(n*m), where n is the number of rows and m is the average number of columns in the rows. This is because it must iterate over all elements of the 2d list.

The space complexity is O(k), where k is the number of occurrences of x in the list. This is because it stores all the coordinates of x in the list.

This solution assumes that the input list is a 2d list of integers and that x is an integer.

Note: The sort function in Go is not stable, meaning that it does not preserve the relative order of equal elements. However, this solution ensures that if two elements have the same row, they are sorted by column in descending order.




## 5. 

