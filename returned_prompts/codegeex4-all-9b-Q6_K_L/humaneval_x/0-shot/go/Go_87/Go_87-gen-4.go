```go
func GetRow(lst [][]int, x int) [][2]int {
    coordinates := [][2]int{}
    for i, row := range lst {
        for j, val := range row {
            if val == x {
                coordinates = append(coordinates, [2]int{i, j})
            }
        }
    }
    sort.Slice(coordinates, func(i, j int) bool {
        if coordinates[i][0] < coordinates[j][0] {
            return true
        } else if coordinates[i][0] > coordinates[j][0] {
            return false
        } else {
            return coordinates[i][1] > coordinates[j][1]
        }
    })
    return coordinates
}
```
这段代码实现了题目要求的功能。它首先遍历输入的二维列表，找到与目标整数x相等的元素，并将它们的坐标存储在一个二维数组中。然后，它使用sort.Slice函数对坐标进行排序，首先按照行号升序排序，如果行号相同，则按照列号降序排序。最后，它返回排序后的坐标数组。

这个解决方案的时间复杂度为O(n^2)，其中n是二维列表中的元素数量。空间复杂度为O(m)，其中m是目标整数x在二维列表中出现的次数。