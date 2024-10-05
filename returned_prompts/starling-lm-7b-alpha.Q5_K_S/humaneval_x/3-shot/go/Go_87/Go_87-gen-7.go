    result := make([][2]int, 0)
    for i, row := range lst {
        if i >= 0 && len(row) >= 0 {
            for j, elem := range row {
                if elem == x {
                    result = append(result, [2]int{i, j})
                }
            }
        }
    }
    sort.Slice(result, func(i, j int) bool {
        return result[i][0] < result[j][0]
    })

    for i, _ := range result {
        sort.Slice(result[i][1:], func(i, j int) bool {
            return result[i][1] > result[j][1]
        })
    }
    return result
}



