    result := make([][2]int, 0)
    for index, row := range lst {
        for i, v := range row {
            if v == x {
                result = append(result, [2]int{index, i})
            }
        }
    }
    sort.Slice(result, func(i, j int) bool {
        return result[i][0] < result[j][0]
    })
    for i, _ := range result {
        result[i] = [2]int{result[i][0], len(result[i])-1}
    }
    sort.Slice(result, func(i, j int) bool {
        return result[i][1] > result[j][1]
    })
    return result
}



