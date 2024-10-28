    var result []string
    sort.Slice(lst, func(i, j int) bool {
        if len(lst[i]) != len(lst[j]) {
            return len(lst[i]) < len(lst[j])
        }
        return lst[i] < lst[j]
    })
    for _, s := range lst {
        if len(s)%2 == 0 {
            result = append(result, s)
        }
    }
    return result
}
