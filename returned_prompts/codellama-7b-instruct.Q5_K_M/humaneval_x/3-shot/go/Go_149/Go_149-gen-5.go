    sort.Slice(lst, func (i, j int) bool {
        if len(lst[i]) != len(lst[j]) {
            return len(lst[i]) < len(lst[j])
        } else {
            return lst[i] < lst[j]
        }
    })
    return lst
}



