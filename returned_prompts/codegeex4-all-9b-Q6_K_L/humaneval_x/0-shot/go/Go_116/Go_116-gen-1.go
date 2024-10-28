func SortArray(arr []int) []int {
    var res []int
    for _, v := range arr {
        res = append(res, v)
    }
    sort.SliceStable(res, func(i, j int) bool {
        countI := 0
        countJ := 0
        for _, num := range res {
            if num & 1 == 1 {
                countI++
            }
        }
        for _, num := range res {
            if num & 1 == 1 {
                countJ++
            }
        }
        if countI != countJ {
            return countI < countJ
        }
        return res[i] < res[j]
    })
    return res
}

B:
func SortArray(arr []int) []int {
    var res []int
    for _, v := range arr {
        res = append(res, v)
    }
    sort.SliceStable(res, func(i, j int) bool {
        countI := 0
        countJ := 0
        for _, num := range res {
            if num & 1 == 1 {
                countI++
            }
        }
        for _, num := range res {
            if num & 1 == 1 {
                countJ++
            }
        }
        if countI != countJ {
            return countI < countJ
        }
        return res[i] < res[j]
    })
    return res
}

C:
func SortArray(arr []int) []int {
    var res []int
    for _, v := range arr {
        res = append(res, v)
    }
    sort.SliceStable(res, func(i, j int) bool {
        countI := 0
        countJ := 0
        for _, num := range res {
            if num & 1 == 1 {
                countI++
            }
        }
        for _, num := range res {
            if num & 1 == 1 {
                countJ++
            }
        }
        if countI != countJ {
            return countI < countJ
        }
        return res[i] < res[j]
    })
    return res
}

D:
func SortArray(arr []int) []int {
    var res []int
    for _, v := range arr {
        res = append(res, v)
    }
    sort.SliceStable(res, func(i, j int) bool {
        countI := 0
        countJ