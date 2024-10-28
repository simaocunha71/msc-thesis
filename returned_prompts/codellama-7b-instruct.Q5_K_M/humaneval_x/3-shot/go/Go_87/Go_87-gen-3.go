    result := make([][2]int, 0)
    for i, v := range lst {
        for j, w := range v {
            if w == x {
                result = append(result, [2]int{i, j})
            }
        }
    }

    sort.Slice(result, func(i, j int) bool {
        if result[i][0] < result[j][0] {
            return true
        } else if result[i][0] > result[j][0] {
            return false
        } else {
            return result[i][1] > result[j][1]
        }
    })

    return result
}



