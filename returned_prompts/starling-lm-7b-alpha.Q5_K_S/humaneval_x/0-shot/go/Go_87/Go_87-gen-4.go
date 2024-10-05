    var result [] [2]int
    for i, row := range lst {
        for j, v := range row {
            if v == x {
                result = append(result, [2]int{i, j})
            }
        }
    }
    sort.Slice(result, func(i, j int) bool {
        return result[i][0] < result[j][0]
    })
    for i := range result {
        for j := i + 1; j < len(result); j++ {
            if result[i][0] == result[j][0] {
                sort.Slice(result[i:j+1], func(i, j int) bool {
                    return result[i][1] < result[j][1]
                })
            }
        }
    }
    return result
}

func main() {
    // GetRow([][]int{{1, 2, 3, 4, 5, 6}, {1, 2, 3, 4, 1, 6}, {1, 2, 3, 4, 5, 1}}, 1)
    // GetRow([][]int{{2, 3, 4, 5, 6}, {1, 2, 3, 4, 1, 6}, {1, 2, 3, 4, 5, 1}}, 1)
    // GetRow([][]int{{1, 2, 3, 4, 5, 6}, {1, 2, 3, 4, 1, 6}, {1, 2, 3, 4, 5, 1}, {1, 2, 3, 4, 5, 6}}, 1)
    GetRow([][]int{{1, 2, 3, 4, 5, 6}, {1, 2, 3, 4, 1, 6}, {1, 2, 3, 4, 5, 1}, {1, 2, 3, 4, 5, 6}}, 1)
    GetRow([][]int{{2, 