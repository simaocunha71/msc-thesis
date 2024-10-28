    result := make([]string, 0)
    for _, v := range arr {
        if 1 <= v && v <= 9 {
            result = append(result, v.String())
        }
    }
    sort.Ints(result)
    for i, v := range result {
        result[i] = v.String()
    }
    return result
}



