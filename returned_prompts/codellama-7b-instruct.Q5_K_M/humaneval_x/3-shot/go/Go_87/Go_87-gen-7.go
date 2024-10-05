    result := make([][2]int, 0)

    for i := 0; i < len(lst); i++{
        for j := 0; j < len(lst[i]); j++{
            if lst[i][j] == x{
                result = append(result, [2]int{i, j})
            }
        }
    }

    sort.Slice(result, func(i, j int) bool {
        if result[i][0] < result[j][0] {
            return true
        }else if result[i][0] == result[j][0] && result[i][1] > result[j][1]{
            return true
        }
        return false
    })
    return result
}



