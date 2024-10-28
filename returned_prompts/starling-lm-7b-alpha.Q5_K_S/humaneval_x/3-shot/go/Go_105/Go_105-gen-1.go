    var result = make([]string, 0)
    for _, i := range arr {
        if i >=1 && i <= 9 {
            result = append(result, "OneTwoThreeFourFiveSixSevenEightNine"[i-1])
        }
    }
    sort.Slice(result, func(i, j int)bool {
        return len(result[i]) < len(result[j])
    })
    sort.Slice(result, func(i, j int)bool {
        return result[i] < result[j]
    })
    return result
}



