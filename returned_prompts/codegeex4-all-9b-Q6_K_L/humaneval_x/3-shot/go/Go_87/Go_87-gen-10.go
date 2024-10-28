    result := make([][2]int, 0)
    for row, values := range lst {
        for column, value := range values {
            if value == x {
                result = append(result, [2]int{row, column})
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

