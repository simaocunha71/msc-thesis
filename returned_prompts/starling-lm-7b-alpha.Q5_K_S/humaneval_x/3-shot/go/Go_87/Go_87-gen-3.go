    result := make([][2]int, 0)
    for i, row := range lst {
        for j, val := range row {
            if val == x {
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
                if result[i][1] < result[j][1] {
                    result[i], result[j] = result[j], result[i]
                }
            }else if result[i][0] > result[j][0] {
                result[i], result[j] = result[j], result[i]
            }
        }
    }
    return result
}



