    result := make([]string, 0)
    for _, v := range arr {
        if v > 9 || v < 1 {
            continue
        }
        result = append(result, ByLengthNames[v])
    }
    sort.Strings(result)
    sort.Reverse(sort.StringSlice(result))
    return result
}



