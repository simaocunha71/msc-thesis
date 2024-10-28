    sort.Slice(lst, func(i, j int) bool {
        if len(lst[i]) == len(lst[j]) {
            return lst[i] < lst[j]
        }
        return len(lst[i]) < len(lst[j])
    })
    return lst
}



