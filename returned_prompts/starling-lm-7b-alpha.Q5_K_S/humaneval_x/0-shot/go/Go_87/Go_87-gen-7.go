    var result [] [2]int
    for i, row := range lst {
        if len(row) > 0 && row[0] == x {
            result = append(result, [2]int{i, sort.SearchInts(row, x)})
        }
    }
    sort.Slice(result, func(i, j int) bool {
        return result[i][0] < result[j][0]
    })
    return result
}




func GetRow(lst [][]int, x int) [][2]int {
    var result [] [2]int
    for i, row := range lst {
        if len(row) > 0 && row[0] == x {
            result = append(result, [2]int{i, sort.SearchInts(row, x)})
        }
    }
    sort.Slice(result, func(i, j int) bool {
        return result[i][0] < result[j][0]
    })
    return result
}



func GetRow(lst [][]int, x int) [][2]int {
    var result [] [2]int
    for i, row := range lst {
        if len(row) > 0 && row[0] == x {
            result = append(result, [2]int{i, sort.SearchInts(row, x)})
        }
    }
    sort.Slice(result, func(i, j int) bool {
        return result[i][0] < result[j][0]
    })
    return result
}



































































































































