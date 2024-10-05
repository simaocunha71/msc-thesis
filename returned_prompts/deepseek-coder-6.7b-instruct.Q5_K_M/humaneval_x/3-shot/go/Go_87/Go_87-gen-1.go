    var res [][2]int
    for i, row := range lst {
        for j, col := range row {
            if col == x {
                res = append(res, [2]int{i, j})
            }
        }
    }

    sort.Slice(res, func(i, j int) bool {
        if res[i][0] == res[j][0] {
            return res[i][1] > res[j][1]
        } 
        return res[i][0] < res[j][0]
    })

    return res
}



