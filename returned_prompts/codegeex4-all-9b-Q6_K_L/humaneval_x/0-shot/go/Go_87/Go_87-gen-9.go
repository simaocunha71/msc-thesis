```go
func GetRow(lst [][]int, x int) [][2]int {
    var ans [][2]int
    for i, row := range lst {
        for j, y := range row {
            if y == x {
                ans = append(ans, [2]int{i, j})
            }
        }
    }
    sort.Slice(ans, func(i, j int) bool {
        if ans[i][0] == ans[j][0] {
            return ans[i][1] > ans[j][1]
        }
        return ans[i][0] < ans[j][0]
    })
    return ans
}
```
This solution iterates through the given list of lists (lst) and checks if the value of each element is equal to x. If it is, it appends the coordinates of the element (row and column indices) to the answer list (ans). After iterating through all elements, it sorts the answer list first by row index in ascending order, and then by column index in descending order. Finally, it returns the sorted answer list.

The time complexity of this solution is O(n^2), where n is the total number of elements in the list of lists (lst). This is because the solution iterates through each element in the list of lists and performs constant time operations (checking for equality and appending to the answer list). The sorting operation has a time complexity of O(n log n), where n is the number of elements in the answer list. Therefore, the overall time complexity of the solution is O(n^2 + n log n).