    var result [][2]int = make([][2]int, 0)

    for i, row := range lst {
        for j, col := range row {
            if col == x {
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



