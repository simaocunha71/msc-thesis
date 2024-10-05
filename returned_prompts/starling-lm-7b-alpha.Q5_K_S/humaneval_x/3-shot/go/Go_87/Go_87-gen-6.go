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
        result[i][1] = len(result[i][1]) - result[i][1]
    }
    sort.Slice(result, func(i, j int) bool {
        return result[i][1] > result[j][1]
    })

    return result
}



