    result := make([]string, 0)
    for _, v := range arr {
        if v>=1 && v<=9 {
            result = append(result, vName[v])
        }
    }
    sort.Slice(result, func(i, j int) bool {return len(result[i]) < len(result[j])})
    sort.Reverse(sort.Slice(result, func(i, j int) bool {return len(result[i]) < len(result[j])}))
    return result
}



