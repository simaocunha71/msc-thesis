    result := make([][2]int, 0)
    var temp [2]int
    for i:=0; i<len(lst); i++{
        for j:=0; j<len(lst[i]); j++{
            if lst[i][j] == x{
                temp[0] = i
                temp[1] = j
                result = append(result, temp)
            }
        }
    }

    sort.Slice(result, func(i, j int) bool {
        return result[i][0] < result[j][0] || result[i][0] == result[j][0] && result[i][1] > result[j][1]
    })

    return result
}



