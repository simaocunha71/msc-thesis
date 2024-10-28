    result := make([]string, 0)
    for _, value := range arr {
        if value > 0 && value <= 9 {
            result = append(result, "OneTwoThreeFourFiveSixSevenEightNine"[:value])
        }
    }
    sort.Strings(result)
    sort.Reverse(sort.StringSlice(result))
    return result
}



