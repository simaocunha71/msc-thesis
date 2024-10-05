    result := make([][2]int, 0)

    for row, col := range lst {
        for i, v := range col {
            if v == x {
                result = append(result, [2]int{row, i})
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



