    result  := make([][2]int, 0)

    for rowIndex, row := range lst  {
        for colIndex, value := range row  {
            if value == x  {
                result = append(result, [2]int{rowIndex, colIndex})
            }
        }
    }

    sort.Slice(result, func(i, j int) bool {
        if result[i][0] == result[j][0]  {
            return result[i][1] > result[j][1]
        }
        return result[i][0] < result[j][0]
    })

    return result
}



