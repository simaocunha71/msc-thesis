    var result [][2]int
    for i, row := range lst {
        for j, num := range row {
            if num == x {
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

