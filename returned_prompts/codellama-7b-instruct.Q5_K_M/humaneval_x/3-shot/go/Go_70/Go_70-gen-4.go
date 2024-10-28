    sort.Slice(lst, func(i, j int) bool {
        if lst[i] != lst[j] {
            if lst[i] < lst[j] {
                return true
            }
            if lst[i] > lst[j] {
                return false
            }
            return i < j
        }
        return i < j
    })
    return lst
}



