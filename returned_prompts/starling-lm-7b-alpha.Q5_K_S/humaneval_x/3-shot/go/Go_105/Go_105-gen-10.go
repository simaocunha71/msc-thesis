    result := make([]string,0)
    for _, i := range arr {
        if i > 0 && i < 10 {
            result = append(result, ByLengthNumber(i))
        }
    }
    sort.Strings(result)
    sort.Slice(result, func(i, j int) bool { return result[i] > result[j] })
    return result
}



