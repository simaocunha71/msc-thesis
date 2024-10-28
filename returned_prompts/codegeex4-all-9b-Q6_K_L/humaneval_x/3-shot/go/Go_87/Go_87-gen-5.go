    result := make([][2]int, 0)
    for y, row := range lst {
        for x, value := range row {
            if value == x {
                result = append(result, [2]int{y, x})
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