    sort.Slice(lst, func(i, j int) bool {
        if len(lst[i:]) <= 1 {
            return false
        }
        if len(lst[i:]) == 2 {
            return lst[i] < lst[i+1]
        }
        return lst[i] < lst[i+len(lst[i:])//2]
    })
    return lst
}