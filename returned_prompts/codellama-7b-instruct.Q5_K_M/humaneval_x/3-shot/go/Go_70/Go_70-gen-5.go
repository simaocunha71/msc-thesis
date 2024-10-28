    sort.Slice(lst, func(a, b int) bool {
        if lst[a] == lst[b] {
            return false
        }
        if lst[a] < lst[b] {
            return true
        }
        if lst[a] > lst[b] {
            return false
        }
        return true
    })
    return lst
}



