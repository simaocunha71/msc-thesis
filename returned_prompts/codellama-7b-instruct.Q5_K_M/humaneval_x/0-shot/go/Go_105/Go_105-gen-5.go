    sort.Sort(sort.Reverse(sort.IntSlice(arr)))
    var result []string
    for _, v := range arr {
        if v >= 1 && v <= 9 {
            result = append(result, strconv.Itoa(v))
        }
    }
    return result
}































