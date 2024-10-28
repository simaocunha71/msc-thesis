    var res [][2]int
    for i, row := range lst {
        for j := range row {
            if row[j] == x {
                res = append(res, [2]int{i, j})
            }
        }
    }
    sort.Slice(res, func(i, j int) bool {
        return res[i][0] < res[j][0]
    })

    for i := range res {
        for j := i + 1; j < len(res); j++ {
            if res[i][0] == res[j][0] {
                for k := range res[i][1]; k < range res[j][1]; k++ {
                    if res[i][1][k] > res[j][1][k] {
                        res[i], res[j] = res[j], res[i]
                    }
                }
            } else {
                break
            }
        }
    }

    return res
}

// GetRow returns a list of tuples, [(x1, y1), (x2, y2) ...] such that
// each tuple is a coordinate - (row, columns), starting with 0.
// Sort coordinates initially by rows in ascending order.
// Also, sort coordinates of the row by columns in descending order.
func GetRow(lst [][]int, x int) [][]int {
    var res [][2]int
    for i, row := range lst {
        for j := range row {
            if row[j] == x {
                res = append(res, [2]int{i, j})
            }
        }
    }
    sort.Slice(res, func(i, j int) bool {
        return res[i][0] < res[j][0]
    })

    for i := range res {
        for j := i + 1; j < len(res); j++ {
            if res[i][0] == res[j][0] {
                for k := range res[i][1]; k < range res[j][1]; k++ {
                