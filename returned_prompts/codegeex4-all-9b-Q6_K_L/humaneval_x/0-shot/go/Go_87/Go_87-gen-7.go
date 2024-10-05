```go
func GetRow(lst [][]int, x int) [][2]int {
    coords := [][2]int{}
    for i, row := range lst {
        for j, num := range row {
            if num == x {
                coords = append(coords, [2]int{i, j})
            }
        }
    }
    sort.Slice(coords, func(i, j int) bool {
        if coords[i][0] != coords[j][0] {
            return coords[i][0] < coords[j][0]
        }
        return coords[i][1] > coords[j][1]
    })
    return coords
}
```
This solution works by iterating over the nested list and checking if each element is equal to x. If it is, it adds the coordinates of that element to a slice of coordinates. After iterating over the entire list, it sorts the coordinates by row in ascending order and by column in descending order. Finally, it returns the sorted coordinates.

This solution has a time complexity of O(n^2), where n is the total number of elements in the nested list. This is because it iterates over each element in the nested list once. The sorting operation also has a time complexity of O(n log n), where n is the number of coordinates. Therefore, the overall time complexity of the solution is O(n^2 + n log n).